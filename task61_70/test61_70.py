import unittest
import task61_70


class Test_task_61_70(unittest.TestCase):

    def test_task_61(self):
        self.assertEqual(task61_70.task_61('hello'), b'hello')

    def test_task_61_numbers(self):
        self.assertEqual(task61_70.task_61('123'), b'123')

    def test_task_61_empty(self):
        self.assertEqual(task61_70.task_61(''), b'')

    def test_task_63(self):
        self.assertEqual(task61_70.task_63(5), 4)

    def test_task_63_zero(self):
        self.assertEqual(task61_70.task_63(0), 0)

    def test_task_63_negative(self):
        self.assertEqual(task61_70.task_63(-2), 0)

    def test_task_64_empty(self):
        self.assertEqual(task61_70.task_63(), 'You have not entered a data.')

    def test_task_65(self):
        self.assertEqual(task61_70.task_65(7), 13)

    def test_task_65_negative(self):
        self.assertEqual(task61_70.task_65(-2), 'You must enter a positive number')

    def test_task_65_zero(self):
        self.assertEqual(task61_70.task_65(0), 0)

    def test_task_65_one(self):
        self.assertEqual(task61_70.task_65(1), 1)

    def test_task_65_empty(self):
        self.assertEqual(task61_70.task_65(), 'You have not entered a data.')

    def test_task_66(self):
        self.assertEqual(task61_70.task_66(7), 13)

    def test_task_66_negative(self):
        self.assertEqual(task61_70.task_66(-2), 'You must enter a positive number')

    def test_task_66_zero(self):
        self.assertEqual(task61_70.task_66(0), 0)

    def test_task_66_one(self):
        self.assertEqual(task61_70.task_66(1), 1)

    def test_task_66_empty(self):
        self.assertEqual(task61_70.task_66(), 'You have not entered a data.')

    def test_task_68(self):
        self.assertEqual(task61_70.task_68(10), '0,2,4,6,8,10')

    def test_task_68_negative(self):
        self.assertEqual(task61_70.task_68(-10), '')

    def test_task_68_zero(self):
        self.assertEqual(task61_70.task_68(0), '0')

    def test_task_68_empty(self):
        self.assertEqual(task61_70.task_68(), 'You have not entered a data.')

    def test_task_69(self):
        self.assertEqual(task61_70.task_69(100), '0,35,70')

    def test_task_69_negative(self):
        self.assertEqual(task61_70.task_69(-10), '')

    def test_task_69_zero(self):
        self.assertEqual(task61_70.task_69(0), '0')

    def test_task_69_empty(self):
        self.assertEqual(task61_70.task_69(), 'You have not entered a data.')




if __name__ == '__main__':
    unittest.main()
