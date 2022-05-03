from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import BusDriverForm, DriverReliefForm, NoveltyForm, BusReliefForm
from .models import Bus, Driver, Novelty, ReliefDriver, ReliefBus
from .services import get_buses


class BusView(TemplateView):
    model = Bus
    template_name = 'administremos/buses/buses.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print(request.POST)
            if action == 'list':
                data = []
                for i in Bus.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'edit':
                bus = Bus.objects.get(pk=request.POST['id'])
                form = BusDriverForm(request.POST, instance=bus)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                novelty = Bus.objects.get(pk=request.POST['id'])
                novelty.driver = None
                novelty.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Asociasion'
        context['form'] = BusDriverForm
        return context


class ReliefBusView(TemplateView):
    model = ReliefBus
    template_name = 'administremos/buses/relief_bus.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in ReliefBus.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = BusReliefForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                bus_relief = ReliefBus.objects.get(pk=request.POST['id'])
                form = BusReliefForm(request.POST, instance=bus_relief)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                bus_relief = ReliefBus.objects.get(pk=request.POST['id'])
                bus_relief.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Relevo'
        context['form'] = BusReliefForm
        return context


class DriversView(TemplateView):
    model = ReliefDriver
    template_name = 'administremos/drivers/drivers.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in Driver.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = DriverReliefForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                bus_relief = ReliefBus.objects.get(pk=request.POST['id'])
                form = BusReliefForm(request.POST, instance=bus_relief)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                bus_relief = ReliefBus.objects.get(pk=request.POST['id'])
                bus_relief.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Relevo'
        context['form'] = DriverReliefForm
        return context


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


@login_required()
def driver(request):
    get_buses()
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers,
    }
    return render(request, 'administremos/drivers/drivers.html', context)


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
    return render(request, 'administremos/drivers/relief_driver.html', context)


class NoveltyView(TemplateView):
    model = Novelty
    template_name = 'administremos/novelty/novelty.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in Novelty.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = NoveltyForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                novelty = Novelty.objects.get(pk=request.POST['id'])
                form = NoveltyForm(request.POST, instance=novelty)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                novelty = Novelty.objects.get(pk=request.POST['id'])
                novelty.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_novelty_url'] = reverse_lazy('administremos:create_novelty')
        context['title_card'] = 'Listado Novedades'
        context['btn_action'] = 'Crear Novedad'
        context['form'] = NoveltyForm()
        return context
