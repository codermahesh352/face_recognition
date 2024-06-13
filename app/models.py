from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import numpy as np

class UserManager(BaseUserManager):
    def create_user(self, username, face_encoding, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if face_encoding is None:
            raise ValueError("Users must have a face encoding")
        
        user = self.model(username=username, face_encoding=face_encoding)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, face_encoding, password):
        user = self.create_user(username, face_encoding, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    face_encoding = models.BinaryField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['face_encoding']

    def __str__(self):
        return self.username

    def get_face_encoding(self):
        return np.frombuffer(self.face_encoding, dtype=np.float64)

    def set_face_encoding(self, encoding):
        self.face_encoding = encoding.tobytes()
