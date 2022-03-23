from django.contrib import admin
from .models import FileUpload
# Register your models here.
@admin.register(FileUpload)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','fileurl')
