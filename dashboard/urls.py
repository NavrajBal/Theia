from django.urls import path
from . import views

urlpatterns = [
  path("", views.DashboardView.as_view(), name="dashboard"),
  path("create/", views.CreatePatientView.as_view(), name="create_patient"),
  path("<uuid:pk>/", views.PatientDetailView.as_view(), name="patient_detail"),
  path("<uuid:pk>/delete/", views.PatientDeleteView.as_view(), name="patient_delete"),
  path("<uuid:pk>/update/", views.PatientUpdateView.as_view(), name="patient_update")
]