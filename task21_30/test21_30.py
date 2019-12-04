import unittest
import task21_30


class Test_task_21_30(unittest.TestCase):

    def test_task_21(self):
        self.assertEqual(task21_30.task_21("UP 5 DOWN 3 LEFT 3 RIGHT 2"), 2)

    def test_task_21_empty(self):
        self.assertEqual(task21_30.task_21(""), 0)

    def test_task_21_only_one(self):
        self.assertEqual(task21_30.task_21("UP 5"), 5)

    def test_task_22(self):
        self.assertEqual(task21_30.task_22("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"),
                         [('2', 2), ('3', 1), ('3?', 1), ('New', 1), ('Python', 5), ('Read', 1), ('and', 1), ('between', 1), ('choosing', 1), ('or', 2), ('to', 1)])

    def test_task_22_empty(self):
        self.assertEqual(task21_30.task_22(""), [])

    def test_task_22_only_one(self):
        self.assertEqual(task21_30.task_22("New"), [('New', 1)])

    def test_task_23(self):
        self.assertEqual(task21_30.task_23(3), 9)

    def test_task_23_negative(self):
        self.assertEqual(task21_30.task_23(-2), 4)

    def test_task_23_zero(self):
        self.assertEqual(task21_30.task_23(0), 0)

    def test_task_23_one(self):
        self.assertEqual(task21_30.task_23(1), 1)

    def test_task_23_empty(self):
        self.assertEqual(task21_30.task_23(), 'You have not entered a data.')

    def test_task_26(self):
        self.assertEqual(task21_30.task_26(1,2), 3)

    def test_task_26_two_negative(self):
        self.assertEqual(task21_30.task_26(-1,-2), -3)

    def test_task_26_negative_and_positive(self):
        self.assertEqual(task21_30.task_26(1,-2), -1)

    def test_task_26_one_zero(self):
        self.assertEqual(task21_30.task_26(1,0), 1)

    def test_task_26_two_zeros(self):
        self.assertEqual(task21_30.task_26(0,0), 0)

    def test_task_26_one_empty(self):
        self.assertEqual(task21_30.task_26(1), 'You have not entered a data.')

    def test_task_26_two_empty(self):
        self.assertEqual(task21_30.task_26(), 'You have not entered a data.')

    def test_task_27(self):
        self.assertEqual(task21_30.task_27(15), '15')

    def test_task_27_empty(self):
        self.assertEqual(task21_30.task_27(), 'You have not entered a data.')

    def test_task_29(self):
        self.assertEqual(task21_30.task_29('2 3'), 5)

    def test_task_29_one_negative(self):
        self.assertEqual(task21_30.task_29('-2 3'), 1)

    def test_task_29_empty(self):
        self.assertEqual(task21_30.task_29(''), 'You have not entered a data.')

    def test_task_30(self):
        self.assertEqual(task21_30.task_30("hello", "world"), 'helloworld')

    def test_task_30_empty(self):
        self.assertEqual(task21_30.task_30("",""), '')

    def test_task_30_two_numbers(self):
        self.assertEqual(task21_30.task_30("1","2"), '12')

    def test_task_30_str_and_number(self):
        self.assertEqual(task21_30.task_30("am","-2"), 'am-2')




if __name__ == '__main__':
    unittest.main()
