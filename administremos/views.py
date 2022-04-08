from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Bus, Driver
from .forms import BusDriverForm
from .services import get_driver, get_symptom, get_detection_mode, get_buses


@login_required
def bus(request):
    # if request.method == "POST":
    #     form = BusDriverForm(request.POST)
    #     new_form = form.save(commit=False)
    get_symptom()
    get_buses()
    get_driver()
    get_detection_mode()
    buses = Bus.objects.all()
    context = {
        'buses': buses,
    }
    return render(request, 'administremos/buses.html', context)


@login_required
def driver(request):
    drivers = Driver.objects.all()
    context = {
        'empleados': drivers,
    }
    return render(request, 'administremos/empleados.html', context)
