from django.contrib import admin

from .models import Activity
from .models import Signup


# Register your models here.
admin.site.register(Activity)
admin.site.register(Signup)
