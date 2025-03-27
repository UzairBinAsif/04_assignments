def main():
    feet = float(input('Enter value in feet: '))
    inch = 12 * feet
    print(f'{feet} ft = {inch:.2f} in')


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()