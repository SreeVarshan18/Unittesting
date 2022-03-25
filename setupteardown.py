import calculator

import unittest


class myapp(unittest.TestCase):

    def setUp(self):
        self.a = 60
        self.b = 30

    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_add(self):
        c = calculator.add2no(self.a, self.b)
        self.assertEqual(c, self.a+self.b)

    def test_sub(self):
        c = calculator.sub2no(self.a, self.b)
        self.assertEqual(c, self.a-self.b)

    def test_mul(self):
        c = calculator.mul2no(self.a, self.b)
        self.assertEqual(c, self.a*self.b)

    def test_div(self):
        c = calculator.div2no(self.a, self.b)
        self.assertEqual(c, self.a/self.b)


if __name__ == "__main__":
    unittest.main()

