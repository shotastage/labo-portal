from django.urls import path
from enrollment.views import Enrollment

urlpatterns = [
    path('enrollment/', Enrollment.as_view(), name='starts'),
]
