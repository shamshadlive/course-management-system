from django.db import models
from django_summernote.fields import SummernoteTextField
from accounts.models import User
# Create your models here.

class ShortTermCourse(models.Model):
    COURSE_STATUS_CHOICES =(
        ("EB", "Enable"),
        ("DB", "Disable"),
        
        )
    
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    course_img = models.ImageField(upload_to='course/main_img/',null=True,blank=True)
    amount = models.IntegerField()
    amount_in_text = models.CharField(max_length=200)
    course_status= models.CharField(choices = COURSE_STATUS_CHOICES,max_length=10 ,default='DB')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def course_name(self):
        return f'{self.title}'