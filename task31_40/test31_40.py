import unittest
import task31_40


class Test_task_31_40(unittest.TestCase):

    def test_task_31_first_more(self):
        self.assertEqual(task31_40.task_31("hello","my"), 'hello')

    def test_task_31_second_more(self):
        self.assertEqual(task31_40.task_31("hi","world"), 'world')

    def test_task_31_two_equal(self):
        self.assertEqual(task31_40.task_31("hello","world"), 'hello'+'\n'+'world')

    def test_task_31_one_empty(self):
        self.assertEqual(task31_40.task_31("hello",""), 'hello')

    def test_task_31_all_empty(self):
        self.assertEqual(task31_40.task_31("",""), ''+'\n'+'')

    def test_task_32_even(self):
        self.assertEqual(task31_40.task_32(4), "It is an even number")

    def test_task_32_odd(self):
        self.assertEqual(task31_40.task_32(9), "It is an odd number")

    def test_task_32_zero(self):
        self.assertEqual(task31_40.task_32(0), "It is an even number")

    def test_task_32_empty(self):
        self.assertEqual(task31_40.task_32(), TypeError)

    def test_task_32_negative_even(self):
        self.assertEqual(task31_40.task_32(-4), "It is an even number")

    def test_task_32_negative_odd(self):
        self.assertEqual(task31_40.task_32(-9), "It is an odd number")

    def test_task_33(self):
        self.assertEqual(task31_40.task_33(3), {1: 1, 2: 4, 3: 9})

    def test_task_33_empty(self):
        self.assertEqual(task31_40.task_33(), ValueError)

    def test_task_33_negative(self):
        self.assertEqual(task31_40.task_33(-2), {})

    def test_task_33_zero(self):
        self.assertEqual(task31_40.task_33(0), {})

    def test_task_34(self):
        self.assertEqual(task31_40.task_34(3), {1: 1, 2: 4, 3: 9})

    def test_task_34_empty(self):
        self.assertEqual(task31_40.task_34(), ValueError)

    def test_task_34_negative(self):
        self.assertEqual(task31_40.task_34(-2), {})

    def test_task_34_zero(self):
        self.assertEqual(task31_40.task_34(0), {})

    def test_task_35(self):
        self.assertEqual(task31_40.task_35(3), 'dict_values([1, 4, 9])')

    def test_task_35_empty(self):
        self.assertEqual(task31_40.task_35(), ValueError)

    def test_task_35_negative(self):
        self.assertEqual(task31_40.task_35(-3), 'dict_values([])')

    def test_task_35_zero(self):
        self.assertEqual(task31_40.task_35(0), 'dict_values([])')

    def test_task_36(self):
        self.assertEqual(task31_40.task_36(3), 'dict_keys([1, 2, 3])')

    def test_task_36_empty(self):
        self.assertEqual(task31_40.task_36(), ValueError)

    def test_task_36_negative(self):
        self.assertEqual(task31_40.task_36(-3), 'dict_keys([])')

    def test_task_36_zero(self):
        self.assertEqual(task31_40.task_36(0), 'dict_keys([])')

    def test_task_37(self):
        self.assertEqual(task31_40.task_37(3), [1, 4, 9])

    def test_task_37_empty(self):
        self.assertEqual(task31_40.task_37(), ValueError)

    def test_task_37_negative(self):
        self.assertEqual(task31_40.task_37(-3), [])

    def test_task_37_zero(self):
        self.assertEqual(task31_40.task_37(0), [])

    def test_task_38(self):
        self.assertEqual(task31_40.task_38(20), [1, 4, 9, 16, 25])

    def test_task_38_empty(self):
        self.assertEqual(task31_40.task_38(), ValueError)

    def test_task_38_negative(self):
        self.assertEqual(task31_40.task_38(-3), [])

    def test_task_38_zero(self):
        self.assertEqual(task31_40.task_38(0), [])

    def test_task_39(self):
        self.assertEqual(task31_40.task_39(20), [256, 289, 324, 361, 400])

    def test_task_39_empty(self):
        self.assertEqual(task31_40.task_39(), ValueError)

    def test_task_39_negative(self):
        self.assertEqual(task31_40.task_39(-3), [])

    def test_task_39_zero(self):
        self.assertEqual(task31_40.task_39(0), [])

    def test_task_40(self):
        self.assertEqual(task31_40.task_40(20), [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])

    def test_task_40_empty(self):
        self.assertEqual(task31_40.task_40(), ValueError)

    def test_task_40_negative(self):
        self.assertEqual(task31_40.task_40(-3), [])

    def test_task_40_zero(self):
        self.assertEqual(task31_40.task_40(0), [])





if __name__ == '__main__':
    unittest.main()
