from django.urls import path
from .views import ContentListAPIView, ContentCreateView

urlpatterns = [
    path('fields/', ContentListAPIView.as_view()),
    path('fields/create/', ContentCreateView.as_view()),
]
