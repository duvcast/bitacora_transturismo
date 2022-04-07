from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse

from contratos.models import FixedContract
from services.forms import ServiceForm
from services.models import Service


def index(request):
    contracts = FixedContract.objects.all()
    services = Service.objects.all()
    context = {
        "contracts": contracts,
        'services': services
    }
    return render(request, "dashboard/index.html", context)
