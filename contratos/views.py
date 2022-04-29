from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from administremos.models import Driver, Bus, ReliefBus, ReliefDriver, Novelty
from contratos.forms import FixedContractForm, FixedContractEditForm, OccasionalContractForm, USerContractForm
from contratos.models import FixedContract, OccasionalContract, UserContractor
from services.forms import ServiceForm
from services.models import Service


@login_required()
def contracts_fixed_list(request):
    contracts = FixedContract.objects.all().order_by('-created_at')
    context = {
        'contracts': contracts,
    }
    return render(request, 'contratos/fixed_contracts/index_contract_fixed.html', context)


@login_required()
def create_fixed_contract(request):
    if request.method == 'POST':
        form = FixedContractForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return redirect('contracts:contracts_fixed_list')
    else:
        form = FixedContractForm()
    context = {
        'form': form,
    }
    return render(request, 'contratos/fixed_contracts/create_fixed_contract.html', context)


def contract_fixed_delete(request):
    if request.method == 'POST':
        print(request.POST.get('id-contract-fixed', False))
        contract = FixedContract.objects.get(id=request.POST.get('id-contract-fixed', False))
        contract.delete()
        print('eliminado...')
        return HttpResponse('record deleted')


@login_required
def detail_contract_fixed(request, pk):
    contract = get_object_or_404(FixedContract, pk=pk)
    if request.method == "POST":
        form = ServiceForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.contract = contract
            new_form.save()
            return HttpResponse('ok')
    else:
        form = ServiceForm()
    services = Service.objects.filter(contract_id=contract.id).order_by('-created_at')
    context = {
        'contract': contract,
        'services': services,
        'form': form,
    }
    return render(request, "contratos/details_contract_fixed.html", context)


@login_required
def spreadsheet(request):
    contractors_for = UserContractor.objects.filter(type_contractor__iexact='CONTRATISTA')
    contractors_by = UserContractor.objects.filter(type_contractor__iexact='CONTRATANTE')
    fixed_contracts = FixedContract.objects.all().order_by('-created_by')
    print(fixed_contracts)
    occasional_contracts = OccasionalContract.objects.all().order_by('-created_at')
    buses = Bus.objects.all().order_by('-created_at')
    drivers = Driver.objects.all().order_by('-created_at')
    relief_buses = ReliefBus.objects.all().order_by('-created_at')
    relief_drivers = ReliefDriver.objects.all().order_by('-created_at')
    novelties = Novelty.objects.all().order_by('-created_at')
    context = {
        'contractors_for': contractors_for,
        'contractors_by': contractors_by,
        'fixed_contracts': fixed_contracts,
        'occasional_contracts': occasional_contracts,
        'buses': buses,
        'drivers': drivers,
        'relief_buses': relief_buses,
        'relief_drivers': relief_drivers,
        'novelties': novelties,

    }
    return render(request, 'contratos/spreadsheet.html', context)


class ContractFixedUpdateView(UpdateView):
    model = FixedContract
    form_class = FixedContractEditForm
    success_url = reverse_lazy('contracts:index_contract_fixed')
    template_name = 'contratos/update_contract.html'


class ContractDeleteView(DeleteView):
    model = FixedContract
    success_url = reverse_lazy('contracts:contracts_fixed_list')
    template_name = 'contratos/delete_contract.html'


@login_required
def index_contracts_occasional(request):
    print(request.POST)
    if request.method == 'POST':
        form = OccasionalContractForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponse('ok')
    else:
        form = OccasionalContractForm()
    contracts = OccasionalContract.objects.all().order_by('-created_at')
    context = {
        "contracts": contracts,
        'form': form,
    }
    return render(request, 'contratos/index_contract_occasional.html', context)


class ContractOccasionalUpdateView(UpdateView):
    model = OccasionalContract
    form_class = OccasionalContractForm
    success_url = reverse_lazy('contracts:index_contract_occasional')
    template_name = 'contratos/update_contract_occasional.html'


class ContractOccasionalDeleteView(DeleteView):
    model = OccasionalContract
    success_url = reverse_lazy('contracts:index_contract_occasional')
    template_name = 'contratos/delete_contract_occasional.html'


@login_required()
def users_contract(request):
    if request.method == 'POST':
        form = USerContractForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            new_form.save()
            return HttpResponse('ok')
    else:
        form = USerContractForm()
    users_contracts = UserContractor.objects.all()
    context = {
        'users_contacts': users_contracts,
        'form': form,
    }
    return render(request, 'contratos/index_users_contracts.html', context)


class UserContractUpdateView(UpdateView):
    model = UserContractor
    form_class = USerContractForm
    success_url = reverse_lazy('contracts:users_contract')
    template_name = 'contratos/update_users_contract.html'


class UserContractorDeleteView(DeleteView):
    model = UserContractor
    success_url = reverse_lazy('contracts:users_contract')
    template_name = 'contratos/delete_user_contract.html'
