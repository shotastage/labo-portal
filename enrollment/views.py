from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.conf import settings


class Enrollment(View):

    def get(self, request):

        context = {
            'app_name': settings.APPLICATION_NAME,
        }

        return render(request,'enrollment/enrollment.html', context)


    def post(self, request):

        login_name = request.POST['login_name']
        grade = request.POST['grade']
        password = request.POST['password']

        user = User.objects.create_user(login_name, login_name + '@sfc.wide.ad.jp', password)
        user.member.grade = grade
        user.save()        

        return redirect('/')
