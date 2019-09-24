from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from manager.models import Meetings
from home.models import Attendances

import math

class MyPageView(View):

    @method_decorator(login_required)
    def get(self, request):


        mtg_count = len(Meetings.objects.filter(active=False))

        user_attend = len(Attendances.objects.filter(login=request.user, attend=True))


        try:
            ratio = user_attend / mtg_count * 100

            if mtg_count < user_attend:
                ratio = 100
        except ZeroDivisionError:
            ratio = 0

            if mtg_count < user_attend:
                ratio = 100


        context = {
            'app_name': settings.APPLICATION_NAME,
            'attend_ratio': math.floor(ratio),
            'user_attend_count': user_attend,
            'mtg_count': mtg_count,
        }

        return render(request,'mypage/mypage.html', context)
