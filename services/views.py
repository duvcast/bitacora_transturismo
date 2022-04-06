from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from services.forms import ServiceForm, ScheduleForm
from services.models import Service, Schedule


@login_required
def index(request):
    # TODO: corregir, asociar un contrato con este servicio, hay que modificar el formulation
    if request.is_ajax and request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = ServiceForm()
    # TODO: filed number_contrast does not exist in the contract model
    services = Service.objects.all().order_by('-created_at')
    context = {
        "services": services,
        'form': form
    }
    return render(request, 'services/index.html', context)


@login_required
def detail_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.service = service
            new_form.save()
            print(f"variable new form {new_form}")
            return HttpResponse('ok')
    else:
        form = ScheduleForm()
    horarios = Schedule.objects.filter(service_id=service.id).order_by('-created_at')
    context = {
        'service': service,
        'horarios': horarios,
        'form': form,
    }
    return render(request, "services/details_service.html", context)


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('services:index')
    template_name = 'services/delete_services.html'
