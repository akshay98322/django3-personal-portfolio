from django.contrib import admin
from .models import Blogs


#whatever should be displayed in Admin page UI need to configure here
admin.site.register(Blogs)
