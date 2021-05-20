from django.shortcuts import render
from django.views.generic import View
from manager.models import Attendances
import os
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



class APISubmitView(View):

    def post(self, request):
        token = request.META["HTTP_API_TOKEN"]
        body = request.body.decode('utf-8')


        if os.environ['ADMIN_TOKEN'] == token:
            atd = Attendances(
                login=str(body),
                mtg_id="7a450d05-1e49-4f45-a6f0-9eec9159fe01",
                bw_id="",
                ip_address="",
                attend=True
            )

            atd.save()


            new = Attendances.objects.submit_new(
                contents = str(body)
            )
            new.save()


            return HttpResponse("Successful created new api doc!", status=201)
            send_notification(request)
        else:
            return HttpResponse("Access token is wrong!", status=403)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(APISubmitView, self).dispatch(*args, **kwargs)

