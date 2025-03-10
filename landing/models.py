from django.db import models

class SiteConfig(models.Model):
    launch_date = models.DateTimeField(verbose_name="Launch Date")
    facebook_link = models.URLField(blank=True, null=True, verbose_name="Facebook Page")
    instagram_link = models.URLField(blank=True, null=True, verbose_name="Instagram Profile")
    linkedin_link = models.URLField(blank=True, null=True, verbose_name="LinkedIn Profile")

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configurations"

    def __str__(self):
        return "Site Configuration"

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Subscriber Email")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Subscription Date")

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return self.email
