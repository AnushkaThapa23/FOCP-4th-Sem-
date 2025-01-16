'''Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
'''

def country_capital_manager():
    countries = {}
    while True:
        country = input("Enter the name of a country (or type 'quit' to exit): ").strip().lower()
        if country == 'quit':
            break
        if country in countries:
            print(f"The capital of {country.capitalize()} is {countries[country]}.")
        else:
            capital = input(f"Enter the capital city of {country.capitalize()}: ").strip()
            countries[country] = capital
            print(f"{country.capitalize()} and its capital {capital} have been added.")

country_capital_manager()
