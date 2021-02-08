#STEP 10
print("\nStep 10")
def test_abs1():
    assert abs(42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(42) == -42, "Should be absolute value of a number"

if __name__ == '__main__':
    test_abs1()
    #test_abs2()
    print("All tests passed!")


# STEP 11
print("\nStep 11\n")
import unittest

class TestAbs(unittest.TestCase):
    def test_abs3(self):
        self.assertEqual(abs(42), 42, "Should be absolute value of a number")
    def test_abs4(self):
        self.assertEqual(abs(42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()




