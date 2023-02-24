from buildings import Building
from employees import Employee
from constants import Weekday, Building_Resource_Requirement_Map

from typing import Dict, List


def scheduler(buildings: List[Building], employees: List[Employee])-> Dict:
    work_schedule = {
        "Monday": {},
        "Tuesday": {},
        "Wednesday": {},
        "Thursday": {},
        "Friday": {},
    }
    # base case
    if len(buildings) == 0 or len(employees) == 0:
        return work_schedule
    
    for day in Weekday:
        for building in buildings:
            type = building.getType()
            resrc_list = Building_Resource_Requirement_Map.get(type)
            for resrc in resrc_list:
                for employee in employees:
                    if resrc[0] == type(employee) and employee.getAvailability[day]:
                        work_schedule[day] = (building.id, employee.id)
    return work_schedule


if __name__ == "__main__":
    pass
                


    




    

