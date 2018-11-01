import unittest
from random import randint


class SetupAndTierdown(unittest.TestCase):
    def setUp(self):
        self.data_set=[randint(1,20) for i in range(50)]

    def test_check_contain(self):
        self.assertIn(15, self.data_set)

    def test_list_len(self):
        self.assertEqual(len(self.data_set), 50)

    def tearDown(self):
        del self.data_set

if __name__ == '__main__':
    unittest.main()