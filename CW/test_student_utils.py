import unittest
from student_utils import average, grade


class TestStudentUtils(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([60, 70, 80]), 70)

    def test_single_mark(self):
        self.assertEqual(average([50]), 50)

    def test_two_marks(self):
        self.assertEqual(average([40, 60]), 50)

    def test_39(self):
        self.assertEqual(grade(39), "F")

    def test_40(self):
        self.assertEqual(grade(40), "C")

    def test_59(self):
        self.assertEqual(grade(59), "C")

    def test_60(self):
        self.assertEqual(grade(60), "B")

    def test_89(self):
        self.assertEqual(grade(89), "B")

    def test_90(self):
        self.assertEqual(grade(90), "A")

    def test_100(self):
        self.assertEqual(grade(100), "A")


if __name__ == "__main__":
    unittest.main()
