from django.http import HttpResponse


from .services import get_empleado, get_lugares_operacion, get_modo_deteccion, get_sintomas, get_variable_control, get_buses


def index(request):
    get_empleado()
    get_buses()
    get_lugares_operacion()
    get_sintomas()
    get_variable_control()
    get_modo_deteccion()
    return HttpResponse("Hola")
