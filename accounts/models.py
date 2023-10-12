from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,email,password=None):
        if not email:
            raise ValueError('User Must Have An Email Adress')
        
            
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,first_name,email,password):
        user = self.create_user(email=self.normalize_email(email),
                                first_name=first_name,
                                password=password,
                                )
        user.is_active = True
        user.is_superuser = True
        user.is_email_verified = True
        user.is_staff = True
        
        user.save(using=self._db)
        return user
            

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=100,unique=True)
    
    profile_pic = models.ImageField(upload_to='user/profile_pic/',null=True,blank=True)
    
    #required field
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.first_name
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,add_label):
        return True
        