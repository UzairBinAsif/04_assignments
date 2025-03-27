def main():
    def calc_perimeter():
        l1: float = float(input('What is the length of side 1? '))
        l2: float = float(input('What is the length of side 2? '))
        l3: float = float(input('What is the length of side 3? '))
        
        return f'The perimeter of the triangle is {l1 + l2 + l3}'
    
    print(calc_perimeter())

if __name__ == '__main__':
    main()