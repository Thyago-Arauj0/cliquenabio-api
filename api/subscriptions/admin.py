from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ('user', 'plan',
        'active', 'created_at', 'updated_at')
    
    list_filter = ('plan', 'active')