from django.db import models

# Create your models here.

class Bin(models.Model):
    hash_code = models.CharField(max_length=8)
    input_text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed=True
