from django.urls import path
from . views import *

urlpatterns = [
    path('student',get_student.as_view()),
    path('student/<int:id>',get_student.as_view())

]
