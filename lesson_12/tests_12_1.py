import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner('test_walk')
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = runner.Runner('test_run')
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        w = runner.Runner('test_walk')
        r = runner.Runner('test_run')
        for _ in range(10):
            w.walk()
            r.run()
        self.assertNotEqual(w.distance, r.distance)


if __name__ == '__main__':
    unittest.main()
