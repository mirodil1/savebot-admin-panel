from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import ApiCalls, TelegramUsers, Channels

class ChannelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'language', 'created_at']
    list_editable = ['username', 'language']


class TelegramUsersAdmin(ImportExportModelAdmin):
    list_display = ['id', 'telegram_id', 'full_name', 'username', 'is_premium', 'credits', 'joined_date']
    list_filter = ['is_premium', 'credits', 'joined_date']


class ApiCallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    list_filter = ['name', 'status', 'created_at']

admin.site.register(Channels, ChannelsAdmin)
admin.site.register(TelegramUsers, TelegramUsersAdmin)
admin.site.register(ApiCalls, ApiCallsAdmin)