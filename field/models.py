from django.db import models

# Create your models here.


class Content(models.Model):
  title = models.CharField(max_length = 30)
  text = models.TextField()
  content_type = models.CharField(max_length = 30)
  created_by = models.CharField(max_length = 50)
  is_deleted = models.BooleanField()
  is_updated = models.BooleanField()
