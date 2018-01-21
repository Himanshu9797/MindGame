from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	# fb_id = models.CharField(max_length=200, null=True, blank=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []



	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

