import unittest
from shh_client import CustomSSHClient

class TestCaseSHHClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ssh_client = CustomSSHClient('10.199.196.125',22,'root', 'abc123')

    def test_shh_client(self):
        op=self.ssh_client.check_output('whoami')
        print(op)
        self.assertIn((b'root\n', b''),op)

    @classmethod
    def tearDownClass(cls):
        del cls.ssh_client

if __name__ == '__main__':
    unittest.TestCase()