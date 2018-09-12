from hello import hello_word
import unittest


class HelloTests(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 67)


if __name__ = '__main__':
    unittest.main()

