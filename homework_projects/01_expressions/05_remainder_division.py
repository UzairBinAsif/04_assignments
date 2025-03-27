def main():
    x = float(input('Please enter an integer to be divided: '))
    y = float(input('Please enter an integer to divide by: '))
    print(f'The result of this division is {x//y} with a remainder of {x%y}')

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()