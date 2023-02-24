from constants import Building_Type

class Buildings:
    
    def __init__(self, id: str, type: Building_Type) -> None:
        self.id = id
        self.type = type
    

    def getType(self) -> Building_Type:
        # assumes that self's building type has been set
        return self.type
    
    
    def setType(self, type: Building_Type) -> None:
        self.type = type
