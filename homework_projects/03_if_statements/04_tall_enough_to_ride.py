def main():
    height = input('How tall are you? ')
    while height:
        if int(height) > 49:
            print('You\'re tall enough to ride!')
            height = input('How tall are you? ')
        else:
            print('You\'re not tall enough to ride, but maybe next year!')
            height = input('How tall are you? ')
if __name__ == '__main__':
    main()