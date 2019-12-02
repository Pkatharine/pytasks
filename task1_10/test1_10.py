import unittest
import task1_10

class tests_task_1_10(unittest.TestCase):

    def test_one_valid_1(self):
        self.assertIn(2030, task1_10.one())

    def test_one_valid_2(self):
        self.assertIn(3200, task1_10.one())

    def test_one_valid_3(self):
        self.assertIn(2600, task1_10.one())

    def test_zero(self):
        self.assertEqual(task1_10.two(0), 1)

    def test_positive(self):
        self.assertEqual(task1_10.two(8), 40320)

    def test_three(self):
        self.assertEqual(task1_10.three(8), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64})

    def test_three_negative(self):
        self.assertEqual(task1_10.three(-1), {})

    def test_four(self):
        expected = print(['1', '2', '3']), print(('1','2','3'))
        actual = task_1_10.four("1,2,3")
        self.assertEqual(expected, actual)

    def test_six(self):
        self.assertEqual("18,22,24", task1_10.six("100,150,180"))

    def test_six_1(self):
        self.assertEqual("18", task1_10.six('100'))

    def test_six_2(self):
        self.assertEqual(task1_10.six("100,-3"), "all values should be positive!")

    def test_seven_positive(self):
        self.assertEqual(task1_10.seven(3,5), [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] )

    def test_seven_zero(self):
        self.assertEqual(task1_10.seven(0,0), [])

    def test_seven_one_zero(self):
        self.assertEqual(task1_10.seven(0,), [])

    def test_eight_one(self):
        self.assertEqual(task1_10.eight("ok"), "ok")

    def test_eight_empty(self):
        self.assertEqual(task1_10.eight(""), "")

    def test_eight_ukrainian(self):
        self.assertEqual(task1_10.eight("автомобіль,корабель,ванна"), "автомобіль,ванна,корабель")

    def test_eight_latin(self):
        self.assertEqual(task1_10.eight("without,hello,bag,world"), "bag,hello,without,world")

    def test_eight_first_letter_equal(self):
        self.assertEqual(task1_10.eight("six,seven"), "seven,six")

    def test_nine_empty(self):
        self.assertEqual(task1_10.nine(""), "")

    def test_nine_one(self):
        self.assertEqual(task1_10.nine("ok"), "OK")

    def test_nine_alreadi_capitalized(self):
        self.assertEqual(task1_10.nine("MASHA PETRUSIAK"), "MASHA PETRUSIAK")

    def test_nine_ukrainian(self):
        self.assertEqual(task1_10.nine("автомобіль,корабель,ванна"), "АВТОМОБІЛЬ,КОРАБЕЛЬ,ВАННА")

    def test_nine_latin(self):
        self.assertEqual(task1_10.nine("Hello world Practice makes perfect"), "HELLO WORLD PRACTICE MAKES PERFECT")

    def test_ten_empty(self):
        self.assertEqual(task1_10.ten(""), "")

    def test_ten_one(self):
        self.assertEqual(task1_10.ten("ok"), "ok")

    def test_ten_duplicates(self):
        self.assertEqual(task1_10.ten("hi hi mam mam"), "hi mam")

    def test_ten_first_letter_equal(self):
        self.assertEqual(task1_10.ten("six seven"), "seven six")

    def test_ten_ukrainian(self):
        self.assertEqual(task1_10.ten("Київ Чернівці Черкаси Чернівці"), "Київ Черкаси Чернівці")

    def test_ten_latin(self):
        self.assertEqual(task1_10.ten("hello world and practice makes perfect and hello world again"), "again and hello makes perfect practice world")



if __name__ == '__main__':
    unittest.main()
