from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from . import forms



class SignUp(generic.CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy("login")
	template_name = 'accounts/signup.html'