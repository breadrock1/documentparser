import re
from typing import Dict

from Main.Parser.Objects.Implements.Candidate import Candidate
from Main.Parser.Objects.Implements.Contacts import Contacts
from Main.Parser.Objects.Implements.Personal import Personal
from Main.Parser.Objects.Implements.Socials import Socials


REGEXP_AGE = r'(\d+) года'
REGEXP_EMAIL = r'\S+@\S+\.\S+'
REGEXP_VK_LINK = r'(http|https):\/\/(www\.vk|vk\.)\S+'
REGEXP_LI_LINK = r'(http|https):\/\/(www\.linkedin|linkedin\.)\S+'
REGEXP_FB_LINK = r'(http|https):\/\/(www\.facebook\.|facebook\.)\S+'
REGEXP_INST_LINK = r'(http|https):\/\/(www\.instagram|instagram\.)\S+'
REGEXP_PHONE_NUMBER = r'(\+\d+)(-|\s)\(\d+\)(-|\s)\d+(-|\s)\d+(-|\s)\d+'


class Parser(object):
    def __init__(self):
        self.candidate = Candidate

    @staticmethod
    def _parseGetNameAndMarkData(text_data: str) -> Dict:
        striped_data = text_data.strip(' ')
        name = f'{striped_data[0]} {striped_data[1]}'

        # TODO: How get this info?
        mark = ''

        return {'name': name, 'mark': mark}

    @staticmethod
    def _parsePersonalData(text_data: str) -> Personal:
        age_match = re.search(r'\d+ год', text_data)
        age = age_match.group()

        # TODO: How get this info?
        city = ''
        position = ''

        return Personal(
            age=age,
            city=city,
            position=position
        )

    @staticmethod
    def _parseContacts(text_data: str) -> Contacts:
        email_match = re.search(REGEXP_EMAIL, text_data)
        phone_match = re.search(REGEXP_PHONE_NUMBER, text_data)

        return Contacts(mail=email_match.group(), phone=phone_match.group())

    @staticmethod
    def _parseSocialNetworkLinks(text_data: str) -> Socials:
        # TODO: How get another data?
        vk_match = re.search(REGEXP_VK_LINK, text_data)
        fb_match = re.search(REGEXP_FB_LINK, text_data)
        li_match = re.search(REGEXP_LI_LINK, text_data)
        inst_match = re.search(REGEXP_INST_LINK, text_data)

        return Socials(
            viber={},
            whatsup={},
            telegram={},
            linkedin={'link': li_match},
            facebook={'link': fb_match},
            vkontakte={'link': vk_match},
            instagram={'link': inst_match}
        )

    def parse(self, extracted_data: str) -> Candidate:
        name_and_mark = self._parseGetNameAndMarkData(extracted_data)

        return Candidate(
            name=name_and_mark.get('name'),
            mark=name_and_mark.get('mark'),
            contacts=self._parseContacts(text_data=extracted_data),
            personal=self._parsePersonalData(text_data=extracted_data),
            socials=self._parseSocialNetworkLinks(text_data=extracted_data)
        )


if __name__ == '__main__':
    parser = Parser()

    with open('/Users/breadrock/AppData/Projects/DocumentParser/Test/TestFiles/extracted_data', 'r') as file:
        data = file.read()
        file.close()

    parser.parse(extracted_data=data)
