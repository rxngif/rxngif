from django.db import models
import uuid

# Create your models here.
class Gif(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    url = models.URLField() # max length is 200 by default

    def __str__(self):
        return "{} - {}".format(self.name,self.url)