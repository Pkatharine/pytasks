import unittest
import task91_10


class Test_task_91_100(unittest.TestCase):

    def test_task_91(self):
        self.assertEqual(task91_10.task_91(), [24, 35, 70, 155])

    def test_task_92(self):
        self.assertEqual(task91_10.task_92(), [12, 35, 88, 120, 155])

    def test_task_93(self):
        self.assertEqual(task91_10.task_93(), [35])

    def test_task_94(self):
        self.assertEqual(task91_10.task_94(), [12, 24, 35, 88, 120, 155])

    def test_task_95_male_subclass(self):
        self.assertTrue(issubclass (task91_10.Male, task91_10.Person))

    def test_task_95_female_subclass(self):
        self.assertTrue(issubclass (task91_10.Female, task91_10.Person))

    def test_task_95_person(self):
        self.assertEqual(task91_10.Person().getGender(), 'Person')

    def test_task_95_male(self):
        self.assertEqual(task91_10.Male().getGender(), 'Male')

    def test_task_95_female(self):
        self.assertEqual(task91_10.Female().getGender(), 'Female')

    def test_task_97(self):
        self.assertEqual(task91_10.task_97('rise to vote sir'), 'ris etov ot esir')

    def test_task_97_empty(self):
        self.assertEqual(task91_10.task_97(''), '')

    def test_task_97_numbers(self):
        self.assertEqual(task91_10.task_97('123'), '321')

    def test_task_98(self):
        self.assertEqual(task91_10.task_98('H1e2l3l4o5w6o7r8l9d'), 'Helloworld')

    def test_task_98_empty(self):
        self.assertEqual(task91_10.task_98(''), '')

    def test_task_99(self):
        self.assertEqual(task91_10.task_99(), [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

    def test_task_100(self):
        self.assertEqual(task91_10.task_100(35,94), (12, 23))

    def test_task_100_negative(self):
        self.assertEqual(task91_10.task_100(-35,94), 'You must enter only positive numbers')

    def test_task_100_empty(self):
        self.assertEqual(task91_10.task_100(), 'You have not entered a data.')

    def test_task_100_letter(self):
        self.assertEqual(task91_10.task_100(35,a), 'You must enter only numbers')




if __name__ == '__main__':
    unittest.main()

