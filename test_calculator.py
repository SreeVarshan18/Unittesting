import sys

import calculator

import unittest


class myapp(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith("win"), "Windows not required")
    def test_add(self):
        a = 40
        b = 20
        c = calculator.add2no(a, b)
        self.assertEqual(c, a+b)

    @unittest.skip("Skipped subtraction test")
    def test_sub(self):
        a = 40
        b = 20
        c = calculator.sub2no(a, b)
        self.assertEqual(c, a-b)

    @unittest.skipUnless(sys.platform.startswith("linux"), "Windows required")
    def test_mul(self):
        a = 40
        b = 20
        c = calculator.mul2no(a, b)
        self.assertEqual(c, a*b)

    def test_div(self):
        a = 40
        b = 20
        c = calculator.div2no(a, b)
        self.assertEqual(c, a/b)


if __name__ == "__main__":
    unittest.main()

