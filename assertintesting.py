import unittest

def mylist():
    list = [1,2,3]
    return list

class mylistcheck(unittest.TestCase):

    def test_case(self):
        ele = 2
        self.assertIn(ele, mylist())

    def test_case2(self):
        ele = 4
        self.assertNotIn(ele, mylist())


if __name__ == "__main__":
    unittest.main()

