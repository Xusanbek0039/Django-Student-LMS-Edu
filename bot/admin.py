from django.contrib import admin
from .models import *

class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'user', 'datetime']

class PromptAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message']


admin.site.register(ChatHistory, ChatHistoryAdmin)
admin.site.register(ChatHistoryBackup, ChatHistoryAdmin)
admin.site.register(Prompt, PromptAdmin)
