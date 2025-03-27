def main():
    user_year = int(input('Enter an year to check: '))
    
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print('That\'s a leap year!')
            else:
                print('That\'s not a leap year!')
        else:
            print('That\'s a leap year!')    
    else:
        print('That\'s not a leap year!')

if __name__ == '__main__':
    main()