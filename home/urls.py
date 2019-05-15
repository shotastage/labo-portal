from django.urls import path
from home.views import (
    HomeView,
    AttendanceView
)

urlpatterns = (
    path('atd/', AttendanceView.as_view()),
)
