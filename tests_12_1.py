import unittest
import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        walk = Runner.Runner('Tom')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance,50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        run = Runner.Runner('Anton')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance,100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        obg_1 = Runner.Runner('Victoria')
        obg_2 = Runner.Runner('Alex')
        for i in range(10):
            obg_1.walk()
            obg_2.run()
        self.assertNotEqual(obg_1.distance,obg_2.distance)


if __name__ == '__main__':
    unittest.main()






