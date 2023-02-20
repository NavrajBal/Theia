from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView

# Create your views here.
class SignupPageView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'