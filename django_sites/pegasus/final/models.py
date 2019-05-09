from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        abstract = True

    # Form attributes
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(max_length=10)
    physical_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='final/profile_pictures', blank=True, null=True)
    creation_time = models.DateField(default=now, editable=False)

    # Account attributes
    is_student = models.BooleanField()
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=500)

    # Compatibility scores
    cleanliness = models.IntegerField(blank=True, null=True)
    socialness = models.IntegerField(blank=True, null=True)
    partiness = models.IntegerField(blank=True, null=True)

    # Internal attributes
    permission_level = -1  # 0: Administrator, 1: Landlord, 2: Star Tenant, 3: Student, 4: Unverified user
    last_login = models.DateTimeField(blank=True, null=True)

    def update(
            self, email=None, username=None, date_of_birth=None, physical_address=None, city=None, state=None,
            zip_code=None, password=None, first_name=None, last_name=None, bio=None, phone_number=None, is_student=None,
            cleanliness=None, socialness=None, partiness=None, profile_picture=None
    ):
        if email is not None:
            self.email = email

        if username is not None:
            self.username = username

        if date_of_birth is not None:
            self.date_of_birth = date_of_birth

        if physical_address is not None:
            self.physical_address = physical_address

        if city is not None:
            self.city = city

        if state is not None:
            self.state = state

        if zip_code is not None:
            self.zip_code = zip_code

        if password is not None:
            self.password = password

        if first_name is not None:
            self.first_name = first_name

        if last_name is not None:
            self.last_name = last_name

        if bio is not None:
            self.bio = bio

        if phone_number is not None:
            self.phone_number = phone_number

        if is_student is not None:
            self.is_student = is_student

        if cleanliness is not None:
            self.cleanliness = cleanliness

        if socialness is not None:
            self.socialness = socialness

        if partiness is not None:
            self.partiness = partiness

        if profile_picture is not None:
            self.profile_picture = profile_picture

    def __str__(self):
        return self.email


class RegisteredUser(User):
    class Meta:
        db_table = 'final_unverified_users'

    permission_level = 4


class VerifiedUser(RegisteredUser):
    class Meta:
        db_table = 'final_verified_users    '

    permission_level = 3


class Administrator(VerifiedUser):
    class Meta:
        db_table = "final_admins"

    permission_level = 0
    is_staff = True


class Landlord(VerifiedUser):
    class Meta:
        db_table = "final_landlords"

    permission_level = 1
    agency = models.CharField(max_length=50, blank=True, null=True)

    def update_agency(self, agency):
        self.agency = agency


class StarTenant(VerifiedUser):
    class Meta:
        db_table = "final_star_tenants"

    permission_level = 2


class Student(VerifiedUser):
    class Meta:
        db_table = "final_students"

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
        db_table = 'final_residences'

    residence_id = models.AutoField(primary_key=True)
    residence_options = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('room', 'Room'),
        ('garage', 'Garage'),
        ('in_law_unit', 'In-Law Unit'),
        ('other', 'Other')
    ]

    photo = models.ImageField(upload_to='final/residence_pictures')
    residence_type = models.CharField(max_length=50, choices=residence_options)
    bed_count = models.IntegerField()
    bath_count = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    size = models.IntegerField()
    creation_time = models.DateField(default=now, editable=False)
    owner = models.CharField(max_length=15)
    price = models.FloatField(max_length=10)
    tenants = models.CharField(max_length=100)
    pet_friendly = models.BooleanField()
    pets_allowed = models.CharField(max_length=100, blank=True, null=True)
    limit_tenant_count = models.IntegerField(blank=True, null=True)
    current_tenant_count = models.IntegerField(blank=True, null=True)
    amenities = models.CharField(max_length=100, blank=True, null=True)
    utilities_included_rent = models.BooleanField()
    is_active = models.BooleanField()
    coordinates = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()

    def update(
            self, residence_type=None, bed_count=None, bath_count=None, address=None, city=None, state=None,
            zip_code=None, size=None, owner=None, price=None, tenants=None, pet_friendly=None, pets_allowed=None,
            limit_tenant_count=None, current_tenant_count=None, amenities=None, utilities_included_rent=None,
            is_active=None, description=None
    ):
        if residence_type is not None:
            self.residence_type = residence_type

        if bed_count is not None:
            self.bed_count = bed_count

        if bath_count is not None:
            self.bath_count = bath_count

        if address is not None:
            self.address = address

        if city is not None:
            self.city = city

        if state is not None:
            self.state = state

        if zip_code is not None:
            self.zip_code = zip_code

        if size is not None:
            self.size = size

        if price is not None:
            self.price = price

        if owner is not None:
            self.owner = owner

        if tenants is not None:
            self.tenants = tenants

        if pet_friendly is not None:
            self.pet_friendly = pet_friendly

        if pets_allowed is not None:
            self.pets_allowed = pets_allowed

        if limit_tenant_count is not None:
            self.limit_tenant_count = limit_tenant_count

        if current_tenant_count is not None:
            self.current_tenant_count = current_tenant_count

        if amenities is not None:
            self.amenities = amenities

        if utilities_included_rent is not None:
            self.utilities_included_rent = utilities_included_rent

        if is_active is not None:
            self.is_active = is_active

        if description is not None:
            self.description = description

    def __str__(self):
        return "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip_code)