# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.
#
# emp = Employee(1, "coder")

class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"My id: {self.id}. My name is: {self.name}")


em = Employee("1", "Masrafi")
em.display()