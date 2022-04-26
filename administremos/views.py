from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BusDriverForm, DriverReliefForm, NoveltyForm, BusReliefForm
from .models import Bus, Driver, Novelty, ReliefDriver, ReliefBus


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
    return render(request, 'administremos/buses/buses.html', context)


@login_required()
def buses_relief(request):
    if request.method == "POST":
        form = BusReliefForm(request.POST)
        print(form)
        if form.is_valid():
            print("Relevo de bus Guardado")
            form.save()
            return redirect('administremos:relief_buses')
    else:
        form = BusReliefForm()
    reliefs = ReliefBus.objects.all()
    context = {
        'reliefs_buses': reliefs,
        'form': form,
    }
    return render(request, 'administremos/buses/relief_bus.html', context)


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


@login_required()
def driver(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers,
    }
    return render(request, 'administremos/drivers.html', context)


@login_required()
def drivers_relief(request):
    if request.method == "POST":
        form = DriverReliefForm(request.POST)
        print(form)
        if form.is_valid():
            print("Relevo Guardado")
            form.save()
            return redirect('administremos:relief_drivers')
    else:
        form = DriverReliefForm()
    reliefs = ReliefDriver.objects.all()
    context = {
        'reliefs': reliefs,
        'form': form,
    }
    return render(request, 'administremos/relief_driver.html', context)


@login_required
def novelties(request):
    novelties_list = Novelty.objects.all()
    context = {
        'novelties': novelties_list,
    }
    return render(request, 'administremos/novelties.html', context)


@login_required()
def create_novelty(request):
    if request.method == "POST":
        form = NoveltyForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return redirect('administremos:novelties')
    else:
        form = NoveltyForm()
    context = {
        'form': form,
    }
    return render(request, 'administremos/create_novelty.html', context)
