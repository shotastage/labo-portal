from django.db import models


class Attendances(models.Model):
  login_name = models.CharField(max_length = 255)
  mtg_id = models.CharField(max_length = 255)
  attend = models.BooleanField()
