from django.db import models

from django_dropbox_storage.storage import DropboxStorage

DROPBOX_STORAGE = DropboxStorage()


class DropboxFile(models.Model):
    photo = models.ImageField(upload_to='photos', storage=DROPBOX_STORAGE)