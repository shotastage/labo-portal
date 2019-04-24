from django.db import models

# Create your models here.

def get_next():
    try:
        return Meetings.objects.latest('time').time + 1
    except:
        return 1
 

class Meetings(models.Model):
  time = models.IntegerField(default=get_next)
  mtg_id = models.CharField(max_length = 255)
  active = models.BooleanField(default=True)
