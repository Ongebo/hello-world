from hello import hello_word
import unittest


class HelloTests(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 67)

    def test_hello_world_with_wrong_return_value(self):
        self.assertFalse(hello_world(), 78)


if __name__ = '__main__':
    unittest.main()

