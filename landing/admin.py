from django.contrib import admin
from .models import SiteConfig, Subscriber

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("launch_date", "facebook_link", "instagram_link", "linkedin_link")
    list_editable = ("facebook_link", "instagram_link", "linkedin_link")
    list_display_links = ("launch_date",)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    ordering = ("-subscribed_at",)
