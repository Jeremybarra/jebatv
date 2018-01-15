from django.db import models
from jebatv.models import Media

class Serie(models.Model):
	title = models.CharField(verbose_name="Titre", max_length=200)
	description = models.TextField(verbose_name="Description", default="Aucune description renseignée")
	image = models.FileField(upload_to="", default="placeholder_series.png")

	def __str__(self):
		return self.title

class Season(models.Model):
	name = models.CharField(verbose_name="Nom", max_length=200) 
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Episode(Media):
	season = models.ForeignKey(Season, on_delete=models.CASCADE)
	serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

	def __str__(self):
		return self.title