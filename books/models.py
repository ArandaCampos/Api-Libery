from django.db import models
import uuid
  
# Create your models here.
class booksModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    pages = models.IntegerField(null=False, blank=False)
    publisher = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return "{} ({})".format(self.title, self.author)
