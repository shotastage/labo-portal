from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from uuid import uuid4
from manager.models import Meetings
from home.models import Attendances
import qrcode
from django.conf import settings



class ManageView(View):

    @method_decorator(staff_member_required(login_url='/login'))
    def get(self, request):

        data = Meetings.objects.all()

        online_url = "https://" + settings.APPLICATION_URL + "/atdx/?mtg_id="

        if settings.RUNNING_MODE == "devel":
            online_url = "http://localhost:8000/atdx/?mtg_id="

        context = {
            'table_data': data,
            'online_url': online_url,
        }

        return render(request, "htmlfile/manager.html", context)

    @method_decorator(staff_member_required(login_url='/login'))
    def post(self, request):

        return render(request,'htmlfile/manager.html')


class MeetingDisableView(View):
    @method_decorator(staff_member_required)
    def get(self, request):
        
        time = request.GET.get("time")

        mtg = Meetings.objects.get(time=time)

        mtg.active = False

        mtg.save()

        return redirect('/kgl/')




class MeetingEnableView(View):
    @method_decorator(staff_member_required)
    def get(self, request):
        
        time = request.GET.get("time")

        mtg = Meetings.objects.get(time=time)

        mtg.active = True

        mtg.save()

        return redirect('/kgl/')



class AttendacesListView(View):

    @method_decorator(login_required)
    def get(self, request):
        
        mtg_id = request.GET.get("mtg_id")

        mtg = Meetings.objects.get(mtg_id=mtg_id)
        data = Attendances.objects.filter(mtg_id=mtg_id)

        context = {
            'no': mtg.time,
            'list': data,
            'mtg_id': mtg_id
        }

        return render(request,'htmlfile/attendances.html', context)



class PresentationStatusRegisterView(View):
    @method_decorator(login_required)
    def get(self, request):
        
        login = request.GET.get("login")

        mtg_id = request.GET.get("mtg_id")


        atd = Attendances.objects.filter(login=login, mtg_id=mtg_id).first()

        atd.is_presentationed = True

        atd.save()

        return redirect('/kgl/attendances/?mtg_id=' + mtg_id)



class AttendanceDeleteView(View):
    @method_decorator(login_required)
    def get(self, request):
        
        login = request.GET.get("login")

        mtg_id = request.GET.get("mtg_id")

        atd = Attendances.objects.filter(login=login, mtg_id=mtg_id).first()
        atd.attend = False
        atd.save()

        return redirect('/kgl/attendances/?mtg_id=' + mtg_id)



class AttendanceReEnableView(View):
    @method_decorator(login_required)
    def get(self, request):
        
        login = request.GET.get("login")

        mtg_id = request.GET.get("mtg_id")

        atd = Attendances.objects.filter(login=login, mtg_id=mtg_id).first()
        atd.attend = True
        atd.save()

        return redirect('/kgl/attendances/?mtg_id=' + mtg_id)



class QRShowView(View):

    @method_decorator(login_required)
    def get(self, request):

        mtg_id = request.GET.get("mtg_id")

        url = "https://" + settings.APPLICATION_URL + "/atd/?mtg_id=" + mtg_id

        if settings.RUNNING_MODE == "devel":
            url = "http://localhost:8000/atd/?mtg_id=" + mtg_id

        img=qrcode.make(url)
        img.save('frontend/generates/qrcode_' + mtg_id + '.png')

        context = {
            'qr_image': 'qrcode_' + mtg_id + '.png',
            'url': url,
            'is_debug': settings.DEBUG
        }

        return render(request,'htmlfile/qrcode.html', context)
