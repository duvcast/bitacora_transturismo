from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from contratos.models import FixedContract
from services.models import Service


# Create your views here.

@login_required
def index(request):
    contracts = FixedContract.objects.all()
    services = Service.objects.all()
    context = {
        "contracts": contracts,
        'services': services
    }
    return render(request, "dashboard/index.html", context)
