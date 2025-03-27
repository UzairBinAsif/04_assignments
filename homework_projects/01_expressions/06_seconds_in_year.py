days_per_year = 365
hours_per_day = 24
min_per_hour = 60
sec_per_min = 60

def main():
    sec_per_year = days_per_year * hours_per_day * min_per_hour * sec_per_min
    print(f'There are {sec_per_year} seconds in a year!')

if __name__ == '__main__':
    main()