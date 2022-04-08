from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from users.forms import ManagerForm
from users.models import Manager


@login_required()
def index_managers(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = ManagerForm()

    managers = Manager.objects.all()
    context = {
        'managers': managers,
        'form': form,
    }
    return render(request, 'users/index_managers.html', context)


class ManagerUpdateView(UpdateView):
    model = Manager
    form_class = ManagerForm
    success_url = reverse_lazy('users:index_managers')
    template_name = 'users/update_manager.html'


class ManagerDeleteView(DeleteView):
    model = Manager
    success_url = reverse_lazy('users:index_managers')
    template_name = 'users/delete_manager.html'
