import unittest

from project.car_manager import Car

class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 17, 100)


    def test_init(self):
        self.assertEqual(self.car.make, "Nissan")
        self.assertEqual(self.car.model, "GT-R")
        self.assertEqual(self.car.fuel_consumption, 17)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_invalid_make(self):
        with self.assertRaises(Exception) as context:
            Car("", "GT-R", 17, 100)
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

        # Additional checks for None or other falsy values
        with self.assertRaises(Exception) as context:
            Car(None, "GT-R", 17, 100)
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")


    def test_invalid_model(self):
        with self.assertRaises(Exception) as context:
            Car("Nissan", "", 17, 100)
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

        # Additional checks for None or other falsy values
        with self.assertRaises(Exception) as context:
            Car("Nissan", None, 17, 100)
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")


    def test_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as context:
            Car("Nissan", "GT-R", 0, 100)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            Car("Nissan", "GT-R", -1, 100)
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")


    def test_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as context:
            Car("Nissan", "GT-R", 17, 0)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            Car("Nissan", "GT-R", 17, -1)
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_invalid_fuel_amount(self):
        # Create a car with valid parameters
        car = Car("Nissan", "GT-R", 17, 100)

        # Try to set a negative fuel amount
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

        # Verify that setting to 0 is allowed (since the error message only mentions negative values)
        car.fuel_amount = 0
        self.assertEqual(car.fuel_amount, 0)


    def test_refuel_success(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

        # Test refueling with an amount that does not exceed capacity
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 30)

        # Check if it gets capped when capacity is exceeded
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, 100)


    def test_refuel_fail(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-5)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")


    def test_drive_success(self):
        self.car.refuel(100)
        initial_fuel = self.car.fuel_amount
        self.car.drive(1)
        expected_fuel = initial_fuel - (1 / 100) * self.car.fuel_consumption
        self.assertEqual(self.car.fuel_amount, expected_fuel)


    def test_drive_fail(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")



if __name__ == '__main__':
    unittest.main()

