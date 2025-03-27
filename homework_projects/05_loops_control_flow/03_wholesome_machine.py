def main():
    prompt = input('Please type the following affirmation: I am capable of doing anything I put my mind to.')
    while True:
        if prompt == 'I am capable of doing anything I put my mind to.':
            print('That\'s right! :)')
            break
        else:
            prompt = input('Please type the following affirmation: I am capable of doing anything I put my mind to.')
            

if __name__ == '__main__':
    main()