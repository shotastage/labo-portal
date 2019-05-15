from django.db import models

# Create your models here.

def get_next():
    try:
        return News.objects.latest('priority').priority + 1
    except:
        return 1
 



class Content(models.Model):
  title = models.CharField(max_length = 30)
  text = models.TextField()
  content_type = models.CharField(max_length = 30)
  created_by = models.CharField(max_length = 50)
  is_deleted = models.BooleanField()
  is_updated = models.BooleanField()
  priority = models.IntegerField(default=get_next)
  is_warning = models.BooleanField(default=False)
  is_highlight = models.BooleanField(default=False)


  def get_message_as_markdown(self):
    return mark_safe(markdown(self.content, safe_mode='escape'))

