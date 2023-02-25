from buildings import Building
from employees import Employee, CertifiedSolarInstaller, Apprentice, UncertifiedSolarInstaller
from constants import Building_Type, Weekday

from typing import Dict, List

BUILDING_RESOURCE_REQUIREMENT_MAP = {
    Building_Type.SINGLE_STORY : [(CertifiedSolarInstaller, 1)],
    Building_Type.DOUBLE_STORY : [(CertifiedSolarInstaller, 1), (UncertifiedSolarInstaller, 1)],
    Building_Type.COMMERCIAL: [(CertifiedSolarInstaller, 2),(Apprentice, 4), (Employee, 4)],
}


def scheduler(buildings: List[Building], employees: List[Employee])-> Dict:
    work_schedule = {
        Weekday.Monday: {},
        Weekday.Tuesday: {},
        Weekday.Wednesday: {},
        Weekday.Thursday: {},
        Weekday.Friday: {},
    }
    # base case
    if len(buildings) == 0 or len(employees) == 0:
        return work_schedule
    
    for day in Weekday:
        print(day)
        for building in buildings:
            bd_type = building.getType()
            resrc_list = BUILDING_RESOURCE_REQUIREMENT_MAP.get(bd_type)
            # print(resrc_list)
            for resrc in resrc_list:
                # print(resrc[0])
                for employee in employees:
                    emp_availability = employee.getAvailability()
                    if resrc[0] == type(employee) and emp_availability[day]:
                        work_schedule[day] = (building.id, employee.id)
    return work_schedule


if __name__ == "__main__":

    bd1 = Building("01", Building_Type.COMMERCIAL)
    bd2 = Building("02", Building_Type.DOUBLE_STORY)
    bd3 = Building("03", Building_Type.SINGLE_STORY)
    test_buildings = [bd1, bd2, bd3]

    emp1 = CertifiedSolarInstaller("001", 
                                   {"Monday": True, "Tuesday": False, "Wednesday": False,
                                    "Thursday": False,"Friday": True})
    emp2 = CertifiedSolarInstaller("002", 
                                   {"Monday": False, "Tuesday": False, "Wednesday": False,
                                    "Thursday": True,"Friday": True})
    emp3 = UncertifiedSolarInstaller("003", 
                                   {"Monday": False, "Tuesday": False, "Wednesday": False,
                                    "Thursday": False,"Friday": True})
    
    test_employees = [emp1, emp2, emp3]

    print(scheduler(test_buildings, test_employees))
                


    




    

