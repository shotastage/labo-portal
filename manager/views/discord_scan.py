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
from datetime import datetime



import requests, json


