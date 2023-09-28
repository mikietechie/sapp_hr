from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view),
    path("mark-register/", views.mark_register_view),
    path("attendance-register/", views.attendance_register_view),
]
