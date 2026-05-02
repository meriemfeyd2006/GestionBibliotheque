from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.nom