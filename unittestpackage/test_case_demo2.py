import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass print')

    def setUp(self):
        print('setUp print')

    def test_MethodA(self):
        print('test_MethodA print')

    def test_MethodB(self):
        print('test_MethodB print')

    def tearDown(self):
        print('tearDown print')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass print')


if __name__ == '__main__':
    unittest.main(verbosity=2)
