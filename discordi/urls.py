from django.urls import path
from discordi.views import APISubmitView

urlpatterns = [
    path('submit_attendance/', APISubmitView.as_view()),
]
