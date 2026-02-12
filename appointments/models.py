from django.db import models
from patients.models import Patient
from accounts.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='En attente')

    def __str__(self):
        return f"{self.patient} - {self.date}"
