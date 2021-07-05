from typing import Dict, Any

from Main.Parser.Objects.Object import Object


class Personal(Object):
    def __init__(self,
                 age: str,
                 city: str,
                 position: str):

        super().__init__()

        self.age = age
        self.city = city
        self.position = position

    def getObject(self) -> Dict[str, Any]:
        return {
            'age': self.age,
            'city': self.city,
            'position': self.position
        }
