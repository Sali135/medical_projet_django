from django.db import models
from consultations.models import Consultation

class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    medication = models.TextField()
    instructions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
