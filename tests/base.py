from app import index
import unittest


class MyTest(unittest.TestCase):
    def test_the_index_returning_value(self):
        ''' this is just a simple unittest
        to see are tests work in circleci or not'''
        result = index()
        expected_value = 'hello, world with CI/CD'
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
