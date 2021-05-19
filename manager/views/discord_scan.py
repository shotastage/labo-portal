import qrcode
import asyncio
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.utils.decorators import classonlymethod
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from uuid import uuid4
from manager.models import Meetings
from django.conf import settings
from discordapp.voice_mtg_scanner import scan
from datetime import datetime



import requests, json



class DiscordScan(View):

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

        scan()

        return render(request, "htmlfile/discordscan.html", context)
