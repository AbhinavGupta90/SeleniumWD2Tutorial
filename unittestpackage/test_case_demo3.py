import unittest


class TestCaseDemo3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass here')

    def setUp(self):
        print('setUp here')

    def test_methodA(self):
        print('test_methodA here')

    def test_methodB(self):
        print('test_methodB here')

    def tearDown(self):
        print('tearDown here')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass here')


if __name__ == '__main__':
    unittest.main(verbosity=2)
