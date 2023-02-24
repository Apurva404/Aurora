# Defines constants used across the system

from enum import Enum

OUTPUT_SCHEDULE_DURATION = 5

class Building_Type(Enum):
    SINGLE_STORY = 1
    DOUBLE_STORY = 2
    COMMERCIAL = 3

class Employee_Type(Enum):
    CERTIFIED_INSTALLER = 1
    INSTALLER_PENDING_CERTIFICATION = 2
    LABORER = 3

class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

