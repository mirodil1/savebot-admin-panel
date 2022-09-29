from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class TelegramUsers(models.Model):
    full_name = models.CharField(max_length = 255, verbose_name="TO'LIQ ISM")
    username = models.CharField(max_length = 255, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True)
    language_code = models.CharField(max_length=10, verbose_name="TIL")
    is_premium = models.BooleanField(default=False, verbose_name='PREMIUM')
    credits = models.IntegerField(default=10, verbose_name="KREDITLAR")
    joined_date = models.DateField(auto_now_add=True, verbose_name="QO'SHILGAN VAQTI")

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = "Telegram obunachilar"
        verbose_name_plural = "Telegram obunachilar"

class Channels(models.Model):
    LANGUAGES = (
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
        ('uk', 'Ukrain'),
        ('ar', 'Arabic'),
    )

    username = models.CharField(max_length = 255)
    language = MultiSelectField(choices=LANGUAGES, max_length=10, verbose_name='TIL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="QO'SHILGAN VAQTI")

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Kanallar"
        verbose_name_plural = "Kanallar"


class ApiCalls(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "API so'rovlar"
        verbose_name_plural = "API so'rovlar"