from django.db import models
from django.conf import settings


class Media(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=200)
    description = models.TextField(verbose_name="Description", default="Aucune description renseignée")
    content = models.FileField(upload_to="")

    def __str__(self):
    	return self.title