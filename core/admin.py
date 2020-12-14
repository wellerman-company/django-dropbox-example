from django.contrib import admin
from .models import DropboxFile


class DropboxFileAdmin(admin.ModelAdmin):
    model = DropboxFile
    list_display = ['photo']


admin.site.register(DropboxFile, DropboxFileAdmin)