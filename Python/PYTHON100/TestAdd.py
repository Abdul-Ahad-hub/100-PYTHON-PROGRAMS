
def add(a, b):
    return a + b


def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(100, 200) == 300

def test_add_strings():
    assert add("Hello", " World") == "Hello World"
    assert add("", "abc") == "abc"

def test_add_lists():
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert add([], [1]) == [1]


import unittest

class TestAdd(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(100, 200), 300)

    def test_strings(self):
        self.assertEqual(add("Hello", " World"), "Hello World")
        self.assertEqual(add("", "abc"), "abc")

    def test_lists(self):
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(add([], [1]), [1])


if __name__ == "__main__":
    unittest.main()
