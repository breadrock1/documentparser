from typing import Dict, Any

from Main.Parser.Objects.Object import Object


class Contacts(Object):
    def __init__(self,
                 mail: str,
                 phone: str):

        super().__init__()

        self.mail = mail
        self.phone = phone

    def getObject(self) -> Dict[str, Any]:
        return {
            'mail': self.mail,
            'phone': self.phone
        }
