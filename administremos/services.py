import logging
import requests

from .models import Driver, Bus, Symptom, DetectionMode, OperationPlace, ControlVariable

url_root = "https://bitakora-patio.meliusid.app"


def make_login():
    url_login = f"{url_root}/auth/login"
    credentials = {
        "email": "melius@meliusid.com",
        "password": "Melius2020+*&"
    }
    req = requests.request("POST", url=url_login, data=credentials)
    token = req.json()["token"]
    return f"Bearer {token}"


def get_data(query):
    token = make_login()
    url = f"{url_root}/graphql"
    header = {'Authorization': token}
    return requests.request("POST", url=url, headers=header, json={'query': query}).json()


def get_driver():
    query = """query{
        empleadosAdministremos{
            idEmpleado
            nroIdentificacion
            codigo
            nombre
            }
        }"""
    response_driver = get_data(query)
    for drivers in response_driver["data"]["empleadosAdministremos"]:
        driver_model = Driver()
        driver = Driver.objects.filter(id_driver=drivers["idEmpleado"]).exists()
        if driver:
            print(f"driver: {driver['idEmpleado']} already exists")
            continue
        driver_model.id_driver = drivers["idEmpleado"]
        driver_model.name = drivers["nombre"]
        driver_model.code = drivers["codigo"]
        driver_model.nro_identification = drivers["nroIdentificacion"]
        driver_model.save()


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
        bus = Bus.objects.filter(id_active=buses["idActivo"]).exists()
        if bus:
            print(f"Bus: {buses['idActivo']} already exists")
            continue
        bus_model.id_active = buses["idActivo"]
        bus_model.name = buses["nombre"]
        bus_model.code = buses["codigo"]
        bus_model.plate = buses["placa"]
        bus_model.brand = buses["marca"]
        bus_model.model = buses["modelo"]
        bus_model.save()


def get_detection_mode():
    query = """query{
    modosDeteccionAdministremos{
        idModoDeteccion
        nombre
        codigo
        }
    }"""
    response_detection_mode = get_data(query)
    for mdetection in response_detection_mode["data"]["modosDeteccionAdministremos"]:
        model_detection_model = DetectionMode()
        if DetectionMode.objects.filter(id_detection_mode=mdetection["idModoDeteccion"]).exists():
            continue
        model_detection_model.id_detection_mode = mdetection["idModoDeteccion"]
        model_detection_model.name = mdetection["nombre"]
        model_detection_model.code = mdetection["codigo"]
        model_detection_model.save()


def get_symptom():
    query = """query{
    sintomasAdministremos{
        idSintoma
        nombre
        codigo
        }
    }"""
    response_symptom = get_data(query)
    for symptom in response_symptom["data"]["sintomasAdministremos"]:
        symptom_model = Symptom()
        if Symptom.objects.filter(id_symptom=symptom["idSintoma"]).exists():
            continue
        symptom_model.id_symptom = symptom["idSintoma"]
        symptom_model.name = symptom["nombre"]
        symptom_model.code = symptom["codigo"]
        symptom_model.save()


def get_operation_place():
    query = """query{
    lugaresOperacionAdministremos{
        idLugarOperacion
        codigo
        nombre
    }
    }"""
    response_operation_place = get_data(query)
    for operation_place in response_operation_place["data"]["lugaresOperacionAdministremos"]:
        operation_place_model = OperationPlace()
        if OperationPlace.objects.filter(id_operation_place=operation_place["idLugarOperacion"]).exists():
            continue
        operation_place_model.id_operation_place = operation_place["idLugarOperacion"]
        operation_place_model.name = operation_place["nombre"]
        operation_place_model.code = operation_place["codigo"]
        operation_place_model.save()


def get_control_variable():
    query = """query{
    variablesControlAdministremos{
        idVariableControl
        codigo
        nombre
    }
    }"""
    response_control_variable = get_data(query)
    for control_variable in response_control_variable["data"]["variablesControlAdministremos"]:
        control_variable_model = ControlVariable()
        if ControlVariable.objects.filter(id_control_variable=control_variable["idVariableControl"]).exists():
            continue
        control_variable_model.id_control_variable = control_variable["idVariableControl"]
        control_variable_model.name = control_variable["nombre"]
        control_variable_model.code = control_variable["codigo"]
        control_variable_model.save()
