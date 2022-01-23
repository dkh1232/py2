from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20,verbose_name='班级名称')
    gdate = models.DateTimeField(verbose_name='创建时间')
    ggirlnum = models.IntegerField(verbose_name='女生人数')
    gboynum = models.IntegerField(verbose_name='男生人数')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')
    def __str__(self):
        return self.gname
#     __str__返回对象的描述信息

class Students(models.Model):
    sname = models.CharField(max_length=20,verbose_name='学生名称')
    sgender = models.BooleanField(default=True,verbose_name='性别')
    sage = models.IntegerField(verbose_name='年龄')
    scontend = models.CharField(max_length=20,verbose_name='简介')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE,verbose_name='所属班级')
    def __str__(self):
        return self.sname
    @classmethod
    def creatStudent(cls,name,age,gender,contend,grade,isD = False,):
        stu= cls(sname = name, sage= age, sgender = gender,scontend= contend,sgrade= grade,isDelete =isD,)
        return stu

