import unittest

class CustomTestcase(unittest.TestCase):
    def test_power(self):
        self.assertEqual(pow(2,3),8)

    @unittest.SkipTest
    def test_failure(self):
        self.assertEqual(pow(2,2),4)

if __name__ == '__main__':
    unittest.main()

    """command line : python -m model_name psut1.Customtestcase.test_power -v"""