from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students
from myApp import models
# Create your views here.

def index(request):
    return HttpResponse('hello world')


# 数据库查询操作
def grades(request):
    GradesList = Grades.objects.all()
    return render(request,'myApp/grades.html',{'grades':GradesList})

def students(request):
    StudentsList = Students.objects.filter(sage=20)
    return render(request,'myApp/students.html',{'students':StudentsList})

def GradeStudents(request,num):
    grades = Grades.objects.get(pk = num)#获取班级对象
    studentslist = grades.students_set.all()#获得班级学生对象
    return render(request,'myApp/students.html',{'students':studentslist})

# 添加学生
def addstudent(request):
    grade = Grades.objects.get(pk = 1)
    # stu = Students.creatStudent("刘德华", 59, True, "wo jiao liudehua",grade)
    models.Students.objects.create(sname="吴彦祖",sage=30,sgender= True,scontend="wo shi wu yanzu",sgrade=grade)
    # stu.save()
    return HttpResponse('ok')

#删除学生
def deletestu(request):
    stu = models.Students.objects.get(id=5)
    stu.delete()
    return HttpResponse('delete successful')

def stupage(request, page):
    page = int(page)
    studentslist = Students.objects.all()[(page-1)*2:page *2]
    return render(request, 'myApp/students.html', {"students": studentslist})

def detail(request,num):
    return HttpResponse("detail-%s"%num)

