from django.contrib import admin
from .models import Grades,Students

# Register your models here.
#注册
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 3
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加、修改页属性
    #fields = ['ggirlnum',gboynum','gname','gdate','isDelete']
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ]

# 要把这些属性都添加到注册模块中才能使用
#admin.site.register(Grades,GradesAdmin)

# 使用装饰器完成注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    def delete(self):
        if self.isDelete:
            return "是"
        else:
            return "否"
    #设置页面列的名称
    gender.short_description = "性别"

    list_display = ['pk','sname','sage',gender,'scontend','sgrade',delete]
    list_filter = ['sgrade']
    search_fields = ['sname']
    list_per_page = 10
#admin.site.register(Students,StudentsAdmin)
