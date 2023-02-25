import json
from typing import Dict, List, Tuple

from constants import BuildingType, Weekday
from model.buildings import Building
from model.employees import Employee, CertifiedSolarInstaller, PendingCertificationSolarInstaller, Laborer

def read_data(filename: str) -> Tuple[List[Building], List[Employee]]:
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    
    building_data = data["buildings"]
    employee_data = data["employees"]

    buildings = []
    for item in building_data:
        building = Building(item["id"], BuildingType(item["type"]))
        buildings.append(building)

    employees = []
    for item in employee_data:
        id = item["id"]
        availability = {}
        for k, v in item["availability"].items():
            availability[Weekday(k)] = v
        
        type = item["type"]
        
        if type == "Certified Solar Installer":
            employee = CertifiedSolarInstaller(id, availability)
        elif type == "Pending Certification Solar Installer":
            employee = PendingCertificationSolarInstaller(id, availability)
        elif type == "Laborer":
            employee = Laborer(id, availability)
        else:
            employee = None
        
        employees.append(employee)

    return data["description"], buildings, employees