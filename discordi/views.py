from django.shortcuts import render
from django.views.generic import View
from home.models import Attendances
import os
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



class APISubmitView(View):

    def post(self, request):
        body = request.body.decode('utf-8')

        atd = Attendances(
            login = str(body),
            mtg_id = "4639b69f-f84e-4cba-90a2-24c0c6bee98e",
            bw_id = "",
            ip_address = "",
            attend = True,
            description = "Bot出席",
        )

        atd.save()

        return HttpResponse("Successful created new api doc!", status=201)


    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(APISubmitView, self).dispatch(*args, **kwargs)

