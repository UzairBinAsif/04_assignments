from random import randint as r

actual_number = r(0, 99)
def main():
    user_guess = int(input('I am thinking of a number between 0 and 99... Enter a guess: '))
    while True: 
        if user_guess == actual_number:
            print(f'Congrats! The number was: {actual_number}')
            break
        elif user_guess > actual_number:
            print('Your guess is too high')
        elif user_guess < actual_number:
            print('Your guess is too low')
        else:
            pass
        user_guess = int(input('Enter a new number: '))

if __name__ == '__main__':
    main()