def main():
    l1: list = [1,2,3,4,5,3,2,11,2,66,76,90]
    
    def double(l):
        doubled_l: list = []
        for i in l:
            doubled_l.append(i**2)
        return doubled_l
    
    print(double(l1))

if __name__ == '__main__':
    main()