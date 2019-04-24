from django.urls import path
from home.views import (
    HomeView,
    AttendanceView
)

urlpatterns = (
    path('', HomeView.as_view()),
    path('atd/', AttendanceView.as_view()),
)
