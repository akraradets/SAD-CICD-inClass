from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class TestSet_A(TestCase):
    def this_test_will_be_ignored(self):
        print("---- This won't run")
        self.assertIs(True, True)

    def test_that_run(self):
        print("---- TestSet_A.test_that_run")
        self.assertIs(True, True)
        print("---- This will be execute")
        self.assertIs(True, False)
        print("---- This will not")

class TestSet_B(TestCase):
    def test_2(self):
        print('---- test_2')
        self.assertIs(True, True)
    def test_1(self):
        print('---- test_1')
        self.assertIs(True, True)

class TestSet_C(TestCase):
    value = "A"
    def test_1(self):
        print(f"---- test_1:{self.value}")
        self.value = 'B'
        self.test_2()
        print("---- End test_1")

    def test_2(self):
        print(f"---- test_2:{self.value}")
        pass