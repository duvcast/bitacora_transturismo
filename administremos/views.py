from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import BusDriverForm
from .models import Bus, Driver


@login_required
def bus(request):
    if request.method == "POST":
        id_bus = request.POST.get('id', False)
        bus_object = get_object_or_404(Bus, id=id_bus)
        form = BusDriverForm(request.POST, instance=bus_object)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = BusDriverForm()
    buses = Bus.objects.all()
    context = {
        'buses': buses,
        'form': form,
    }
    return render(request, 'administremos/buses.html', context)


@login_required
def remove_bus_driver(request):
    """"
    THis function unassigned a bus and driver
    """
    if request.method == "POST":
        id_bus = request.POST.get("id-bus", False)
        bus = get_object_or_404(Bus, id=id_bus)
        bus.driver = None
        bus.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('Method Not Allowed')


@login_required
def driver(request):
    drivers = Driver.objects.all()
    context = {
        'empleados': drivers,
    }
    return render(request, 'administremos/drivers.html', context)


