from django.db import models

class Feedback(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    avis = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.date}"