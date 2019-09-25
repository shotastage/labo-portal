from django.urls import path
from home.views import (
    HomeView,
    AttendanceView,
    DriveView
)

urlpatterns = (
    path('', HomeView.as_view()),
    path('atd/', AttendanceView.as_view()),
    path('drive/', DriveView.as_view()),
)
