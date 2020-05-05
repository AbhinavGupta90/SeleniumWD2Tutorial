import unittest


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('This is set up class')

    def setUp(self):
        print('This is set up method')

    def test_MethodA(self):
        print('This is method A')

    def test_MethodB(self):
        print('This is method B')

    def tearDown(self):
        print('This is tear down method')

    @classmethod
    def tearDownClass(cls):
        print('This is tear down class')


if __name__ == '__main__':
    unittest.main(verbosity=2)