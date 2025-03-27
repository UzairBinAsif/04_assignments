def main():
    l1: list = [1,2,3,4,5,3,2,11,2,66,76,90]
    
    def adds(l):
        sum = 0
        for i in l:
            sum += i
        return sum
    print(adds(l1))

if __name__ == '__main__':
    main()