start_phrase = "Engineering is fun. I learned to draw and used Autocad to make my"

def main():
    adj = input("Please type an adjective: ")
    noun = input("Please type a noun: ")
    verb = input("Please type a verb: ")

    print(f'{start_phrase} {adj} {noun} {verb}!')

if __name__ == '__main__':
    main()