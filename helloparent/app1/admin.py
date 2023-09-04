from django.contrib import admin
from .models import Student, academics

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Rollno', 'name', 'fname', 'branch', 'dob', 'gender', 'Mentor')

class AcademicAdmin(admin.ModelAdmin):
    list_display = ('rollno','LADC', 'AP', 'ENG', 'DM', 'VEGC', 'Java', 'DLD', 'BEE', 'DBMS', 'PS', 'CHEM', 'SLL', 'DBMSL', 'JPL', 'LSPD', 'DEVC', 'EWS', 'DS', 'DSL')

admin.site.register(Student, StudentAdmin)
admin.site.register(academics, AcademicAdmin)
