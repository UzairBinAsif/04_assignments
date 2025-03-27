def main():
    x: int = int(input('The first even number is: '))
    if x%2 == 0:
        pass
    else:
        x += 1
    for i in range(x, x+40, 2):
        print(f'{i} ', end='')


if __name__ == '__main__':
    main()