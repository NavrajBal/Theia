from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from dashboard.models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin


# TODO: Implement search feature
# Create your views here.
class DashboardView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = "patients"
    template_name = "dashboard/dashboard.html"

    # Fetching data only authenticated user owns
    def get_queryset(self):
        user = self.request.user
        return Patient.objects.filter(doctor=user)


class CreatePatientView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['firstname', 'lastname', 'ocular_image', 'category', 'note']
    template_name = "dashboard/create_patient.html"
    success_url = reverse_lazy('dashboard')

    # Overriding method to set the doctor to the authenticated user
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = "patient"
    template_name = "dashboard/patient_detail.html"


# View to update patient details
class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['firstname', 'lastname', 'ocular_image', 'note']
    template_name = "dashboard/patient_update.html"


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "dashboard/patient_confirm_delete.html"

    success_url = reverse_lazy("dashboard")
