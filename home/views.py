from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Attendances
from manager.models import Meetings
from news.models import News
from django.conf import settings



class HomeView(View):

    def get(self, request):

        data = News.objects.all().order_by('priority')

        context = {
            'app_name': settings.APPLICATION_NAME,
            'page_title': "Home",
            'table_data': data,
        }

        return render(request, "orc-view/dist/index.html", context)



class AttendanceView(View):

    def get(self, request):

        mtg_id = request.GET.get("mtg_id")

        attendance_list = Attendances.objects.filter(mtg_id=mtg_id)

        context = {
            'mtg_id': mtg_id,
            'list': attendance_list
        }

        return render(request, "htmlfile/attend.html", context)


    def post(self, request):

        # Get params

        
        login_name = request.POST["dwqd2nj2"]
        bw_id = request.POST["bw_id"]
        mtg_id = request.POST["mtg_id"]

        if mtg_id == "None":
            context = {
                'is_error': True,
                'error_title': "エラー",
                'error_desc': "ミーティングIDを確認できませんでした. もう一度QRコードをスキャンして出席してください."
            }

            return render(request, "htmlfile/result.html", context)
    

        # Get device IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    

        recent_atd = Attendances.objects.filter(mtg_id=mtg_id)

        context = {
            'is_error': False
        }

        mtgs = Meetings.objects.filter(mtg_id=mtg_id)

        if not mtgs[0].active:
            context = {
                'is_error': True,
                'error_title': "エラー",
                'error_desc': "このミーティングの出席はすでに締め切られています."
            }

            return render(request, "htmlfile/result.html", context)

        for atd in recent_atd:

            if atd.bw_id == bw_id:
                context = {
                    'is_error': True,
                    'error_title': "多重送信エラー",
                    'error_desc': "同一の端末から複数の異なる出席情報を提出することはできません."
                }

                return render(request, "htmlfile/result.html", context)


            if atd.login == login_name:
                context = {
                    'is_error': True,
                    'error_title': "出席重複",
                    'error_desc': "すでに出席情報が記録されています."
                }

                return render(request, "htmlfile/result.html", context)

            if settings.RUNNING_MODE == "devel":
                pass
            else:    
                if atd.ip_address == ip:
                    context = {
                        'is_error': True,
                        'error_title': "IP重複エラー",
                        'error_desc': "同じIP(端末)からの出欠登録は１回のみです."
                    }

                    return render(request, "htmlfile/result.html", context)

        # Record DB
        atd = Attendances(
            login=login_name,
            mtg_id=mtg_id,
            bw_id=bw_id,
            ip_address=ip,
            attend=True
        )

        atd.save()

        return render(request, "htmlfile/result.html", context)
