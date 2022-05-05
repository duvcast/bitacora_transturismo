from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from administremos.models import Driver, Bus, ReliefBus, ReliefDriver, Novelty
from contratos.forms import FixedContractForm, OccasionalContractForm, USerContractForm
from contratos.models import FixedContract, OccasionalContract, UserContractor
from services.forms import ServiceForm
from services.models import Service, Schedule


class FixedContractView(TemplateView):
    model = FixedContract
    template_name = 'contratos/fixed/fixed_contracts.html'

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
                for i in FixedContract.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = FixedContractForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                fixed_contract = FixedContract.objects.get(pk=request.POST['id'])
                form = FixedContractForm(request.POST, instance=fixed_contract)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                fixed_contract = FixedContract.objects.get(pk=request.POST['id'])
                fixed_contract.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Contrato'
        context['form_fc'] = FixedContractForm
        context['form_uc'] = USerContractForm
        return context


class OccasionalContractView(TemplateView):
    model = OccasionalContract
    template_name = 'contratos/occassionals/occasional_contracts.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in OccasionalContract.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = OccasionalContractForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                occasional_contract = OccasionalContract.objects.get(pk=request.POST['id'])
                form = OccasionalContractForm(request.POST, instance=occasional_contract)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                fixed_contract = OccasionalContract.objects.get(pk=request.POST['id'])
                fixed_contract.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Contrato'
        context['form'] = OccasionalContractForm
        return context


class UserContractsView(TemplateView):
    model = UserContractor
    template_name = 'contratos/users/users.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in UserContractor.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'add':
                form = USerContractForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                users_contracts = UserContractor.objects.get(pk=request.POST['id'])
                form = USerContractForm(request.POST, instance=users_contracts)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                users_contracts = UserContractor.objects.get(pk=request.POST['id'])
                users_contracts.delete()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Usuario'
        context['form'] = USerContractForm
        return context


@login_required
def spreadsheet(request):
    fixed_contracts = FixedContract.objects.all().order_by('-created_by')
    occasional_contracts = OccasionalContract.objects.all().order_by('-created_at')
    services = Service.objects.all().order_by('-created_at')
    schedules = Schedule.objects.all().order_by('-created_at')
    drivers = Driver.objects.all().order_by('-created_at')
    relief_buses = ReliefBus.objects.all().order_by('-created_at')
    relief_drivers = ReliefDriver.objects.all().order_by('-created_at')
    novelties = Novelty.objects.all().order_by('-created_at')
    context = {
        'fixed_contracts': fixed_contracts,
        'occasional_contracts': occasional_contracts,
        'services': services,
        'schedules': schedules,
        'drivers': drivers,
        'relief_buses': relief_buses,
        'relief_drivers': relief_drivers,
        'novelties': novelties,

    }
    return render(request, 'contratos/spreadsheet/spreadsheet.html', context)
