class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __str__(self):
        return ", ".join(self.people)


party = Party()


while True:
    name = input()
    if name == "End":
        break
    party.add_person(name)


print(f"Going: {party}")
print(f"Total: {len(party.people)}")
