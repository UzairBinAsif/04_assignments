MAX_LENGTH: int = 3

def shorten(lst: list):
    while len(lst) > MAX_LENGTH:
        last_elem: list = lst.pop()
        print(last_elem)

def get_lst():
    lst = []
    elem: str = input("Enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element of the list or press enter to stop: ")
    return lst

def main():
    list1: list = get_lst()
    shorten(list1)

if __name__ == '__main__':
    main()