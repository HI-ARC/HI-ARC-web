from django.contrib import admin
from django_paranoid.admin import ParanoidAdmin
from .models import *

# Register your models here.
class ModelAdmin(ParanoidAdmin):
    pass

admin.site.register(User, ModelAdmin)
admin.site.register(Fee, ModelAdmin)
