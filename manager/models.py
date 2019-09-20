from django.db import models

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
  gas_url = models.CharField(max_length = 255, default="")
  room = models.CharField(max_length = 255, default="")
  datetime = 
  description = models.CharField(max_length = 1000)

  # elementaly_presenters = 
  # secondary_presenters = 


class Attendances(models.Model):
  mtg_id = models.CharField(max_length = 255)
  login_name = models.CharField(max_length = 255)
  attend = models.BooleanField()
