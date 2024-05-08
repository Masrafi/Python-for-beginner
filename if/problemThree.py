## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

name1 = input('Enter first city name: ')
name2 = input('Enter first city name: ')

if name1 in india and name2 in india:
    print("They both are in same country")
if name1 in pakistan and name2 in pakistan:
    print("They both are in same country")
if name1 in bangladesh and name2 in bangladesh:
    print("They both are in same country")
else:
    print("Not")
