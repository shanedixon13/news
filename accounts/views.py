from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name="index.html"


class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'

