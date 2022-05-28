from django.urls import path
from .views import *

app_name = "home"


urlpatterns = [
    path('', home, name="home"),
    path('students/', generate_student_data, name="student_data"),
]
