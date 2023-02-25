from constants import BuildingType


class Building:

    def __init__(self, id: str, type: BuildingType) -> None:
        self.id = id
        self.type = type

    def get_building_type(self) -> BuildingType:
        # assumes that self's building type has been set
        return self.type

    def set_building_type(self, type: BuildingType) -> None:
        self.type = type
