from django.db import models
from django.utils.timezone import now

# Create your models here.
class Profile(object):
    def __init__(self, user_object):
        pass # TODO: implement profile logic


class User(models.Model):
    class Meta:
        abstract = True

    # Form attributes
    username = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=10)
    physical_address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to='demo/profile_pictures') # TODO: update to actual path, add validation
    creation_time = models.DateField(default=now, editable=False)

    # Internal attributes
    is_student = False
    permission_level = -1 # 0: Administrator, 1: Landlord, 2: Star Tenant, 3: Student, 4: Unverified user

    # Setters
    def update_email(self, email):
        self.email = email

    def update_username(self, username):
        self.username = username # TODO: add check to verify that username is not already taken

    def update_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth # TODO: add check to verify that DOB is valid

    def update_address(self, address):
        self.physical_address = address

    def __str__(self):
        return self.email


class DisabledUser(models.Model):
    class Meta:
        db_table = 'disabled_users'

    deletion_time = models.DateField(default=now, editable=False)
    secret_key = models.CharField(max_length=50)
    username = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField(max_length=100)


class UnverifiedUser(User):
    class Meta:
        db_table = 'unverified_users'

    permission_level = 4


class VerifiedUser(User):
    class Meta:
        db_table = 'verified_users'

    permission_level = 3

    def get_profile(self):
        return Profile(self)


class Administrator(VerifiedUser):
    class Meta:
        db_table = "admins"

    permission_level = 0


class Landlord(VerifiedUser):
    class Meta:
        db_table = "landlords"

    permission_level = 1
    agency = models.CharField(max_length=50, blank=True, null=True)

    def update_agency(self, agency):
        self.agency = agency


class StarTenant(VerifiedUser):
    class Meta:
        db_table = "star_tenants"

    permission_level = 2


class Student(VerifiedUser):
    class Meta:
        db_table = "students"

    permission_level = 3
    is_student = True
    is_tenant = False

    def update_tenant_status(self, status):
        if status:
            self.is_tenant = True
        else:
            self.is_tenant = False


class Domicile(models.Model):
    class Meta:
        db_table = 'residences'

    residence_id = models.AutoField(primary_key=True)
    residence_options = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('room', 'Room'),
        ('garage', 'Garage'),
        ('in_law_unit', 'In-Law Unit'),
        ('other', 'Other')
    ]

    residence_type = models.CharField(max_length=50, choices=residence_options)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()
    size = models.IntegerField()
    pet_friendly = models.BooleanField()
    pets_allowed = models.CharField(max_length=100, blank=True, null=True)
    limit_tenant_count = models.IntegerField(blank=True, null=True)
    current_tenant_count = models.IntegerField(blank=True, null=True)
    amenities = models.CharField(max_length=100, blank=True, null=True)
    utilities_included_rent = models.BooleanField()
    coordinates = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='demo/residence_pictures') # TODO: update to actual path, add validation
    creation_time = models.DateField(default=now, editable=False)

    def __str__(self):
        return "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip)


class ActiveListing(models.Model):
    class Meta:
        db_table = 'active_listings'

    residence = models.OneToOneField(
        'Domicile', on_delete=models.CASCADE, primary_key=True, to_field='residence_id'
    )
    tenants = models.CharField(max_length=100)
    owner = models.CharField(max_length=15)
    price = models.FloatField(max_length=10)


# TODO: Expired Listings, Direct Messages, Groups


