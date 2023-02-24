from constants import Employee_Type, Weekday
from typing import Dict

class Employee:
    
    def __init__(self, id: str, type: Employee_Type, availability: Dict[Weekday, bool] ) -> None:
        self.id = id
        self.type = type
        self.availability = availability
    
    
    def getType(self) -> Employee_Type:
        # assumes that self's employee type has been set
        return self.type
    
    
    def setType(self, ip_type: Employee_Type) -> None:
        self.type = ip_type

    
    def getAvailability(self) -> Dict[Weekday, bool]:
        # assumes that self's employee availability has been set
        return self.availability
