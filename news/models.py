from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.


def get_next():
    try:
        return News.objects.latest('priority').priority + 1
    except:
        return 1
 

class News(models.Model):
  created_by = models.CharField(max_length = 255)
  created_at = models.DateField()
  title = models.CharField(max_length = 255)
  content = models.TextField(max_length = 10000)
  priority = models.IntegerField(default=get_next)
  is_warning = models.BooleanField(default=False)
  is_highlight = models.BooleanField(default=False)

  def get_message_as_markdown(self):
    return mark_safe(markdown(self.content, safe_mode='escape'))
