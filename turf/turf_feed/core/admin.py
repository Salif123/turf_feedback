from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Stadium)
admin.site.register(Appointment)    
# admin.py



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'feedback_text')
