from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import BusDriverForm
from .models import Bus, Empleado, BusDriver
from .services import get_empleado, get_lugares_operacion, get_modo_deteccion, get_sintomas, get_variable_control, \
    get_buses


def index(request):
    get_empleado()
    get_buses()
    get_lugares_operacion()
    get_sintomas()
    get_variable_control()
    get_modo_deteccion()
    return HttpResponse("Hola")


@login_required
def bus(request):
    buses = Bus.objects.all()
    context = {
        'buses': buses,
    }
    return render(request, 'administremos/buses.html', context)


@login_required
def empleado(request):
    empleados = Empleado.objects.all()
    context = {
        'empleados': empleados,
    }
    return render(request, 'administremos/empleados.html', context)


@login_required
def bus_driver(request):
    if request.method == "POST":
        form = BusDriverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = BusDriverForm()

    bus_drivers = BusDriver.objects.all()
    context = {
        'bus_drivers': bus_drivers,
        'form': form,
    }
    return render(request, 'administremos/bus_driver.html', context)
