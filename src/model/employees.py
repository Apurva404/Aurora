from constants import Weekday
from typing import Dict


class Employee:

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        self.id = id
        self.availability = availability

    def getAvailability(self) -> Dict[Weekday, bool]:
        # assumes that self's employee availability has been set
        return self.availability


class CertifiedEmployee(Employee):

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)


class UncertifiedEmployee(Employee):

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)


class CertifiedSolarInstaller(CertifiedEmployee):

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)


class PendingCertificationSolarInstaller(UncertifiedEmployee):

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)


class Laborer(UncertifiedEmployee):

    def __init__(self, id: str, availability: Dict[Weekday, bool]) -> None:
        super().__init__(id, availability)
