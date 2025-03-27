def main():
    j = float(input('Enter temperature in Fahrenheit: '))
    # c = (f-32)*5/9
    def convertToCelsius(f):
        return round((f-32)*5.0/9.0, 2)
    
    print(f'Temperature: {j}°F = ', convertToCelsius(j), '°C', sep='')

if __name__ == '__main__':
    main()