from django import forms
from .models import ShortTermCourse


class ShortTermCourseUpdateForm(forms.ModelForm):
    class Meta:
        model = ShortTermCourse
        exclude = ('user',)
        widgets = {
            
            'course_status': forms.Select(attrs={'class': 'form-control select2'}),
            
        }
    