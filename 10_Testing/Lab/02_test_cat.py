import unittest

class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")


    def test_init(self):
        self.assertEqual(self.cat.name, "Tom")
        self.assertEqual(self.cat.fed, False)
        self.assertEqual(self.cat.sleepy,False)
        self.assertEqual(self.cat.size, 0)


    def test_size_increases_after_eating(self):
        initial_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size, initial_size + 1)


    def test_cat_is_fed_after_eating(self):
        self.assertEqual(self.cat.fed, False)
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)



    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), "Already fed.")


    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), "Cannot sleep while hungry")


    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()

