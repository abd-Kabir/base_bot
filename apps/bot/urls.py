from django.urls import path

from apps.bot.views import BotWebhook

app_name = 'bot'
urlpatterns = [
    path('bot/webhook/', BotWebhook.as_view())
]
