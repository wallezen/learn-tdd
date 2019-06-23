

class BowlingGame:
    def __init__(self):
        self.__score = 0
        self.__rolls = [0] * 21
        self.__currRoll = 0

    def __is_spare_frame(self, roll_idx):
        return self.__rolls[roll_idx] + self.__rolls[roll_idx + 1] == 10

    def __is_strike_frame(self, roll_idx):
        return self.__rolls[roll_idx] == 10

    def __bonus_of_roll_spare(self, roll_idx):
        return self.__rolls[roll_idx + 2]

    def __bonus_of_roll_strike(self, roll_idx):
        return self.__rolls[roll_idx + 1] + self.__rolls[roll_idx + 2]

    def roll(self, pins):
        self.__rolls[self.__currRoll] = pins
        self.__currRoll += 1

    def score(self):
        roll_idx = 0
        for frame_idx in range(10):
            if self.__is_strike_frame(roll_idx):
                self.__score += 10 + self.__bonus_of_roll_strike(roll_idx)
                roll_idx += 1
            elif self.__is_spare_frame(roll_idx):
                self.__score += 10 + self.__bonus_of_roll_spare(roll_idx)
                roll_idx += 2
            else:
                self.__score += self.__rolls[roll_idx] + self.__rolls[roll_idx + 1]
                roll_idx += 2


        return self.__score
