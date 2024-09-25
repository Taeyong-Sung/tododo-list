from django.contrib import admin
# import your models here
from .models import Todo

# Register your models here
admin.site.register(Todo)