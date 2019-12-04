import unittest
import task71_80


class Test_task_71_80(unittest.TestCase):

    def test_task_71(self):
        self.assertEqual(task71_80.task_71('35+3'), 38)

    def test_task_71_letter(self):
        self.assertEqual(task71_80.task_71('35+a'), 'You must enter only numbers')

    def test_task_71_negative(self):
        self.assertEqual(task71_80.task_71('-35+-5'), -40)

    def test_task_71_empty(self):
        self.assertEqual(task71_80.task_71(''), 'You have not entered a data.')

    def test_task_72(self):
        self.assertEqual(task71_80.task_72([2, 5, 7, 9, 11, 17, 222], 5), 1)

    def test_task_72_negative(self):
        self.assertEqual(task71_80.task_72([2, 5, 7, 9, 11, 17, 222], -5), -1)

    def test_task_72_empty(self):
        self.assertEqual(task71_80.task_72([2, 5, 7, 9, 11, 17, 222], ), 'You have not entered a data.')

    def test_task_73(self):
        self.assertEqual(task71_80.task_73([2, 5, 7, 9, 11, 17, 222], 5), 1)

    def test_task_73_negative(self):
        self.assertEqual(task71_80.task_73([2, 5, 7, 9, 11, 17, 222], -5), -1)

    def test_task_73_empty(self):
        self.assertEqual(task71_80.task_73([2, 5, 7, 9, 11, 17, 222], ), 'You have not entered a data.')

    def test_task_73_letter(self):
        self.assertEqual(task71_80.task_73([2, 5, 7, 9, 11, 17, 222], 'a'), 'You must enter only numbers')

    def test_task_74(self):
        self.assertTrue(10 <= task71_80.task_74() <= 100)

    def test_task_75(self):
        self.assertTrue(5 <= task71_80.task_75() <= 95)

    def test_task_76(self):
        self.assertIn(task71_80.task_76(), [0, 2, 4, 6, 8, 10])

    def test_task_77(self):
        self.assertTrue(0 <= task71_80.task_77() <= 11)

    def test_task_77_zero(self):
        self.assertEqual(task71_80.task_77(), 0)

    def test_task_78(self):
        for i in task71_80.task_78():
            self.assertTrue(100 <= i <= 201)

    def test_task_78_len(self):
        self.assertEqual(len(task71_80.task_78()), 5)

    def test_task_79(self):
        for i in task71_80.task_79():
            self.assertTrue(100 <= i <= 201)

    def test_task_79_len(self):
        self.assertEqual(len(task71_80.task_79()), 5)

    def test_tesk_79_even(self):
        for i in task71_80.task_79():
            self.assertTrue(i%2 == 0)

    def test_task_80(self):
        for i in task71_80.task_80():
            self.assertTrue(1 <= i <= 1001)

    def test_task_80_len(self):
        self.assertEqual(len(task71_80.task_80()), 5)

    def test_tesk_80_division(self):
        for i in task71_80.task_80():
            self.assertTrue(i%5 == 0 and i%7 == 0)





if __name__ == '__main__':
    unittest.main()
