import datetime

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .models import Employee


def index_view(request: WSGIRequest):
    employee = Employee.objects.filter(user_id=request.user.pk)
    return render(request, "sapp_hr/index.html", {"employee": employee})

def mark_register_view(request: WSGIRequest):
    return render(request, "sapp_hr/mark_register.html")

def attendance_register_view(request: WSGIRequest):
    return render(request, "sapp_hr/attendance_register.html", dict(start_date = datetime.date.today() - datetime.timedelta(days=7)))

