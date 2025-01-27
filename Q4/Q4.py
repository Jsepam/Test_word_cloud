import unittest
import sys
sys.path.append("..")
from Q3.Q3 import counter

class TestCounter(unittest.TestCase):

    def test_null_input(self):
        with self.assertRaises(TypeError):
            counter(None)

    def test_empty_input(self):
        result, highest = counter('') 
        self.assertEqual(result, {})
        self.assertEqual(highest, (None, 0))

    def test_invalid_input(self):
        with self.assertRaises(FileNotFoundError):
            counter('invalid_file.txt')

    def test_valid_input(self):
        with open('sample_test.txt', 'w') as f:
            f.write("Hello world! Hello again.")
        
        result, highest = counter('sample_test.txt')
        self.assertEqual(result, {'hello': 2, 'world': 1, 'again': 1})
        self.assertEqual(highest, ('hello', 2))

if __name__ == '__main__':
    unittest.main()