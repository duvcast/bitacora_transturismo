from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
