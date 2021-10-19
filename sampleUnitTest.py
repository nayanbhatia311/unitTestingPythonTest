import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        file1 = True
        file2 = True
        self.assertEqual(file1, file2)

if __name__ == '__main__':
    unittest.main()