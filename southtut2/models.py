from django.db import models
import hashlib


class User(models.Model):

    username = models.CharField(max_length=255)
    password_salt = models.CharField(max_length=8, null=True)
    password_hash = models.CharField(max_length=40, null=True)
    name = models.TextField()

    def check_password(self, password):
        return hashlib.sha1(self.password_salt.encode('utf-8') + password.encode('utf-8')).hexdigest() == self.password_hash