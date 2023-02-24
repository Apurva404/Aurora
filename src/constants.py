# Defines constants used across the system

from enum import Enum
from employees import Employee, CertifiedSolarInstaller, UncertifiedSolarInstaller, Apprentice, Laborer

OUTPUT_SCHEDULE_DURATION = 5

class Building_Type(Enum):
    SINGLE_STORY = 1
    DOUBLE_STORY = 2
    COMMERCIAL = 3

class Certification_Status(Enum):
    COMPLETE = 1
    PENDING = 2
    NA = 3

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

Building_Resource_Requirement_Map = {
    Building_Type.SINGLE_STORY : [(CertifiedSolarInstaller, 1)],
    Building_Type.DOUBLE_STORY : [(CertifiedSolarInstaller, 1), (UncertifiedSolarInstaller, 1)],
    Building_Type.COMMERCIAL: [(CertifiedSolarInstaller, 2),(Apprentice, 4), (Employee, 4) ],
}

