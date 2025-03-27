def main():
    num_list = []
    user_num = input('Enter a number: ')
    
    while user_num:
        num_list.append(int(user_num))
        user_num = input('Enter a number: ')

    num_dict: dict = {}
    for x in num_list:
        if x not in num_dict:
            num_dict[x] = 1
        else:
            num_dict[x] += 1
    print(num_dict)

    for i in num_dict:
        print(f'{i} appears {num_dict[i]} times.')

if __name__ == '__main__':
    main()