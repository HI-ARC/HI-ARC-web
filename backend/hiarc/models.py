from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django_paranoid.models import ParanoidModel
from django.db import models

class UserManager(BaseUserManager):    
    use_in_migrations = True    
    
    def create_user(self, email, name, password=None, **extra_fields):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            name = name,
            **extra_fields      
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            name = name,
            password = password             
        )
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user

class User(AbstractUser, PermissionsMixin, ParanoidModel):
    objects = UserManager()
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'

    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )
    name = models.CharField(
        max_length=20,
        null=False
    )
    student_id = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    attending_status = models.CharField(max_length=30, default="재학 중")
    semester = models.CharField(max_length=30, blank=True, null=True)
    boj_id = models.CharField(max_length=30)
    codeforces_id = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Fee(ParanoidModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=30)
    paid = models.BooleanField(default=False)
    exemption = models.BooleanField(default=False)
