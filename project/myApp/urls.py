from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index),
    path('grades/',views.grades),
    path('students/',views.students),
    re_path(r'^grades/(\d+)',views.GradeStudents),
    path('addstudent/',views.addstudent),
    re_path(r'^stu/(\d+)$',views.stupage),
    re_path(r'^(\d+)$',views.detail),
    path('delete/',views.deletestu),
    # path('addstudent/',views.add_student),
    # path('addstudent/addstudenttodatabase/',views.ok)
]
