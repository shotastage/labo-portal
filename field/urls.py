from django.urls import path
from .views import ContentListAPIView

urlpatterns = [
    path('fields/', ContentListAPIView.as_view()),
]