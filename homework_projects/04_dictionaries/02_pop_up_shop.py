def main():
    fruits = {
        "apple": 12,
        "durian": 3,
        "jackfruit": 9,
        "kiwi": 22,
        "rambutan": 17,
        "mango": 8
    }
    total = 0
    for i in fruits:
        user_choice = int(input(f'How many ({i}) do you want?: '))
        total += user_choice * fruits[i]
    print(f'Your total is ${total}')
        
if __name__ == '__main__':
    main()