import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r_u = rt.Runner('Усэйн', 10)
        self.r_a = rt.Runner('Андрей', 9)
        self.r_n = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print({k: v.name for k, v in value.items()})

    def test_first_tournament(self):
        """   1-й тест из задания :return: Ok   """

        participants = (self.r_u, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[1] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)

    def test_second_tournament(self):
        """   2-й тест из задания :return: Ok   """

        participants = (self.r_a, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[2] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)

    def test_third_tournament(self):
        """   3-й тест из задания :return: Ok   """

        participants = (self.r_u, self.r_a, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[3] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)


if __name__ == '__main__':
    unittest.main()
