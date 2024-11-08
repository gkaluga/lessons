import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = rt.Runner('test_walk')
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = rt.Runner('test_run')
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        w = rt.Runner('test_walk')
        r = rt.Runner('test_run')
        for _ in range(10):
            w.walk()
            r.run()
        self.assertNotEqual(w.distance, r.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament (self):
        participants = (self.r_u, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[1] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament (self):
        participants = (self.r_a, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[2] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament (self):
        participants = (self.r_u, self.r_a, self.r_n)
        t = rt.Tournament(90, *participants)
        result = t.start()
        TournamentTest.all_results[3] = result
        worst_rezult = result[max(result.keys())]
        slowest_runner = min(participants, key=lambda val: val.speed)
        self.assertTrue(worst_rezult.name == slowest_runner.name)


if __name__ == '__main__':
    unittest.main()
