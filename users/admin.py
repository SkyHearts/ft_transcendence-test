from django.contrib import admin

# Register your models here.
from users.models import Profile

# Register model created and register to be seen in admin dashboard
admin.site.register(Profile)