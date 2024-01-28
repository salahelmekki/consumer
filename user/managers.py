from django.contrib.auth.models import BaseUserManager, Group


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, username=None):
        """
        Creates and saves a simple user
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            # username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            # username=username

        )
        user.admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
