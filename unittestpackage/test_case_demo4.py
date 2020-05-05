import unittest


class TestCaseDemo4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass here')

    def setUp(self):
        print('setUp here')

    def test_MethodA(self):
        print('test_MethodA here')

    def test_MethodB(self):
        print('test_MethodB here')

    def tearDown(self):
        print('tearDown here')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass here')


if __name__ == '__main__':
    unittest.main(verbosity=2)
