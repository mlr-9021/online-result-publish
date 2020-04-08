
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
#from import_export.admin import ImportExportModelAdmin


#
# admin.site.register(StudentSemesterProfile)
# class DetailInfoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'roll', 'semester','gpa')
#
# admin.ste.register(Result, DetailInfoAdmin)
#
# # class ViewAdmin(ImportExportModelAdmin):
# #    pass
#
# class DetailInfoAdmin(admin.ModelAdmin):
#      list_display = ('id', 'roll', 'semester','gpa')


@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):

    list_display = ('roll','gpa','semester', 'session')
    # list_display = ("name", "category", "origin")
    # actions = ["export_as_csv"]