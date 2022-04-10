from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Creates and saves a new user model
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :param extra_fields:
        :return: User
        """
        if not email:
            raise ValueError("Email field is required")
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a user as a superuser in the database via command line
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :param extra_fields:
        :return: user
        """
        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, verbose_name="email", unique=True)
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name")
    is_active = models.BooleanField(default=True, verbose_name="is active")
    is_admin = models.BooleanField(default=False, verbose_name="is staff")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'user'


class Manager(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="first name")
    last_name = models.CharField(max_length=150, verbose_name="last name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'manager'
