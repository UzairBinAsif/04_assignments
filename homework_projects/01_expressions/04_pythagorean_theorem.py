import math as m

def main():
    AB = float(input('Enter the length of AB: '))
    AC = float(input('Enter the length of AC: '))
    BC = m.sqrt((AB ** 2) + ( AC ** 2))
    print(f'The length of BC (the hypotenuse) is: {BC}')

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()