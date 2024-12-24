from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class UserModel(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
