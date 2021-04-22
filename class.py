class Animal:
    name = ""
    kind = "dog"
    color = ""
    value = 5000.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

dog1 = Animal()
dog1.name = "Odi"
dog1.color = "black"
dog1.kind = "Labrador"
dog1.value = 60000.00

dog2 = Animal()
dog2.name = "Jammy"
dog2.color = "Brown"
dog2.kind = "Rottweiler"
dog2.value = 25000.00

print(dog1.description())
print(dog2.description())
