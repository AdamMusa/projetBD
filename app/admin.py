from django.contrib import admin

# Register your models here.
from app.models import School, Study

admin.site.register(School)
admin.site.register(Study)