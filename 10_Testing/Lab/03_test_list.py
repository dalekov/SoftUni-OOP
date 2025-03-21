import unittest


class IntegerListTests(unittest.TestCase):
    def test_init_takes_integers(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integer_list.get_data())

    def test_init_ignores_non_integers(self):
        integer_list = IntegerList(1, 2, 3, [4], 5.5, "6")
        self.assertEqual([1, 2, 3], integer_list.get_data())

    def test_add_integer(self):
        # Test adding an integer
        integer_list = IntegerList(1, 2)
        result = integer_list.add(3)
        self.assertEqual([1, 2, 3], result)  # check that the add method returns the updated list
        self.assertEqual([1, 2, 3], integer_list.get_data())  # check that the internal state is correctly updated

    def test_add_non_integer(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(ValueError) as context:
            integer_list.add("4")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_valid_index(self):
        integer_list = IntegerList(1, 2)
        result = integer_list.remove_index(1)  # Returns the removed element, in this case 2

        self.assertEqual(2, result)
        self.assertEqual([1], integer_list.get_data())

    def test_remove_invalid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as context:
            integer_list.remove_index(2)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_valid_index(self):
        integer_list = IntegerList(1, 2)
        result = integer_list.get(1)
        self.assertEqual(2, result)

    def test_get_invalid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as context:
            integer_list.get(2)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_valid_data(self):
        integer_list = IntegerList(1, 2)
        integer_list.insert(1, 3)
        self.assertEqual([1, 3, 2], integer_list.get_data())

    def test_insert_invalid_index(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(IndexError) as context:
            integer_list.insert(2, 3)

        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_invalid_element(self):
        integer_list = IntegerList(1, 2)
        with self.assertRaises(ValueError) as context:
            integer_list.insert(1, "4")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest(self):
        integer_list = IntegerList(1, 2)
        result = integer_list.get_biggest()
        self.assertEqual(2, result)

    def test_get_index(self):
        integer_list = IntegerList(1, 2)
        result = integer_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()