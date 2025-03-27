Peturksbouipo_age : int = 16
Stanlau_age : int = 25
Mayengua_age : int = 48

def main():
    usr_age: str = int(input('How old are you? '))
    
    if usr_age >= Peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {str(Peturksbouipo_age)}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {str(Peturksbouipo_age)}.")
    
    if usr_age >= Stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {str(Stanlau_age)}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {str(Stanlau_age)}.")
    
    if usr_age >= Mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {str(Mayengua_age)}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {str(Mayengua_age)}.")

if __name__ == '__main__':
    main()