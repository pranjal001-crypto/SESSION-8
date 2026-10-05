import unittest
from student_utils import calculate_average, assign_grade


class TestStudentUtils(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average([60, 70, 80]), 70)

    def test_single_mark(self):
        self.assertEqual(calculate_average([75]), 75)

    def test_average_two_marks(self):
        self.assertEqual(calculate_average([40, 60]), 50)

    def test_39(self):
        self.assertEqual(assign_grade(39), "F")

    def test_40(self):
        self.assertEqual(assign_grade(40), "C")

    def test_59(self):
        self.assertEqual(assign_grade(59), "C")

    def test_60(self):
        self.assertEqual(assign_grade(60), "B")

    def test_89(self):
        self.assertEqual(assign_grade(89), "B")

    def test_90(self):
        self.assertEqual(assign_grade(90), "A")

    def test_100(self):
        self.assertEqual(assign_grade(100), "A")


if __name__ == "__main__":
    unittest.main()
