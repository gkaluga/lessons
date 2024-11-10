import rt_with_exceptions as rt
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = rt.Runner('Вася', -5)
            for _ in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r = rt.Runner(2)
            for _ in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
        except TypeError:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        w = rt.Runner('Вася')
        r = rt.Runner('Петя')
        for _ in range(10):
            w.walk()
            r.run()
        self.assertNotEqual(w.distance, r.distance)

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    unittest.main()


