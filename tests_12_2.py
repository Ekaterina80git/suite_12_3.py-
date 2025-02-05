import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн',10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        for test_key,test_value in cls.all_results.items():
            print(f'Тест:{test_key}')
            for key,value in test_value.items():
                print(f'\t{key}:{value.name}')

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament1 = Tournament(90,self.runner_1,self.runner_3)
        all_results = tournament1.start()
        self.assertEqual(all_results[max(all_results)],self.runner_3)
        TournamentTest.all_results[1] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament2 = Tournament(90,self.runner_2,self.runner_3)
        all_results = tournament2.start()
        self.assertEqual(all_results[max(all_results)],self.runner_3)
        TournamentTest.all_results[1] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament3 = Tournament(90,self.runner_2,self.runner_1,self.runner_3)
        all_results = tournament3.start()
        self.assertEqual(all_results[max(all_results)],self.runner_3)
        TournamentTest.all_results[1] = all_results


if __name__ == '__main__':
    unittest.main()