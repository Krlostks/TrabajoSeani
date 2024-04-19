from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'career', 'stage', 'score', 'created', 'updated']
    list_filter = ['career', 'stage']
