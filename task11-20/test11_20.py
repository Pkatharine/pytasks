import unittest
import task11_20


class Tests_task_11_20(unittest.TestCase):

    def test_eleven(self):
        self.assertEqual(task11_20.task_11("0100,0011,1010,1001"), '1010')

    def test_twelve(self):
        self.assertIn('2000', task11_20.task_12())

    def test_twelve_negative(self):
        self.assertIn('1000', task11_20.task_12())

    def test_twelve1(self):
        self.assertIn('2222', task11_20.task_12())

    def test_thourteen(self):
        self.assertEqual(task11_20.task_13("hello world! 123"), "LETTERS " + '10' + '\n' + "DIGITS " + '3')

    def test_thourteen_empty(self):
        self.assertEqual(task11_20.task_13(""), "LETTERS " + '0' + '\n' + "DIGITS " + '0')

    def test_thourteen_only_letters(self):
        self.assertEqual(task11_20.task_13("hello world!"), "LETTERS " + '10' + '\n' + "DIGITS " + '0')

    def test_thourteen_only_numbers(self):
        self.assertEqual(task11_20.task_13("122345"), "LETTERS " + '0' + '\n' + "DIGITS " + '6')

    def test_fourteen(self):
        self.assertEqual(task11_20.task_14("Hello world!"), "UPPER CASE " + '1' + '\n' + "LOWER CASE " + '9')

    def test_fourteen_empty(self):
        self.assertEqual(task11_20.task_14(""), "UPPER CASE " + '0' + '\n' + "LOWER CASE " + '0')

    def test_fourteen_only_upper(self):
        self.assertEqual(task11_20.task_14("HELLO"), "UPPER CASE " + '5' + '\n' + "LOWER CASE " + '0')

    def test_fourteen_only_lower(self):
        self.assertEqual(task11_20.task_14("hello world!"), "UPPER CASE " + '0' + '\n' + "LOWER CASE " + '10')

    def test_fifteen(self):
        self.assertEqual(task11_20.task_15(9), 11106)

    def test_fifteen_zero(self):
        self.assertEqual(task11_20.task_15(0), 0)

    def test_fifteen_negative(self):
        self.assertEqual(task11_20.task_15(-1), ValueError)

    def test_sixteen(self):
        self.assertEqual(task11_20.task_16("1,2,3,4,5,6,7,8,9"), "1, 9, 25, 49, 81")

    def test_sixteen_empty(self):
        self.assertEqual(task11_20.task_16(""), TypeError)

    def test_sixteen_only_one(self):
        self.assertEqual(task11_20.task_16("1"), '1')

    #input one valid and one invalid value
    def test_sixteen_two_values(self):
        self.assertEqual(task11_20.task_16("1,2"), '1')

    def test_eighteen(self):
        self.assertEqual(task11_20.task_18("ABd1234@1,a F1#,2w3E*,2We3345"), 'ABd1234@1')

    def test_eighteen_empty(self):
        self.assertEqual(task11_20.task_18(""), '')

    def test_eighteen_one_invalid(self):
        self.assertEqual(task11_20.task_18("2We3345"), '')











if __name__ == '__main__':
    unittest.main()
