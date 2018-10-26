from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin
)
from django.db import models
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):
	def create_user(self, email, username, date_of_birth, password=None):
		"""
        Creates and saves a User with the given email, username, date of
        birth and password.
        """
		if not email:
			raise ValueError("Users must have an email address")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			date_of_birth=date_of_birth,
		)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, username, date_of_birth, password):
		user = self.create_user(email, username, date_of_birth, password)
		user.is_admin = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	date_of_birth = models.DateField()
	avatar = models.ImageField(blank=True, null=True, upload_to='image/avatar')
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username', 'date_of_birth']

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email	

	def get_short_name(self):
		return self.email
		
	@property
	def is_staff(self):
		return self.is_admin
