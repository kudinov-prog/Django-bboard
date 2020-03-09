from django.contrib import admin

from .models import Bd
from .models import Rubric

class BdAmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bd, BdAmin)
admin.site.register(Rubric)

# Register your models here.
