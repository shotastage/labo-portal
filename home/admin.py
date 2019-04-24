from django.contrib import admin
from .models import Attendances
# Register your models here.

@admin.register(Attendances)
class AttendancesAdmin(admin.ModelAdmin):
  list_display = ('login', 'description')
