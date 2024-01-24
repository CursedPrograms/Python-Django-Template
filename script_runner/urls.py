from django.urls import path
from .views import run_script, show_run_script_form

urlpatterns = [
    path('run_script/<str:script_number>/', run_script, name='run_script'),
    path('show_run_script_form/', show_run_script_form, name='show_run_script_form'),
]