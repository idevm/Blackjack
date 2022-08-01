import unittest

from pytest import skip
import blackjack

class BlackjackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bj = blackjack

    def test_getBet_ValidInput_return_bet(self):
        maxBet = 500
        for i in [1, 5, 10, 200, 500]:
            with self.subTest(i):
                self.assertEqual(self.bj.getBet(maxBet, str(i)), i)
    
    def test_getBet_invalidInput_return_0(self):
        maxBet = 500
        for i in ['g', -5, 1000, 501]:
            with self.subTest(i):
                self.assertEqual(self.bj.getBet(maxBet, str(i)), 0)

    def test_getDeck_return_listOfTuple(self):
        self.assertIsInstance(self.bj.getDeck(), list)
        self.assertIsInstance(self.bj.getDeck()[0], tuple)

    def test_getDeck_return_listOf52Items(self):
        self.assertEqual(len(self.bj.getDeck()), 52)
        
    def test_getHandValue_correctInput_return_value(self):
        exp = [12, 6]
        params = [[('2', chr(9829)), ('J', chr(9829))], [('6', chr(9829))]]
        for i in range(2):
            with self.subTest(i):
                self.assertEqual(self.bj.getHandValue(params[i]), exp[i])
        

if __name__ == '__main__':
    unittest.main()