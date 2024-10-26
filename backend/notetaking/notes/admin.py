from django.contrib import admin
from .models import Memo

# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display="title","message"

admin.site.register(Memo,MemoAdmin)