import unittest
import task51_60

class Test_task_51_60(unittest.TestCase):

    def test_task_51(self):
        self.assertTrue(issubclass (task51_60.NewYorker, task51_60.American))

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