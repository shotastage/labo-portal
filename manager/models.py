from django.db import models
from django.utils import timezone

# Create your models here.

def get_next():
    try:
        return Meetings.objects.latest('time').time + 1
    except:
        return 1
 

class Meetings(models.Model):
  mtg_id = models.CharField(max_length = 255)
  time = models.IntegerField(default=get_next)
  active = models.BooleanField(default=True)

  # 時限
  period = models.IntegerField(default=6)
  due_date = models.DateTimeField(default=timezone.now)
  campus = models.CharField(max_length = 255, default="")
  room = models.CharField(max_length = 255, default="")
  gas_url = models.CharField(max_length = 255, default="")
  elementaly_presenters = models.CharField(max_length = 500, default="")
  secondary_presenters = models.CharField(max_length = 500, default="")
  description = models.CharField(max_length = 1000, default="")



class Attendances(models.Model):
  mtg_id = models.CharField(max_length = 255)
  login_name = models.CharField(max_length = 255)
  attend = models.BooleanField()
