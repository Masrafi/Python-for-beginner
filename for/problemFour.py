# Lets say you are running a 5 km race. Write a program that,
#
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
num = 0
for x in range(5):
    num = x
    if x == 1:
        txt = input("Are you tired: ")
        if txt == 'yes':
            print("you didn't finish the race")
            break
if num == 4:
    print("Congratulations!! You complete the race")
else:
    print("you didn't finish the race")


