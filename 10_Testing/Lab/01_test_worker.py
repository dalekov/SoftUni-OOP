import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Denis", 4000, 100)



    def test_initialization(self):
        self.assertEqual("Denis", self.worker.name)

        self.assertEqual(4000, self.worker.salary)

        self.assertEqual(100, self.worker.energy)

        self.assertEqual(0, self.worker.money)

    def test_rest(self):
        # Store initial energy
        initial_energy = self.worker.energy

        # Call the rest method and capture the result
        self.worker.rest()

        # Assert that energy increased by 1
        self.assertEqual(initial_energy + 1, self.worker.energy)


    def test_work(self):
        initial_money = self.worker.money
        initial_energy = self.worker.energy

        self.worker.work()

        self.assertEqual(initial_money + self.worker.salary, self.worker.money)
        self.assertEqual(initial_energy - 1, self.worker.energy)


        self.worker.energy = 0

        with self.assertRaises(Exception) as context:
            self.worker.work()

        self.assertEqual(str(context.exception), "Not enough energy.")


        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()

        self.assertEqual(str(context.exception), "Not enough energy.")


    def test_get_info(self):
        expected = self.worker.get_info()
        actual = f"{self.worker.name} has saved {self.worker.money} money."

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()