from django.contrib.auth.hashers import make_password, check_password
from .models import *
import requests


def encrypt_password(password):
    return make_password(password)


def remove_empty_dict(**input_dict):
    filtered_dict = {
        key: value for key, value in input_dict.items() if value is not '' and value is not False and value is not None
    }

    return filtered_dict


class AuthBackend:
    def authenticate(self, username=None, password=None, **kwargs):
        print("[INFO] Received auth request for '%s'." % username)
        try:
            user = RegisteredUser.objects.get(username=username)
            if user:
                user_password = user.password
                if check_password(password, user_password):
                    print("[INFO] Auth success.")
                    return user
                else:
                    print("[ERROR] Password mismatched. Auth rejected.")
                    return None

        except:
            print("[ERROR] Username not found. Auth rejected.")
            return None

    def get_user(self, user_id):
        try:
            return RegisteredUser.objects.get(pk=user_id)
        except:
            return None


# Get geocoding data (lat / long) for searched listings
def get_lat_long(residences):
    # List of dictionaries {'lat': xxx, 'lng':xxx}
    all_lat_lng = []
    for residence in residences:
        geodata = {
            'lat': 0,
            'lng': 0
        }
        addr = residence.address

        if addr:
            GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=' \
                                  + addr \
                                  + '&key=AIzaSyCbr6KeU9un_uLPpH581LUfOb8PE3zi1x0'
            params = {'address': addr}
            map_request = requests.get(GOOGLE_MAPS_API_URL, params=params)
            response = map_request.json()

            if len(response['results']) > 0:
                result = response['results'][0]
                geodata['lat'] = result['geometry']['location']['lat']
                geodata['lng'] = result['geometry']['location']['lng']
                all_lat_lng.append(geodata)
    return all_lat_lng