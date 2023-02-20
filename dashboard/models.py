from django.urls import reverse
from django.conf import settings
from django.db import models
import uuid


# fetching current user model from settings
User = settings.AUTH_USER_MODEL


# Database model for patient
class Patient(models.Model):

    # Converting default id to use UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100000)
    lastname = models.CharField(max_length=100000)
    category = models.CharField(max_length=100000)
    ocular_image = models.ImageField(null=True, blank=True, upload_to="xrays/")
    note = models.TextField(null=True, blank=True)
    prediction = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])
