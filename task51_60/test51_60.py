import unittest
import task51_60

class Test_task_51_60(unittest.TestCase):

    def test_task_51(self):
        self.assertTrue(issubclass (task51_60.NewYorker, task51_60.American))

    def test_task_52(self):
        self.assertEqual(task51_60.Circle(5).area(), 79)

    def test_task_52_zero(self):
        self.assertEqual(task51_60.Circle(0).area(), 0)

    def test_task_52_negative(self):
        self.assertEqual(task51_60.Circle(-5).area(), 'You must enter a positive number')

    def test_task_52_letter(self):
        self.assertEqual(task51_60.Circle(a).area(), 'You must enter only positive number')

    def test_task_53(self):
        self.assertEqual(task51_60.Rectangle(5,4).area(), 18)

    def test_task_53_zeros(self):
        self.assertEqual(task51_60.Rectangle(0,0).area(), 0)

    def test_task_53_negative(self):
        self.assertEqual(task51_60.Rectangle(-5,4).area(), -2)

    def test_task_53_letter(self):
        self.assertEqual(task51_60.Rectangle(5,a).area(), 'You must enter only numbers')

    def test_task_54_subclass(self):
        self.assertTrue(issubclass(task51_60.Square, task51_60.Shape))

    def test_task_54_default_shape(self):
        self.assertEqual(task51_60.Shape().area(), 0)

    def test_task_54_default_square(self):
        self.assertEqual(task51_60.Square().length, 0)

    def test_task_54(self):
        self.assertEqual(task51_60.Square(3).area(), 9)

    def test_task_54_negative(self):
        self.assertEqual(task51_60.Square(-3).area(), 9)

    def test_task_54_zero(self):
        self.assertEqual(task51_60.Square(0).area(), 0)

    def test_task_54_letter(self):
        self.assertEqual(task51_60.Square(a).area(), 'You must enter only number')

    def test_task_55(self):
        self.assertEqual(task51_60.task_55(5), "You are dividing a number by ZERO!")

    def test_task_55_empty(self):
        self.assertEqual(task51_60.task_55(), 'You have not entered a data.')

    def test_task_57(self):
        self.assertEqual(task51_60.task_57('john@google.com'), 'john')

    def test_task_57_numbers(self):
        self.assertEqual(task51_60.task_57('123.@gmail.com'), 'You must using only letters in your email')

    def test_task_57_empty(self):
        self.assertEqual(task51_60.task_57(''), 'You have not entered a data.')

    def test_task_58(self):
        self.assertEqual(task51_60.task_58('john@google.com'), 'google')

    def test_task_58_numbers(self):
        self.assertEqual(task51_60.task_58('john@123google.com'), 'You must using only letters in your email')

    def test_task_58_empty(self):
        self.assertEqual(task51_60.task_58(''), 'You have not entered a data.')

    def test_task_59(self):
        self.assertEqual(task51_60.task_59('2 cats and 3 dogs'), ['2', '3'])

    def test_task_59_only_letters(self):
        self.assertEqual(task51_60.task_59('cats and dogs'), [])

    def test_task_59_empty(self):
        self.assertEqual(task51_60.task_59(''), 'You have not entered a data.')

    def test_task_60(self):
        self.assertEqual(task51_60.task_60(), "hello world")





if __name__ == '__main__':
    unittest.main()