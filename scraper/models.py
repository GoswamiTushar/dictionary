from django.db import models

# Create your models here.

class ScraperDetails(models.Model):
    ip_addr = models.CharField(max_length=15)
    search = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.ip_addr
    
