from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from administremos.services import get_buses, get_driver
from services.forms import ServiceForm, ScheduleForm
from services.models import Service, Schedule


class ServiceView(TemplateView):
    model = Service
    template_name = 'services/services/services.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'list':
                data = []
                for i in Service.objects.all().order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'list_schedule':
                data = []
                for i in Schedule.objects.filter(service_id=request.POST['id']).order_by('-created_at'):
                    data.append(i.model_to_json())
            elif action == 'edit_schedule':
                schedule = Schedule.objects.get(pk=request.POST['id'])
                form = ScheduleForm(request.POST, instance=schedule)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete_schedule':
                schedule = Schedule.objects.get(pk=request.POST['id'])
                schedule.delete()
            elif action == 'add':
                form = ServiceForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.save()
                else:
                    data['error'] = form.errors
            elif action == 'edit':
                service = Service.objects.get(pk=request.POST['id'])
                form = ServiceForm(request.POST, instance=service)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            elif action == 'delete':
                service = Service.objects.get(pk=request.POST['id'])
                service.delete()
            elif action == 'add_schedule':
                service = Service.objects.get(id=request.POST["id"])
                form = ScheduleForm(request.POST)
                if form.is_valid():
                    new_form = form.save(commit=False)
                    new_form.created_by = request.user
                    new_form.service = service
                    new_form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_action'] = 'Crear Servicio'
        context['form'] = ServiceForm
        context['form_sch'] = ScheduleForm
        return context


@login_required
def detail_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(data=request.POST)
        print(f'EL error del form de schedule es: {form.errors}')
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
