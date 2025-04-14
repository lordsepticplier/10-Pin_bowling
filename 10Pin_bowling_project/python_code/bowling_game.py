"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""
class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        if pins < 0 :
            #this happens if a roll is below 0 and makes it 0 by defult and says you cheated
            print( "\ncheating detected " , pins , "is lower then 0 and thus cheating so this roll will be made 0")
            self.rolls.append(0)
            self.current_roll += 1
        elif pins > 10 :
            #this happens if a roll is above 10 and makes it 0 by defult and says you cheated
            print("\ncheating detected ", pins , "is higher then 10 and thus cheating so this roll will be made 0")
            self.rolls.extend([0, 0])
            self.current_roll += 2
        else:
            #this happens if the roll is between 0 and 10 / a normal roll
            self.rolls.append(pins)
            self.current_roll += 1

    def score(self):
        """Calculate the score for the current game."""
        score = 0
        frame_index = 0

        for frame in range(10):
            #changing from 9 to 10 makes it that round 10 happens
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self._open_frame(frame_index) 
                #changed from taking the roll to taking both rolls in the open frame
                frame_index += 2
        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        return self.rolls[frame_index + 2]
    def _open_frame(self, frame_index):
        """
        Calculate the open frame

        Args:
            frame_index: Index of the first roll in the open frame

        Returns:
            The value of the open frame
        """
        return self.rolls[frame_index] + self.rolls[frame_index + 1] 
