from django.urls import path
from register.views import Top, Login, Logout


app_name = 'register'

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
