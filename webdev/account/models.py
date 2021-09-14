from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='نویسنده')
    special_user = models.DateTimeField(default=timezone.now, verbose_name='ویژه تا', )

    def is_specialuser(self):
        if self.special_user > timezone.now():
            return True
        return False
