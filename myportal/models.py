from django.db import models

# Create your models here.


class RegisteredBrowser(models.Model):
  bwid = models.CharField(max_length = 255)
