from django.shortcuts import render
from django.views.generic import View
from manager.models import Attendances
import os
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



class APISubmitView(View):

    def post(self, request):
        body = request.body.decode('utf-8')


        atd = Attendances(
            login_name=str(body),
            mtg_id="7a450d05-1e49-4f45-a6f0-9eec9159fe01",
            attend=True
        )

        atd.save()

        return HttpResponse("Successful created new api doc!", status=201)
    

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(APISubmitView, self).dispatch(*args, **kwargs)

