from typing import Dict, Any

from Main.Parser.Objects.Object import Object
from Main.Parser.Objects.Implements.Public import Public
from Main.Parser.Objects.Implements.Socials import Socials
from Main.Parser.Objects.Implements.Contacts import Contacts
from Main.Parser.Objects.Implements.Personal import Personal
from Main.Parser.Objects.Implements.Influence import Influence


class Candidate(Object):
    def __init__(self,
                 name: str,
                 mark: str,
                 public: Public,
                 socials: Socials,
                 personal: Personal,
                 contacts: Contacts,
                 influence: Influence):

        super().__init__()

        self.name = name
        self.mark = mark

        self.public = public
        self.influence = influence

        self.socials = socials
        self.personal = personal
        self.contacts = contacts

    def getObject(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'mark': self.mark,
            'Public': self.public,
            'Influence': self.influence,
            'Socials': self.socials,
            'Personal': self.personal,
            'Contacts': self.contacts
        }
