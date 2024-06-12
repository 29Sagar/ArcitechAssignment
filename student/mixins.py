from django.db import models

class BasicTimeStamp(models.Model):
    created_by = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True