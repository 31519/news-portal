from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.files import ImageField
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError ("User must have email address")
        if not username:
            raise ValueError("User must have a valid username")
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user=self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
    


my_gender = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others')
)

class Account(AbstractBaseUser):
    first_name       = models.CharField(max_length=200, unique=True)
    last_name        = models.CharField(max_length=200, unique=True)
    username         = models.CharField(max_length=200, unique=True)
    email            = models.EmailField(max_length=200, unique=True)
    country          = models.CharField(max_length=200)
    state            = models.CharField(max_length=200)
    phone_number     = models.IntegerField(blank=True, null=True)
    gender           = models.CharField(max_length=200, choices=my_gender)

    # required field
    date_joined       = models.DateField(auto_now_add=True)
    last_login        = models.DateField(auto_now=True)
    is_admin          = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=False)
    is_staff          = models.BooleanField(default=False)
    is_superadmin     = models.BooleanField(default=False)

    USERNAME_FIELD    = 'email'
    REQUIRED_FIELDS   = ['username', 'first_name', 'last_name']

    objects           = MyAccountManager()

    def __str__(self):
        return self.email
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    images = models.ImageField(upload_to='images/profile', default='images/profile/def.jpg')
    phone = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.first_name
        


