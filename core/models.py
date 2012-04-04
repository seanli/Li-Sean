from django.db import models
from django.contrib.auth.models import User


class WebFile(models.Model):

    name = models.CharField(max_length=255)
    item = models.FileField(upload_to='webfiles', max_length=255)
    uploader = models.ForeignKey(User, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'ls_webfile'
        verbose_name = 'web file'
        verbose_name_plural = 'web files'
