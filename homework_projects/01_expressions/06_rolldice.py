import random as r

num_of_sides = 6

def main():    
    die1 = r.randint(1, num_of_sides)
    die2 = r.randint(1, num_of_sides)
    
    total = die1 + die2
    
    print("\nFirst die:", die1)
    print("Second die:", die2)
    print("Total of both dice:", total)

if __name__ == '__main__':
    main()