from django.urls import path
#from app.views import YOUR_VIEW_CLASSES
from app.views import index_view


urlpatterns = [
    # path('url_letter/', YOUR_VIEW_CLASS.as_view(), name='starts'),
    path('', index_view, name='index'),

]
