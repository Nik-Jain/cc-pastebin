from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class PasteBin(models.Model):
    class ExpirationChoices(models.TextChoices):
        never = "NO", "Never"
        burn = "BU", "Burst after read"
        minute_10 =  "10M", "10 Minutes"
        hour_1 = "1H", "1 Hour"
        day_1 = "1D", "1 Day"
        week_1 = "1W", "1 Week"
        week_2 = "2W", "2 Week"
        month_1 = "1M", "1 Month"
        month_6 = "6M", "6 Month"
        year_1 = "1Y", "1 Year"
    
    class PasteExposureChoices(models.TextChoices):
        public = 'public', 'Public'
        unlisted = 'unlisted', 'Unlisted'
    
    title = models.CharField(max_length=60, blank=True)
    hash_code = models.CharField(max_length=8)
    input_text = models.TextField(blank=False)
    paste_expiration = models.CharField(
        max_length=3,
        choices=ExpirationChoices.choices,
        default=ExpirationChoices.never
        )
    paste_exposure = models.CharField(
        max_length=8,
        choices=PasteExposureChoices.choices,
        default=PasteExposureChoices.public
    )
    hit_count = models.IntegerField(default=0)
    is_password_protected  = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=60,blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(default=datetime.now() + timedelta(days=36500))

    class Meta:
        managed=True
