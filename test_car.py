import unittest
from car_factory import CarFactory
from datetime import date

class TestCar(unittest.TestCase):

    def test_create_car(self):
        carFactory = CarFactory()
        car1 = carFactory.create_calliope(date.today(), date(2020, 12, 25), 50000, 50000)
        car2 = carFactory.create_palindrome(date.today(), date(2010, 12, 25), False)
        self.assertEqual(car1.needs_service(), True)
        self.assertEqual(car2.needs_service(), True)


if __name__ == "__main__":
    unittest.main()