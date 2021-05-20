from constants.deck_decode_constants import CURRENT_FORMAT_VERSION, SUPPORTED_VERSIONS, faction_mapping
from config import NUMBER_OF_SETS
from utils.base32_utils import decode_base32, int_list, encode_base32_from_list
from typing import List
import json
from statics import STATIC_ABSOLUTE_PATH


class LORDeckUtils:
    def decode_from_string(self, deck_code: str) -> dict:
        """
        Decode deck string into deck dict
        :param deck_code: String with the deck code
        :return: Deck dict
        """
        raw_data = decode_base32(deck_code)
        data = int_list(raw_data)
        return self.__generate_card_dict(data)

    def encode_from_dict(self, deck_dict: dict) -> str:
        """
        From a deck dict it returns a deck string
        :param deck_dict: Dict with the deck data.
        :return: String encoding the deck
        """
        copies_dict = self.__generate_copies_dict(deck_dict)
        list_of_int = self.__generate_list_of_ints(copies_dict)
        return encode_base32_from_list(list_of_int)

    def __generate_copies_dict(self, deck_dict: dict) -> dict:
        """
        From a deck dict, it formats to a copies dict
        :param deck_dict: Dict with the deck data.
        :return: Returns copies dict
        """
        copies_dict = {
            3: {},
            2: {},
            1: {}
        }
        for card_code in deck_dict.keys():
            copies = deck_dict[card_code]
            lor_set, region, number = self.__divide_code(card_code)
            if lor_set not in copies_dict[copies]:
                copies_dict[copies][lor_set] = {}
                copies_dict[copies][lor_set][region] = [number]
            elif region not in copies_dict[copies][lor_set]:
                copies_dict[copies][lor_set][region] = [number]
            else:
                copies_dict[copies][lor_set][region].append(number)
        return copies_dict

    def __generate_list_of_ints(self, copies_dict: dict) -> List[int]:
        """
        From a copies dict returns a list of ints with the encoded deck
        :param copies_dict: Dict of copies
        :return: List of integers
        """
        list_of_int = [CURRENT_FORMAT_VERSION]
        for copies in copies_dict.keys():
            sets = copies_dict[copies]
            count = 0
            local_list = []
            for lor_set in sets.keys():
                for region in sets[lor_set].keys():
                    count += 1
                    local_list.append(len(sets[lor_set][region]))
                    local_list.append(lor_set)
                    local_list.append(region)
                    for card in sets[lor_set][region]:
                        local_list.append(card)
            list_of_int.extend([count] + local_list)
        return list_of_int

    def __divide_code(self, code: str) -> (int, int, int):
        """
        Gets a card code and divide in in its components
        :param code: String with a card code
        :return: Tuple with al the card data
        """
        lor_set = int(code[0:2])
        region = faction_mapping[code[2:4]]
        number = int(code[4:])
        return lor_set, region, number

    def __generate_card_dict(self, data: List[int]) -> dict:
        """
        Takes a list of integers and returns a card dict
        :param data: List of integers
        :return: Deck dict
        """
        cards_dict = {}
        version = data.pop(0)
        if version not in SUPPORTED_VERSIONS:
            raise Exception("Version not supported")

        copies = [3, 2, 1]
        while len(data) > 0:
            n_card_copies = data.pop(0)
            copies_value = copies.pop(0)
            for item in range(n_card_copies):
                n_cards = data.pop(0)
                set_number = data.pop(0)
                faction = data.pop(0)
                for cards in range(n_cards):
                    card_number = data.pop(0)
                    cards_dict[f'{set_number:02}{faction_mapping.get(faction)}{card_number:03}'] = copies_value
        return cards_dict

    def __lor_set_dict(self, set_path: str) -> dict:
        """
        From the path to a json of set return a dict with the json data
        :param set_path: String with the path to the set json
        :return: Dict of the set
        """
        with open(set_path, 'rb') as json_file:
            result_dict = {}
            data = json.load(json_file)
            for card in data:
                result_dict[card['cardCode']] = card
            return result_dict

    def __lor_set_list(self, set_path: str) -> dict:
        """
        From the path to a json of set return a dict with the json data
        :param set_path: String with the path to the set json
        :return: Dict of the set
        """
        with open(set_path, 'rb') as json_file:
            data = json.load(json_file)
            return data

    def get_sets_dict(self):
        """
        Returns a dict with all the cards from the current sets
        :return: Dict with the cards from all sets
        """
        sets_json = {}
        for lor_set in range(1, NUMBER_OF_SETS + 1):
            set_path = f'{STATIC_ABSOLUTE_PATH}/set{lor_set}-en_us.json'
            sets_json = {
                **sets_json,
                **self.__lor_set_dict(set_path)
            }
        return sets_json

    def get_sets_list(self):
        sets_list = []
        for lor_set in range(1, NUMBER_OF_SETS + 1):
            set_path = f'{STATIC_ABSOLUTE_PATH}/set{lor_set}-en_us.json'
            sets_list.extend(self.__lor_set_list(set_path))
        return sets_list
