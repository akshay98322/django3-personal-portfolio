from django.contrib import admin

# Register your models here.
from .models import Blogs
# Register your models here.

#whatever should be displayed in Admin page UI need to configure here
admin.site.register(Blogs)
