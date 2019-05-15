from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Content
from .serializers import ContentSerializer


class ContentListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()


class ContentCreateView(generics.CreateAPIView):
    ermission_classes = (AllowAny,)
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
