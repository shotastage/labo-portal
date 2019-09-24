from django.db import models


class Attendances(models.Model):
  login = models.CharField(max_length = 255)
  mtg_id = models.CharField(max_length = 255)
  bw_id = models.CharField(max_length = 255, default="NONE")
  ip_address = models.CharField(max_length = 255)
  attend = models.BooleanField(default=True)
  description = models.TextField(max_length = 500, default="No Description")
  is_presentationed = models.BooleanField(default=False)
