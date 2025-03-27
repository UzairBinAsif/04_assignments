def get_lst():
    lst = []
    value: str = input("Enter a value: ")
    while value != "":
        lst.append(value)
        value = input("Enter a value: ")
    return f'Here\'s the list: {lst}'

def main():    
    print(get_lst())

if __name__ == '__main__':
    main()