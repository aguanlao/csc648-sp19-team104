from django.db import models
from django.utils.timezone import now


class TextObject(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateField(default=now, editable=False)
    text = models.CharField(max_length=500)

    def get_creation_time(self):
        return self.creation_time

    def edit_text(self, text):
        self.text = text


class Message(TextObject):
    recipient = models.OneToOneField(
        'VerifiedUser', on_delete=models.CASCADE, to_field='username', related_name='recipient_id'
    )

    poster = models.OneToOneField(
        'VerifiedUser', on_delete=models.CASCADE, primary_key=True, to_field='username', related_name='message_poster_id'
    )

    def get_poster(self):
        return self.poster


class Post(TextObject):
    comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
        return True

    def remove_comment(self, comment):
        try:
            self.comments = [message for message in self.comments if message != comment]
            return True
        except:
            return False

    poster = models.OneToOneField(
        'VerifiedUser', on_delete=models.CASCADE, primary_key=True, to_field='username',
        related_name='post_poster_id'
    )

    def get_poster(self):
        return self.poster


class Comment(TextObject):
    def __init__(self, post):
        TextObject.__init__(self)
        self.parent_post = post

    def get_parent_post(self):
        return self.parent_post

    poster = models.OneToOneField(
        'VerifiedUser', on_delete=models.CASCADE, primary_key=True, to_field='username',
        related_name='comment_poster_id'
    )

    def get_poster(self):
        return self.poster


class User(models.Model):
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

    # TODO: update to actual path, add validation
    profile_picture = models.ImageField(upload_to='demo/profile_pictures', blank=True, null=True)
    creation_time = models.DateField(default=now, editable=False)

    # Account attributes
    is_student = models.BooleanField()
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=50)

    # Compatibility scores
    cleanliness = models.IntegerField(blank=True, null=True)
    socialness = models.IntegerField(blank=True, null=True)
    partiness = models.IntegerField(blank=True, null=True)

    # Internal attributes
    permission_level = -1 # 0: Administrator, 1: Landlord, 2: Star Tenant, 3: Student, 4: Unverified user

    def update(
            self, email=None, username=None, date_of_birth=None, physical_address=None, city=None, state=None, zip_code=None,
            password=None, first_name=None, last_name=None, bio=None, phone_number=None, is_student=None,
            cleanliness=None, socialness=None, partiness=None, profile_picture=None
    ):
        if email != None:
            self.email = email

        if username != None:
            self.username = username

        if date_of_birth != None:
            self.date_of_birth = date_of_birth

        if physical_address != None:
            self.address = physical_address

        if city != None:
            self.city = city

        if state != None:
            self.state = state

        if zip_code != None:
            self.zip_code = zip_code

        if password != None:
            self.password = password

        if first_name != None:
            self.first_name = first_name

        if last_name != None:
            self.last_name = last_name

        if bio != None:
            self.bio = bio

        if phone_number != None:
            self.phone_number = phone_number

        if is_student != None:
            self.is_student = is_student

        if cleanliness != None:
            self.cleanliness = cleanliness

        if socialness != None:
            self.socialness = socialness

        if partiness != None:
            self.partiness = partiness

        if profile_picture != None:
            self.profile_picture = profile_picture


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
    friends = []

    # TODO: define what a profile will be
    def get_profile(self):
        pass

    def add_friend(self, user):
        pass

    def remove_friend(self, user):
        pass

    def send_message(self, user):
        pass


class Administrator(VerifiedUser):
    class Meta:
        db_table = "admins"

    permission_level = 0

    # TODO
    def accept_listing(self):
        pass

    def remove_listing(self, listing):
        pass

    def update_listing(self, listing):
        pass

    def remove_user(self, user):
        pass


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
    zip_code = models.IntegerField()
    size = models.IntegerField()
    creation_time = models.DateField(default=now, editable=False)

    def __str__(self):
        return "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip_code)


class ActiveListing(models.Model):
    class Meta:
        db_table = 'active_listings'

    residence = models.OneToOneField(
        'Domicile', on_delete=models.CASCADE, primary_key=True, to_field='residence_id'
    )
    tenants = models.CharField(max_length=100)
    owner = models.CharField(max_length=15)
    price = models.FloatField(max_length=10)
    pet_friendly = models.BooleanField()
    pets_allowed = models.CharField(max_length=100, blank=True, null=True)
    limit_tenant_count = models.IntegerField(blank=True, null=True)
    current_tenant_count = models.IntegerField(blank=True, null=True)
    amenities = models.CharField(max_length=100, blank=True, null=True)
    utilities_included_rent = models.BooleanField()
    coordinates = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()

    # TODO: update to actual path, add validation
    photo = models.ImageField(upload_to='demo/residence_pictures')
