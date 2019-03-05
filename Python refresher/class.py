class Dog:

    dogInfo = "Hey dogs are cool!"

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("BARK!")

mydog = Dog("Fido", 13, "Brown")
mydog.bark("hehehehe")

mydog.name = "Fido"
#mydog.age = 16

print(mydog)
print(mydog.name)
print(mydog.age)

Dog.dogInfo = "Hey there"
print(Dog.dogInfo)
