from django.db import models


class URL(models.Model):
    short_code = models.CharField(max_length=6, unique=True, primary_key=True)
    original_url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
