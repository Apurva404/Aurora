from constants import Weekday, Certification_Status
from typing import Dict

class Employee:
    
    def __init__(self, id: str, availability: Dict[Weekday, bool] ) -> None:
        self.id = id
        self.availability = availability
    
    def getAvailability(self) -> Dict[Weekday, bool]:
        # assumes that self's employee availability has been set
        return self.availability


class CertifiedSolarInstaller(Employee):
    
    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)
        self.certification_status = Certification_Status.COMPLETE


class UncertifiedSolarInstaller(Employee):
    
    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)


class Apprentice(UncertifiedSolarInstaller):
    
    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)
        self.certification_status = Certification_Status.PENDING


class Laborer(UncertifiedSolarInstaller):
    
    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)
        self.certification_status = Certification_Status.NA
