import unittest

from game import Card_game


class TestGameUnit(unittest.TestCase):

    def setUp(self):
        print('Start test !')
        self.game = Card_game()

    def tearDown(self):
        print('Test complete !')
        pass

    def test_init_suit(self):
        p = 0
        k = 0
        c = 0
        b = 0
        for i in self.game.deck:
            if 'пики' in i:
                p += 1
            elif 'крести' in i:
                k += 1
            elif 'червы' in i:
                c += 1
            elif 'буби' in i:
                b += 1
        self.assertEqual(p, 9)
        self.assertEqual(k, 9)
        self.assertEqual(c, 9)
        self.assertEqual(b, 9)

    def test_init_card(self):
        a = 0
        k = 0
        q = 0
        j = 0
        for i in self.game.deck:
            if 'A' in i:
                a += 1
            elif 'K' in i:
                k += 1
            elif 'Q' in i:
                q += 1
            elif 'J' in i:
                j += 1
        self.assertEqual(a, 4)
        self.assertEqual(k, 4)
        self.assertEqual(q, 4)
        self.assertEqual(j, 4)

    def test_ranked(self):
        self.assertEqual(self.game.ranked_card('7'), 7)

    def test_creation_deck_pl(self):
        self.game.creation_deck_player()
        self.assertEqual(len(self.game.deck_cards_player), 6)

    def test_creation_deck(self):
        self.game.creation_deck_comp()
        self.assertEqual(len(self.game.deck_cards_comp), 6)

    def test_trump_card(self):
        self.game.trump_card()
        self.assertNotIn(self.game.trump_card, self.game.deck)

    def test_disunion_deck_player(self):
        self.game.creation_deck_player()
        self.game.disunion_deck_player()
        self.assertEqual(len(self.game.disunion_deck_player), 6)
        for i in self.game.disunion_deck_player:
            self.assertEqual(len(i), 2)

    def test_disunion_deck_comp(self):
        self.game.creation_deck_comp()
        self.game.disunion_deck_comp()
        self.assertEqual(len(self.game.disunion_deck_comp), 6)
        for i in self.game.disunion_deck_comp:
            self.assertEqual(len(i), 2)

