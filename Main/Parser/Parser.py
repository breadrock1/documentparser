import re
from typing import Dict

from Main.Parser.Objects.Implements.Candidate import Candidate
from Main.Parser.Objects.Implements.Contacts import Contacts
from Main.Parser.Objects.Implements.Socials import Socials


REGEXP_AGE = r'(\d+) года'
REGEXP_EMAIL = r'\S+@\S+\.\S+'
REGEXP_VK_LINK = r'(http|https):\/\/(www\.vk|vk\.)\S+'
REGEXP_FB_LINK = r'(http|https):\/\/(www\.facebook\.|facebook\.)\S+'
REGEXP_PHONE_NUMBER = r'(\+\d+)(-|\s)\(\d+\)(-|\s)\d+(-|\s)\d+(-|\s)\d+'


class Parser(object):
    def __init__(self):
        self.candidate = Candidate

    def _parseContacts(self, text_data: str) -> Contacts:
        email_match = re.search(REGEXP_EMAIL, text_data)
        phone_match = re.search(REGEXP_PHONE_NUMBER, text_data)

        return Contacts(mail=email_match.group(), phone=phone_match.group())

    def _parseSocialNetworkLinks(self, text_data: str) -> Socials:
        vk_match = re.search(REGEXP_VK_LINK, text_data)
        fb_match = re.search(REGEXP_FB_LINK, text_data)

        return Socials(
            viber={},
            whatsup={},
            telegram={},
            linkedin={},
            instagram={},
            facebook={'link': fb_match},
            vkontakte={'link': vk_match}
        )

    def parse(self, extracted_data: str) -> Candidate:
        return Candidate(
            contacts=self._parseContacts(text_data=extracted_data),
            socials=self._parseSocialNetworkLinks(text_data=extracted_data)
        )


if __name__ == '__main__':
    parser = Parser()

    with open('/Users/breadrock/AppData/Projects/DocumentParser/Test/TestFiles/extracted_data', 'r') as file:
        data = file.read()
        file.close()

    parser.parse(extracted_data=data)
