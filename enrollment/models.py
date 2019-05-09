from django.db import models

# Create your models here.


class Member(models.Model):
  login_name = models.CharField(max_length = 255)
  full_japanese_name = models.CharField(max_length = 255)
  full_english_name = models.CharField(max_length = 255)
  grade = models.CharField(max_length = 255)
  faculity = models.CharField(max_length = 255)
