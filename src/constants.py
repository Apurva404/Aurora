# Defines constants used across the system

from enum import Enum

class BuildingType(Enum):
    SINGLE_STORY = "Single Story"
    DOUBLE_STORY = "Double Story"
    COMMERCIAL = "Commercial"

class Weekday(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
