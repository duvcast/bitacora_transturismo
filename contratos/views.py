from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from contratos.forms import FixedContractForm, FixedContractEditForm
from contratos.models import FixedContract, Spreadsheet
from services.forms import ServiceForm
from services.models import Service


@login_required
def index_contracts_fixed(request):
    if request.method == 'POST':
        form = FixedContractForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = FixedContractForm()
    contracts = FixedContract.objects.all().order_by('-created_at')
    context = {
        "contracts": contracts,
        'form': form,
    }
    return render(request, 'contratos/index_contract_fixed.html', context)


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
def spreadsheet(request, pk):
    spreadsheets = get_object_or_404(Spreadsheet, pk=pk)
    contracts = FixedContract.objects.filter(spreadsheets=spreadsheets.id)
    context = {
        'spreadsheets': spreadsheets,
        'contracts': contracts,
    }
    return render(request, 'contratos/spreadsheet.html', context)


class ContractUpdateView(UpdateView):
    model = FixedContract
    form_class = FixedContractEditForm
    success_url = reverse_lazy('contracts:index_contract_fixed')
    template_name = 'contratos/update_contract.html'


class ContractDeleteView(DeleteView):
    model = FixedContract
    success_url = reverse_lazy('contracts:index')
    template_name = 'contratos/delete_contract.html'
