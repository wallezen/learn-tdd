'''
Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.

@File: tradional_bowling_game.py
@File Created: 2019-06-17 11:11:38
@Author: judezhang (judezhang@tencent.com)
@Last Modified: 2019-06-17 11:11:44
@Modified By: judezhang (judezhang@tencent.com)
@Brief: this is a simple description...
'''

class BowlingGame:
    def __init__(self):
        self.rolls = [0] * 21
        self.curr_roll = 0
        self.score = 0

    def roll(self, pins):
        self.rolls[self.curr_roll] = pins
        self.curr_roll += 1

    def score(self):
        for frame_idx in range(10):
            self.score += self.rolls[frame_idx] + self.rolls[frame_idx + 1]

        retrun self.score
