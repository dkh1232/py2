from django.contrib import admin

# Register your models here.
from .models import Grades,Students
admin.site.site_header = '学生班级管理系统'
admin.site.site_title = '我的第一个后台系统'
admin.site.index_title = '欢迎使用'
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_per_page = 5
admin.site.register(Grades,GradesAdmin)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'
    list_display = ['pk', 'sname', 'sage', gender,
                    'scontend', 'sgrade', 'isDelete']
    list_per_page = 10
# admin.site.register(Students,StudentsAdmin)


