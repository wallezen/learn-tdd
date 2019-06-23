'''
Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.

@File: test_tdd_bowling_game.py
@File Created: 2019-06-17 11:30:06
@Author: judezhang (judezhang@tencent.com)
@Last Modified: 2019-06-17 11:30:26
@Modified By: judezhang (judezhang@tencent.com)
@Brief: this is a simple description...
'''

'''
- 如果每次投球都没有击倒球瓶，则得分为 0
- 如果每次投球都击倒1个球瓶，则得分为 20
- 如果投球过程中有一局“补中”， 并且紧跟着的1次投球击倒3个球瓶，其他投球都没有击倒球瓶，则得分为 16
- 如果投球过程中有一局“全中”， 并且紧跟着的2次投球分贝击倒3个和4个球瓶，其他投球都没有击倒球瓶，则得分为 24
- 如果投球过程中每局都为“全中”，第10局第二、三次投球也都击倒了10个球瓶，则得分为 300
'''
import unittest

import sys
sys.path.append("../")
from tdd_bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.__bowling_game = BowlingGame()

    def __run_many(self, cnt, pins):
        for i in range(cnt):
            self.__bowling_game.roll(pins)

    def __roll_spare(self):
        self.__bowling_game.roll(5)
        self.__bowling_game.roll(5)

    def __roll_strike(self):
        self.__bowling_game.roll(10)

    def test_all_zero(self):
        self.__run_many(20, 0)

        self.assertEqual(self.__bowling_game.score(), 0)

    def test_all_one(self):
        self.__run_many(20, 1)

        self.assertEqual(self.__bowling_game.score(), 20)

    def test_one_spare(self):
        self.__roll_spare()
        self.__bowling_game.roll(3)
        self.__run_many(17, 0)

        self.assertEqual(self.__bowling_game.score(), 16)

    def test_one_strike(self):
        self.__roll_strike()
        self.__bowling_game.roll(3)
        self.__bowling_game.roll(4)
        self.__run_many(16, 0)

        self.assertEqual(self.__bowling_game.score(), 24)

    def test_all_strike(self):
        self.__run_many(10, 10)
        self.__bowling_game.roll(10)
        self.__bowling_game.roll(10)

        self.assertEqual(self.__bowling_game.score(), 300)

    def test_other_case(self):
        self.__bowling_game.roll(1)
        self.__bowling_game.roll(4)

        self.__bowling_game.roll(4)
        self.__bowling_game.roll(5)

        self.__bowling_game.roll(6)
        self.__bowling_game.roll(4)

        self.__bowling_game.roll(5)
        self.__bowling_game.roll(5)

        self.__roll_strike()

        self.__bowling_game.roll(0)
        self.__bowling_game.roll(1)

        self.__bowling_game.roll(7)
        self.__bowling_game.roll(3)

        self.__bowling_game.roll(6)
        self.__bowling_game.roll(4)

        self.__roll_strike()

        self.__bowling_game.roll(2)
        self.__bowling_game.roll(8)
        self.__bowling_game.roll(6)

        self.assertEqual(self.__bowling_game.score(), 133)

if __name__ == "__main__":
    unittest.main()
