from django.urls import path
from manager.views import (
    ManageView,
    MeetingCreateView,
    MeetingDisableView,
    QRShowView,
    AttendacesListView,
    PresentationStatusRegisterView,
    AttendanceDeleteView,
    AttendanceReEnableView
)

urlpatterns = (
    path('', ManageView.as_view()),
    path('create/', MeetingCreateView.as_view()),
    path('disable/', MeetingDisableView.as_view()),
    path('attendances/', AttendacesListView.as_view()),
    path('show_qr/', QRShowView.as_view()),
    path('record_presentation_status/', PresentationStatusRegisterView.as_view()),
    path('attendance_delete/', AttendanceDeleteView.as_view()),
    path('attendance_enable/', AttendanceReEnableView.as_view())
)
