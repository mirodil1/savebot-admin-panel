from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import ApiCalls, InviteLink, TelegramUsers, Channels

class ChannelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'invite_link', 'status', 'language', 'created_at']
    list_editable = ['username', 'language', 'invite_link', 'status']


class TelegramUsersAdmin(ImportExportModelAdmin):
    list_display = ['id', 'telegram_id', 'full_name', 'username', 'is_premium', 'credits', 'joined_date']
    list_filter = ['is_premium', 'credits', 'joined_date']


class ApiCallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    list_filter = ['name', 'status', 'created_at']


class InviteLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['name', 'created_at']


admin.site.register(Channels, ChannelsAdmin)
admin.site.register(TelegramUsers, TelegramUsersAdmin)
admin.site.register(ApiCalls, ApiCallsAdmin)
admin.site.register(InviteLink, InviteLinkAdmin)