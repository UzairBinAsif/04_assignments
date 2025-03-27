def get_lst():
    lst = []
    elem: str = input("Enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element of the list or press enter to stop: ")
    return lst

def main():
    l1: list = get_lst()
    
    def get_first_element(lst):
        if lst == []:
            return ""
        return lst[0]
    
    print(get_first_element(l1))

if __name__ == '__main__':
    main()