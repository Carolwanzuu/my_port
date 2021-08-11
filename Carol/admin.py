from typing import ChainMap
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Skills)
admin.site.register(Profile)

