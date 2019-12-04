import unittest
import task81_90


class Test_task_81_90(unittest.TestCase):

    def test_task_81(self):
        self.assertTrue(7 <= task81_90.task_81() <= 16)

    def test_task_82(self):
        self.assertEqual(task81_90.task_82(),
                         (b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5', b'hello world!hello world!hello world!hello world!'))

    def test_task_87(self):
        self.assertEqual(task81_90.task_87(), [5, 77, 45, 12])

    def test_task_88(self):
        self.assertEqual(task81_90.task_88(), [12, 24, 70, 88, 120, 155])

    def test_task_89(self):
        self.assertEqual(task81_90.task_89(), [24, 70, 120])

    def test_task_90(self):
        self.assertEqual(task81_90.task_90(),
                         [[[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]])



if __name__ == '__main__':
    unittest.main()
