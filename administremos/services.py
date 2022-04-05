import logging
import requests

from .models import Empleado, Bus, Sintomas, ModosDeteccion, LugaresOperacion, VariablesControl

url_root = "https://bitakora-patio.meliusid.app/"


def make_login():
    url_login = f"{url_root}auth/login"
    credentials = {
        "email": "melius@meliusid.com",
        "password": "Melius2020+*&"
    }
    req = requests.request("POST", url=url_login, data=credentials)
    token = req.json()["token"]
    return f"Bearer {token}"


def get_data(query):
    token = make_login()
    url = f"{url_root}graphql"
    header = {'Authorization': token}
    return requests.request("POST", url=url, headers=header, json={'query': query}).json()


def get_empleado():
    query = """query{
        empleadosAdministremos{
            idEmpleado
            nroIdentificacion
            codigo
            nombre
            }
        }"""
    response_empleado = get_data(query)
    for empleados in response_empleado["data"]["empleadosAdministremos"]:
        empleado_model = Empleado()
        empleado = Empleado.objects.filter(id_empleado=empleados["idEmpleado"]).exists()
        if empleado:
            print(f"el registro de empleado: {empleados['idEmpleado']} existe")
            continue
        empleado_model.id_empleado = empleados["idEmpleado"]
        empleado_model.nombre = empleados["nombre"]
        empleado_model.codigo = empleados["codigo"]
        empleado_model.nro_identificacion = empleados["nroIdentificacion"]
        empleado_model.save()


def get_buses():
    query = """query{
                busesAdministremos{
                idActivo
                nombre
                codigo
                placa
                marca
                modelo
                }
            }"""
    response_bus = get_data(query)
    for buses in response_bus["data"]["busesAdministremos"]:
        bus_model = Bus()
        bus = Bus.objects.filter(id_activo=buses["idActivo"]).exists()
        if bus:
            print(f"el registro de bus: {buses['idActivo']} existe")
            continue
        bus_model.id_activo = buses["idActivo"]
        bus_model.nombre = buses["nombre"]
        bus_model.codigo = buses["codigo"]
        bus_model.placa = buses["placa"]
        bus_model.marca = buses["marca"]
        bus_model.modelo = buses["modelo"]
        bus_model.save()


def get_modo_deteccion():
    query = """query{
    modosDeteccionAdministremos{
        idModoDeteccion
        nombre
        codigo
        }
    }"""
    response_modo_deteccion = get_data(query)
    for mdeteccion in response_modo_deteccion["data"]["modosDeteccionAdministremos"]:
        modo_deteccion_model = ModosDeteccion()
        if ModosDeteccion.objects.filter(id_modo_deteccion=mdeteccion["idModoDeteccion"]).exists():
            continue
        modo_deteccion_model.id_modo_deteccion = mdeteccion["idModoDeteccion"]
        modo_deteccion_model.nombre = mdeteccion["nombre"]
        modo_deteccion_model.codigo = mdeteccion["codigo"]
        modo_deteccion_model.save()


def get_sintomas():
    query = """query{
    sintomasAdministremos{
        idSintoma
        nombre
        codigo
        }
    }"""
    response_sintoma = get_data(query)
    for sintoma in response_sintoma["data"]["sintomasAdministremos"]:
        sintomas_model = Sintomas()
        if Sintomas.objects.filter(id_sintoma=sintoma["idSintoma"]).exists():
            continue
        sintomas_model.id_sintoma = sintoma["idSintoma"]
        sintomas_model.nombre = sintoma["nombre"]
        sintomas_model.codigo = sintoma["codigo"]
        sintomas_model.save()


def get_lugares_operacion():
    query = """query{
    lugaresOperacionAdministremos{
        idLugarOperacion
        codigo
        nombre
    }
    }"""
    response_lugar_operacion = get_data(query)
    for lugar_operacion in response_lugar_operacion["data"]["lugaresOperacionAdministremos"]:
        lugares_operacion_model = LugaresOperacion()
        if LugaresOperacion.objects.filter(id_lugar_operacion=lugar_operacion["idLugarOperacion"]).exists():
            continue
        lugares_operacion_model.id_lugar_operacion = lugar_operacion["idLugarOperacion"]
        lugares_operacion_model.nombre = lugar_operacion["nombre"]
        lugares_operacion_model.codigo = lugar_operacion["codigo"]
        lugares_operacion_model.save()


def get_variable_control():
    query = """query{
    variablesControlAdministremos{
        idVariableControl
        codigo
        nombre
    }
    }"""
    response_variable_control = get_data(query)
    for variable_control in response_variable_control["data"]["variablesControlAdministremos"]:
        variable_control_model = VariablesControl()
        if VariablesControl.objects.filter(id_variable_control=variable_control["idVariableControl"]).exists():
            continue
        variable_control_model.id_variable_control = variable_control["idVariableControl"]
        variable_control_model.nombre = variable_control["nombre"]
        variable_control_model.codigo = variable_control["codigo"]
        variable_control_model.save()
