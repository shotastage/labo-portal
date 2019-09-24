from django.urls import path
from mypage.views import MyPageView

urlpatterns = [
    path('mypage/', MyPageView.as_view(), name='starts'),
]
