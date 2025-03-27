import random

num_of_sides = 6

def roll_dice():
    die1 = random.randint(1, num_of_sides)
    die2 = random.randint(1, num_of_sides)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    die1 = 10
    print("die1 starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 is now: " + str(die1))

if __name__ == '__main__':
    main()