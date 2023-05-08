import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("spades", 3)
        self.card2 = Card("hearts", 8)
        self.card3 = Card("diamonds", 1)
        self.card4 = Card("clubs", 4)
        self.cards1 = [self.card1, self.card2, self.card3]
        self.cards2 = [self.card4]

    def test_card_has_suit(self):
        self.assertEqual("spades", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(3, self.card1.value)

    # check for ace true
    def test_check_for_ace__true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card3))


    # check for ace false
    def test_check_for_ace__false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    #  test for higest card
    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    #  test for cards total
    def test_cards_total(self):
        self.assertEqual("You have a total of 12", self.card_game.cards_total(self.cards1))
        self.assertEqual("You have a total of 4", self.card_game.cards_total(self.cards2))
        self.assertEqual("You have a total of 16", self.card_game.cards_total(self.cards2 + self.cards1))