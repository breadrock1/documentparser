from typing import Dict, Any

from Main.Parser.Objects.Object import Object


class Socials(Object):
    def __init__(self,
                 viber: Dict,
                 whatsup: Dict,
                 telegram: Dict,
                 facebook: Dict,
                 linkedin: Dict,
                 instagram: Dict,
                 vkontakte: Dict):

        super().__init__()

        self.viber = viber
        self.whatsup = whatsup
        self.telegram = telegram
        self.facebook = facebook

        self.linkedin = linkedin
        self.instagram = instagram
        self.vkontakte = vkontakte

    def getObject(self) -> Dict[str, Any]:
        return {
            'fb': self.facebook,
            'lin': self.linkedin,
            'insta': self.instagram,
            'vk': self.vkontakte,
            'wup': self.whatsup,
            'tg': self.telegram,
            'viber': self.viber
        }
