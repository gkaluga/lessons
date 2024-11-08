import unittest
import tests_12_3

test_suit = unittest.TestSuite()
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suit)