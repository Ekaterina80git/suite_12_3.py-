import unittest
import tests_12_1
import tests_12_2

runnST = unittest.TestSuite()

runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))


test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(runnST)



