from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Level)
admin.site.register(Month)

admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(ExamResult)

# admin.site.register(Parent)
admin.site.register(Teacher)

admin.site.register(FeeRecord)
admin.site.register(SalaryRecord)
admin.site.register(SalaryRate)
