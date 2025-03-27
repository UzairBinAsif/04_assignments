def main():
    m: float = float(input('Enter mass in kg: '))
    c: int = 299792458
    e = m * c**2
    print(f'''e = m * C^2
m = {m} kg
C = 299792458 m/s
\n{e} joules of energy!''')

if __name__ == '__main__':
    main()