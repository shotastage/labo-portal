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
import qrcode
from django.conf import settings


from datetime import datetime



import requests, json



class MeetingCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request,'manager/create_mtg.html')

    @method_decorator(login_required)
    def post(self, request):
        generated_id = uuid4()

        period = request.POST['period']
        campus = request.POST['campus']
        room = request.POST['room']
        gas_url = request.POST['gas_url']
        elem_presenters = request.POST['elem_presenters']
        second_presenters = request.POST['second_presenters']
        desc = request.POST['desc']

        month = request.POST['month']
        day = request.POST['day']
        hour = request.POST['hour']
        minu = request.POST['minu']



        mtg = Meetings(
            mtg_id= generated_id,
            active = True,
            period = period,
            due_date = datetime(2019, int(month), int(day), int(hour), int(minu)),
            campus = campus,
            room = room,
            gas_url = gas_url,
            elementaly_presenters = elem_presenters,
            secondary_presenters = second_presenters,
            description = desc
        )
        
        mtg.save()


        try:
            is_notify = request.POST['is_notify']
            is_notify = "@channel"
        except:
            is_notify = ""
        
        text = u'{0}\n*🔴  次回MTG連絡*\n>*日時:* {1}時限目 2019/{2}/{3} {4}:{5}~\n>*キャンパス:* {6}  *教室:* {7}\n>*進捗発表:* {8}\n>*LT発表:* {9}\n>*メッセージ:* {10}'.format(
            is_notify, period, month, day, hour, minu, campus, room, elem_presenters, second_presenters, desc)

        try:
            is_slack = request.POST['is_slack']


            WEB_HOOK_URL = settings.SLACK_INCOMING_TOKEN

            requests.post(WEB_HOOK_URL, data = json.dumps({
                'text': text,
                'username': u'{0} Portal System'.format(settings.APPLICATION_NAME),
                'icon_emoji': u':smile_cat:',
                'link_names': 1,
            }))
        except:
            pass


        return redirect('/kgl/')
