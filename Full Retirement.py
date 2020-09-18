def main():

    yob = int(input("Enter your year of birth: "))
    mob = int(input("Enter the month of birth: "))

    # calculates how old you are at the full retirement age
    if yob <= 1937:
        print("Your full retirement age is 65 and 0 months.")
        months = 0
        year = 65
    elif yob == 1938:
        print("Your full retirement age is 65 and 2 months.")
        months = 2
        year = 65
    elif yob == 1939:
        print("Your full retirement age is 65 and 4 months.")
        months = 4
        year = 65
    elif yob == 1940:
        print("Your full retirement age is 65 and 6 months.")
        months = 6
        year = 65
    elif yob == 1941:
        print("Your full retirement age is 65 and 8 months.")
        months = 8
        year = 65
    elif yob == 1942:
        print("Your full retirement age is 65 and 10 months.")
        months = 10
        year = 65
    elif yob == 1943:
        print("Your full retirement age is 66 and 0 months.")
        months = 0
        year = 66
    elif yob <= 1954:
        print("Your full retirement age is 66 and 0 months.")
        months = 0
        year = 66
    elif yob == 1955:
        print("Your full retirement age is 66 and 2 months.")
        months = 2
        year = 66
    elif yob == 1956:
        print("Your full retirement age is 66 and 4 months.")
        months = 4
        year = 66
    elif yob == 1957:
        print("Your full retirement age is 66 and 6 months.")
        months = 6
        year = 66
    elif yob == 1958:
        print("Your full retirement age is 66 and 8 months.")
        months = 8
        year = 66
    elif yob == 1959:
        print("Your full retirement age is 66 and 10 months.")
        months = 10
        year = 66
    elif yob >= 1960:
        print("Your full retirement age is 67 and 0 months.")
        months = 0
        year = 66

    # calculates the estimate SSA retirement age
    est_year = yob + year
    est_month = months + mob
    if est_month > 12:
        est_year = est_year + 1
        est_month = est_month - 12

    # calculating which month the SSA retirement falls on
    if est_month == 1:
        print("This will be in January of", est_year)
    elif est_month == 2:
        print("This will be in February of", est_year)
    elif est_month == 3:
        print("This will be in March of", est_year)
    elif est_month == 4:
        print("This will be in April of", est_year)
    elif est_month == 5:
        print("This will be in May of", est_year)
    elif est_month == 6:
        print("This will be in June of", est_year)
    elif est_month == 7:
        print("This will be in July of", est_year)
    elif est_month == 8:
        print("This will be in August of", est_year)
    elif est_month == 9:
        print("This will be in September of", est_year)
    elif est_month == 10:
        print("This will be in October of", est_year)
    elif est_month == 11:
        print("This will be in November of", est_year)
    elif est_month == 12:
        print("This will be in December of", est_year)


main()
