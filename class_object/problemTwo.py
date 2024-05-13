# Use del property to first delete id attribute and then the entire object
import problemOne

em = problemOne.Employee("1", "Masrafi")
em.display()

print(em.id)
del em.id
try:
    print(em.id)
except:
    print("ID not found")

print(em.name)
del em.name
try:
    print(em.name)
except:
    print("Name not found")
