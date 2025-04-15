"""
more in depth usage of the Bowling Game

This file shows the tests in more depth being that it
1. makes a game
2. Rolls the balls
3. Calculates and displays the score

For each game, I show:
- The rolls in each frame
- The expected score based on standard bowling rules
- The actual score calculated by our implementation

Note: I have made this appart of my testing but have done major changes so I hope that is ok
"""

from bowling_game import BowlingGame


def print_game_results(game_name, rolls, expected_score, actual_score):
    """Print the results of a game, showing expected vs actual score."""
    print(f"\n{game_name}:")
    print(f"Rolls: {rolls}")
    print(f"Expected score: {expected_score}")
    print(f"Actual score: {actual_score}")
    print(f"Correct implementation: {'✓' if expected_score == actual_score else '✗'}")


def example_game():
    """
    Play a sample game with strikes, spares and open frames.

    Frames and scoring:
    Frame 1: 10 (Strike)         | 10 + 3 + 6 = 19
    Frame 2: 3, 6                | 9
    Frame 3: 5, 5 (Spare)        | 10 + 8 = 18
    Frame 4: 8, 1                | 9
    Frame 5: 10 (Strike)         | 10 + 10 + 10 = 30
    Frame 6: 10 (Strike)         | 10 + 10 + 9 = 29
    Frame 7: 10 (Strike)         | 10 + 9 + 0 = 19
    Frame 8: 9, 0                | 9
    Frame 9: 7, 3 (Spare)        | 10 + 10 = 20
    Frame 10: 10, 10, 8          | 28

    Total expected score: 190
    """
    game = BowlingGame()
    #this has all the rolls in it the space is to seperate the rounds
    rolls = [10,   3, 6,   5, 5,   8, 1,   10,   10,   10,   9, 0,   7, 3,   10, 10, 8]

    #this puts all the rolls in the game
    for pins in rolls:
        game.roll(pins)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 190

    print_game_results("Example Game", rolls, expected_score, actual_score)
    return actual_score

def regular_game():
    """
    Play a regular game with no strikes or spares.

    Frames and scoring:
    Frame 1: 3, 4  | 7
    Frame 2: 2, 5  | 7
    Frame 3: 1, 6  | 7
    Frame 4: 4, 2  | 6
    Frame 5: 8, 1  | 9
    Frame 6: 7, 1  | 8
    Frame 7: 5, 3  | 8
    Frame 8: 2, 3  | 5
    Frame 9: 4, 3  | 7
    Frame 10: 2, 6 | 8

    Total expected score: 72
    """
    game = BowlingGame()
    #this has all the rolls in it the space is to seperate the rounds
    rolls = [3, 4,   2, 5,   1, 6,   4, 2,   8, 1,   7, 1,   5, 3,   2, 3,   4, 3,   2, 6]

    #this puts all the rolls in the game
    for pins in rolls:
        game.roll(pins)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 72

    print_game_results("Regular Game", rolls, expected_score, actual_score)
    return actual_score

def normal_game():
    """
    Play a normal game with strikes, spares and open frames.

    Frames and scoring:
    Frame 1: 8, 1                | 9
    Frame 2: 6, 4 (Spare)        | 10 + 5 = 15
    Frame 3: 5, 2                | 7
    Frame 4: 10 (Strike)         | 10 + 7 + 3 = 20
    Frame 5: 7, 3 (Spare)        | 10 + 0 = 10
    Frame 6: 0, 7                | 7
    Frame 7: 7, 2                | 9
    Frame 8: 10 (Strike)         | 10 + 9 + 0 = 19
    Frame 9: 9, 0                | 9
    Frame 10: 7, 3, 7            | 17

    Total expected score: 122
    """
    game = BowlingGame()
    #this has all the rolls in it the space is to seperate the rounds
    rolls = [8, 1,   6, 4,   5, 2,   10,   7, 3,   0, 7,   7, 2,   10,   9, 0,   7, 3, 7]

    #this puts all the rolls in the game
    for pins in rolls:
        game.roll(pins)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 122

    print_game_results("normal Game", rolls, expected_score, actual_score)
    return actual_score

def all_spares():
    """
    Play a game with all spares and 10 at the end

    Frames and scoring:
    Frame 1: 0, 10 (Spare) | 10 + 1 = 11
    Frame 2: 1, 9 (Spare)  | 10 + 2 = 12
    Frame 3: 2, 8 (Spare)  | 10 + 3 = 13
    Frame 4: 3, 7 (Spare)  | 10 + 4 = 14
    Frame 5: 4, 6 (Spare)  | 10 + 5 = 15
    Frame 6: 5, 5 (Spare)  | 10 + 6 = 16
    Frame 7: 6, 4 (Spare)  | 10 + 7 = 17
    Frame 8: 7, 3 (Spare)  | 10 + 8 = 18
    Frame 9: 8, 2 (Spare)  | 10 + 9 = 19
    Frame 10: 9, 1, 10      | 20

    Total expected score: 155
    """
    game = BowlingGame()
    #this has all the rolls in it the space is to seperate the rounds
    rolls = [0, 10,   1, 9,   2, 8,   3, 7,   4, 6,   5, 5,   6, 4,   7, 3,   8, 2,   9, 1, 10]

    #this puts all the rolls in the game
    for pins in rolls:
        game.roll(pins)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 155

    print_game_results("All Spares Game", rolls, expected_score, actual_score)
    return actual_score

def all_strikes():
    """
    Play a perfect game (all strikes).

    Frames and scoring:
    Frame 1: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 2: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 3: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 4: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 5: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 6: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 7: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 8: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 9: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 10: 10, 10, 10  | 30

    Total expected score: 300
    """
    game = BowlingGame()
    rolls = []

    # Roll 12 strikes (10 frames + 2 bonus rolls)
    for _ in range(12):
        game.roll(10)
        rolls.append(10)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 300

    print_game_results("All Strikes", rolls, expected_score, actual_score)
    return actual_score

def all_missed():
    """
    Play a game with all missed balls (0 pins).

    Expected score: 0
    """
    game = BowlingGame()
    rolls = []

    # Roll 20 missed balls (0 pins)
    for _ in range(20):
        game.roll(0)
        rolls.append(0)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 0

    print_game_results("All Missed", rolls, expected_score, actual_score)
    return actual_score

def negitive_game():
    """
    Play a game with fisrt bowl being -1 rest missed balls (0 pins).

    Expected score: 0
    """
    game = BowlingGame()
    rolls = []
    # Roll 1 get -1/cheating/invalid
    game.roll(-1)
    rolls.append(-1)
    # Roll 20 missed balls (0 pins)
    for _ in range(19):
        game.roll(0)
        rolls.append(0)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 0

    print_game_results("Negitive Game", rolls, expected_score, actual_score)
    return actual_score

def bowls_11_game():
    """
    Play a game where first bowl is 11 and the rest are strikes(10 pins).
    Frames and scoring:
    Frame 1: 11 (Strike)  | 0
    Frame 2: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 3: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 4: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 5: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 6: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 7: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 8: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 9: 10 (Strike)  | 10 + 10 + 10 = 30
    Frame 10: 10, 10, 10  | 30

    Total expected score: 270
    """
    game = BowlingGame()
    rolls = []
    # Roll 1 get 11/cheating/invalid
    game.roll(11)
    rolls.append(11)
    # Roll 11 strikes(10 pins)
    for _ in range(11):
        game.roll(10)
        rolls.append(10)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 270

    print_game_results("Bowls 11 Game", rolls, expected_score, actual_score)
    return actual_score

def more_than_10_game():
    """
    Play a game with fisrt bowl being 9 then 4 then the rest missed balls (0 pins).

    Frames and scoring:
    Frame 1: 9, 4  | 9
    Frames 2-10: 0 | 0
    Expected score: 9
    """
    game = BowlingGame()
    rolls = []
    # Roll 9 and then a 4/cheating/invalid
    game.roll(9)
    game.roll(4)
    rolls.extend([9, 4])
    # Roll 18 missed (0 pins)
    for _ in range(18):
        game.roll(0)
        rolls.append(0)

    # Calculate the final score
    actual_score = game.score()
    expected_score = 9

    print_game_results("More Then 10 Game", rolls, expected_score, actual_score)
    return actual_score

def bowls_3_times_without_bonus_game():
    """
    Play a game with fisrt bowl being 9 then 4 then the rest missed balls (0 pins).

    Frames and scoring:
    Frames 1-9: 0     | 0
    Frame 10: 3, 3, 3 | 6
    Expected score: 6
    """
    game = BowlingGame()
    rolls = []
    # Roll 18 missed (0 pins)
    for _ in range(18):
        game.roll(0)
        rolls.append(0)    
    # Roll 3 and then a 3 and then a 3/cheating/invalid
    game.roll(3)
    game.roll(3)
    game.roll(3)
    rolls.extend([3, 3, 3])


    # Calculate the final score
    actual_score = game.score()
    expected_score = 6

    print_game_results("Bowls 3 Times Without Bonus Game", rolls, expected_score, actual_score)
    return actual_score

def main():
    """Run all example games and print a summary."""
    print("BOWLING GAME EXAMPLES")
    print("=====================")
    print("These examples demonstrate how bowling scoring should work.")
    print("The 'Correct implementation' indicator shows if our current")
    print("implementation calculates the score correctly.")
    print("\nStudents should ensure their fixed implementation correctly")
    print("calculates all of these scenarios.")

    example_game()
    regular_game()  
    normal_game()
    all_spares()
    all_strikes()
    all_missed()
    negitive_game()
    bowls_11_game()
    more_than_10_game()
    bowls_3_times_without_bonus_game()
    

if __name__ == "__main__":
    main()
