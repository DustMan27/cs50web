class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(f"Hello {self.firstname} {self.lastname}!")

class People():
    people = []
    people_count = 0

def Maker():
    firstname = input("What's your first name: ")
    lastname = input("What's your last name: ")
    new_guy = Person(firstname, lastname)
    return new_guy

# INITIALISE PEOPLE LIST
friends = People()

# PROMPT USER
print("Please create five guys.")

# RUN MAKER FUNCTION
x = 5 
while x > friends.people_count:
    friends.people.append(Maker())
    x = x - 1

for friend in friends.people:
    print(f"{friend.firstname} {friend.lastname}")
