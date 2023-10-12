from django.contrib import admin
from .models import ShortTermCourse
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ShortTermCourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    
admin.site.register(ShortTermCourse,ShortTermCourseAdmin)