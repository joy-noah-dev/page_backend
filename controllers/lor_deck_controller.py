from utils.lor_deck_utils import LORDeckUtils


class LorDeckController:
    lor = LORDeckUtils()

    def decode_deck(self, deck_string):
        """
        Decode a deck and returns a dict with all the cards data
        :param deck_string: String with the encoded deck
        :return:
        """
        deck_data = []

        deck = self.lor.decode_from_string(deck_string)
        for card in deck.keys():
            deck_data.append({
                "copies": deck[card],
                **self.lor.get_sets_dict()[card]
            })
        return deck_data
