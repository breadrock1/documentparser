from typing import List, Dict, Any

from Main.Parser.Objects.Object import Object


class Public(Object):
    def __init__(self,
                 founder: List[str],
                 director: List[str]):

        super().__init__()

        self.founder = founder
        self.director = director

    def getObject(self) -> Dict[str, Any]:
        return {
            'founder': self.founder,
            'director': self.director
        }
