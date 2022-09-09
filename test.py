import unittest

from logics import (able_to_move, get_empty_list, get_index_from_number,
                    get_number_from_index, is_zero_in_arr, move_down,
                    move_left, move_up)


class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1,2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3,3), 16)        

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        arr = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(arr), a)


    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        arr = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(arr), a)

    def test_5(self):
        a = []
        arr = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(arr), a)
    
    def test_6(self):
        self.assertEqual(get_index_from_number(7), (1,2))

    def test_7(self):
        self.assertEqual(get_index_from_number(16), (3,3))

    def test_8(self):
        self.assertEqual(get_index_from_number(1), (0,0)) 

    def test_9(self):
        a = []
        arr = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_arr(arr), False) 

    def test_10(self):
        a = []
        arr = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_arr(arr), True)

    def test_11(self):
        a = []
        arr = [
            [1, 1, 0, 1],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_arr(arr), True)

    def test_12(self):
        arr = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        res = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_left(arr), (res, 12))

    def test_13(self):
        arr = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4],
        ]
        res = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0],
        ]
        self.assertEqual(move_left(arr), (res, 32))

    def test_14(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        res = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_up(arr), (res, 24))

    def test_15(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        res = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4],
        ]
        self.assertEqual(move_down(arr), (res, 24))

    def test_16(self):
        arr = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]

        self.assertEqual(able_to_move(arr), True)
    
    def test_17(self):
        arr = [
            [2, 4, 8, 2],
            [16,32, 2, 8],
            [8, 64, 128, 4],
            [2, 256, 16, 512],
        ]

        self.assertEqual(able_to_move(arr), False)



if __name__ == "__main__":
    unittest.main()
