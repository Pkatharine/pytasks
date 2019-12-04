import unittest
import task41_50

class Test_task_41_50(unittest.TestCase):

    def test_task_41(self):
        self.assertEqual(task41_50.task_41(20), (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400))

    def test_task_41_empty(self):
        self.assertEqual(task41_50.task_41(), 'You have not entered a data.')

    def test_task_41_negative(self):
        self.assertEqual(task41_50.task_41(-3), ())

    def test_task_41_zero(self):
        self.assertEqual(task41_50.task_41(0), ())

    def test_task_42(self):
        self.assertEqual(task41_50.task_42(), ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)))

    def test_task_43(self):
        self.assertEqual(task41_50.task_43(), (2, 4, 6, 8, 10))

    def test_task_44_yes(self):
        self.assertEqual(task41_50.task_44('yes'), 'Yes')

    def test_task_44_Yes(self):
        self.assertEqual(task41_50.task_44('Yes'), 'Yes')

    def test_task_44_YES(self):
        self.assertEqual(task41_50.task_44('YES'), 'Yes')

    def test_task_44_empty(self):
        self.assertEqual(task41_50.task_44(''), 'No')

    def test_task_44_another(self):
        self.assertEqual(task41_50.task_44('another'), 'No')

    def test_task_45(self):
        self.assertEqual(task41_50.task_45(), [2, 4, 6, 8, 10])

    def test_task_46(self):
        self.assertEqual(task41_50.task_46(), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_task_47(self):
        self.assertEqual(task41_50.task_47(), [4, 16, 36, 64, 100])

    def test_task_48(self):
        self.assertEqual(task41_50.task_48(20), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_task_48_empty(self):
        self.assertEqual(task41_50.task_48(), 'You have not entered a data.')

    def test_task_48_negative(self):
        self.assertEqual(task41_50.task_48(-3), [])

    def test_task_48_zero(self):
        self.assertEqual(task41_50.task_48(0), [])

    def test_task_49(self):
        self.assertEqual(task41_50.task_49(20),
                         [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])

    def test_task_49_empty(self):
        self.assertEqual(task41_50.task_49(), 'You have not entered a data.')

    def test_task_49_negative(self):
        self.assertEqual(task41_50.task_49(-3), [])

    def test_task_49_zero(self):
        self.assertEqual(task41_50.task_49(0), [])


if __name__ == '__main__':
    unittest.main()
