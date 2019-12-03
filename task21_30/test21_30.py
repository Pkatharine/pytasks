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















if __name__ == '__main__':
    unittest.main()
