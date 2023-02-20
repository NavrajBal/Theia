from django.test import TestCase
from django.contrib.auth import get_user_model
from dashboard.models import Patient


# Create your tests here.
class PatientTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="'test_user@gmail.com",
            firstname="test",
            lastname="user",
            password="testuser123"
        )

        self.patient = Patient.objects.create(
            doctor=self.user,
            firstname='Billy',
            lastname='Bob',
            category="glaucoma",
        )

    def test_model_str(self):
        self.assertEqual(str(self.patient.firstname), "Billy")

    def test_patient(self):
        self.assertEqual(f'{self.patient.firstname}', 'Billy')
        self.assertEqual(f'{self.patient.lastname}', 'Bob')
        self.assertEqual(f'{self.patient.category}', 'glaucoma')


