# We have following information on countries and their population (population is in crores),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# 1. Using above create a dictionary of countries and its population
# 2. Write a program that asks user for three type of inputs,
# a. print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# b. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

country_population = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "Pakistan": 21
}


def print1():
    print("Found here")
    for key in country_population:
        print(key, "==>", country_population[key])


def add1():
    name = input("Enter a country name: ")
    if name in country_population:
        print("Exist")
    else:
        popu = input("Enter population: ")
    country_population[name] = popu
    print(country_population)


def remove1():
    name = input("Enter a country name: ")
    if name in country_population:
        country_population.pop(name)
        print(country_population)
    else:
        print("Not Found")


def query1():
    name = input("Which country you want to show: ")
    if name in country_population:
        print(country_population[name])
    else:
        print("Not Found")


def random1():
    print("Not found")


def main():
    print(country_population)
    value = input("Enter a String: ")
    value = value.lower()
    if value in country_population:
        print1()
    elif value == "add":
        add1()
    elif value == "remove":
        remove1()
    elif value == "query":
        query1()
    else:
        random1()


if __name__ == '__main__':
    main()
