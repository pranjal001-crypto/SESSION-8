import unittest
from student_utils import average, grade


class TestStudentUtils(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([60, 70, 80]), 70)

    def test_single_mark(self):
        self.assertEqual(average([50]), 50)

    def test_pass_boundary(self):
        self.assertEqual(grade(40), "C")

    def test_fail(self):
        self.assertEqual(grade(39), "F")

    def test_a_grade(self):
        self.assertEqual(grade(90), "A")

    def test_b_grade(self):
        self.assertEqual(grade(60), "B")


if __name__ == "__main__":
    unittest.main()
