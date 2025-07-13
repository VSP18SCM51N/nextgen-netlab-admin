from django.db import models

class LabCase(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
