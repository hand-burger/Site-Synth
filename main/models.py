from django.db import models

class DownloadableFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads/')  # This will store the file in the 'downloads' directory inside the 'media' folder.
