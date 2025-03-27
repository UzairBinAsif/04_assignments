def main():
    def sum_of_num(n1, n2):
        return n1 + n2

    x1 = int(input('Enter first number: '))
    x2 = int(input('Enter second number: '))
    print(f'The sum of {x1} and {x2} is:', sum_of_num(x1, x2))

if __name__ == '__main__':
    main()