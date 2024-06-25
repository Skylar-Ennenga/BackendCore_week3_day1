# Object Oriented Programming

# classes - Blueprint for an object. Defines the structure and behavior of objects that are derived from that class.


# objects - A specific instance of a class, that adheres to the structure and behavior that are defined by the class
# objects == instance of a class

# defining a class
# class ClassName - PasqualCase
class Car:
    # constructor - run everytime we instantiate an object from a class
    # responsible for assigning class variables to their values
    # initializes the data attributes of an object
    def __init__(self, motor, piston, tires, super_cool_sticker ): #init will always take in self as a paramter
        # self refer to the object created from the class
        # setting class attributes to parameters
        # object.attribute = the argument that fulfills the paramter when we instantiate an class object
        # attribute == class variable - variable within a class
        self.motor = motor
        self.piston = piston
        self.tires = tires
        self.super_cool_sticker = super_cool_sticker
        # because the init gets called on every instantiation of a class
        # we can call other functions in the init
        print("We're creating a car")

# instantiating an object from a class (creating an instance of class)
# we create a variable name to hold our object
# set variable name equal to the class name
# add arguments to instantiate the class variables
mazda = Car("4 cylinder", 10, 4, "I love my Chinese Crested")

# access an object through the variable name
# object location in memory
print(mazda) #object and location
print(type(mazda)) # the class its derived from

# accessing information from our class
print(mazda.motor)
print(mazda.piston)
print(mazda.tires)
print(mazda.super_cool_sticker)

# create a class for an RPG character (or whatever youd like if youre not a nerd)
# give the class attributes
# instatiate 2 objects from the class
# print out the attributes for each of your objects


class Character:

    def __init__ (self, name, height, characterist, superpower):
        self.name = name
        self.height = height
        self.characterist = characterist
        self.superpower = superpower

matilda = Character( "Matilda", 5, 'super_friendly', 'physique')
bob = Character("Bob the Builder", 3, "super helpful","build fast while teaching")
print(matilda.superpower)
print(matilda.name)
print(bob.superpower)
print(bob.characterist)


class Characters:
    
    def __init__(self, sugar, spice, everythingnice):
        self.sugar = sugar
        self.spice = spice
        self.everythingnice = everythingnice

    def print_info(self):
        print(self.sugar, self.spice, self.everythingnice)
   


powderpuff = Characters("sugar", "cinnamon", ["puppies", "kittens", "hearts", "smooches"])
print(powderpuff)
print(powderpuff.everythingnice)
# Objects from a class are all unqique from other objects
blossom = Characters("sugar", "lavender", ["flowers", "butterflies"])
bubbles = Characters("sugar", "paprika", ["puppies", "kittens"])
buttercup = Characters("sugar", "salt", ["bear cubs", "light wrestling"])

print(blossom.spice)
print(bubbles.spice)
print(buttercup.spice)

# __dict__ - turns our class objects into a dictionary
blossom_dict = blossom.__dict__
for attribute, value in blossom_dict.items():
    print(attribute, value)



class Character:
# create a class for an RPG character (or whatever youd like if youre not a nerd)
# give the class attributes
# instatiate 2 objects from the class
# print out the attributes for each of your objects
    def __init__(self, class_name, weapon, spell, chest, hp, mana):
        
        self.class_name = class_name
        self.weapon = weapon
        self.spell = spell
        self.chest = chest
        self.hp = hp
        self.mana = mana

paladin = Character("Paladin", "Mace", "Heal", "Cloak of Wisdom", 100, 50)
thief = Character("Thief", "Dagger", "Shadowstep", "Cloak of Invisibilitty", 80, 30)

print(f"That {paladin.class_name} class starts with a {paladin.weapon} weapon, a {paladin.spell} spell, the {paladin.chest}, and has {paladin.hp} health, {paladin.mana} mana. ")
print(f"That {thief.class_name} class starts with a {thief.weapon} weapon, a {thief.spell} spell, the {thief.chest}, and has {thief.hp} health, {thief.mana} mana. ")


# class methods == functions within a class
# can interact with attributes from the class changing them with each call
# manage the state of each of our objects
# displaying information about the class

# creating an rpg character with methods that update the classes attributes
class Character:

    def __init__(self, class_name, strength, dexterity, constitution, wisdom, intelligence, charisma):
        # attributes - class variables
        self.class_name = class_name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

class Character:

    def __init__(self, class_name, strength, dexterity, constitution, wisdom, intelligence, charisma):
        # attributes - class variables
        self.class_name = class_name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    # class methods with live here
    def attack(self):
        print(f"{self.class_name} makes an attack")

    def move(self, distance): #class method that takes an arugment that isn't an attribute
        print(f"{self.class_name} moves a distance of {distance}")

    def level_up(self):
        values = 0,1
        # self.attribute = however we're altering the class attribute
        self.strength += random.choice(values)
        print(f"Strength is now {self.strength}")
        self.dexterity += random.choice(values)
        print(f"Dexterity is now {self.dexterity}")
        self.constitution += random.choice(values)
        print(f"Constitution is now {self.constitution}")
        self.wisdom += random.choice(values)
        print(f"Wisdom is now {self.wisdom}")
        self.intelligence += random.choice(values)
        print(f"Intelligence is now {self.intelligence}")
        self.charisma += random.choice(values)
        print(f"Charisma is now {self.charisma}")

    # def defend(): all class methods need self as an argument - lest you get a TypeErro for 0 positional arguments
        # print("You are now defending")

character = Character("Paladin", 11, 7, 15, 12, 13, 10)
# accessing class attributes
print(character.class_name)
print(character.strength)

# call class methods
character.attack()

# calling class method with an argument
character.move("25 ft")
# class method that alters our attributes
character.level_up()

# building on your previously made class
# create 3 methods
# 1.  for displaying information about the object 
#       or simply references an attribute within the method like attack method above
# 2. method that takes in an extra argument other tha self
# 3. method that alters an already existing attribute in your class
import random
class Character:
# create a class for an RPG character (or whatever youd like if youre not a nerd)
# give the class attributes
# instatiate 2 objects from the class
# print out the attributes for each of your objects
    def __init__(self, class_name, inventory, hp, mana):
        
        self.class_name = class_name
        self.inventory = inventory
        self.hp = hp
        self.mana = mana
    
    
    def item_pick_up(self, item):
        items = self.inventory.append(item)
        print(f"You have pickedup {item}")
        pass
    
    def level_up(self):
        hp_level = [7, 13]
        mana_level = [2, 8]
        hp_gain = random.choice(hp_level)
        mana_gain = random.choice(mana_level)
        self.hp += hp_gain
        print(f"You have gained {hp_gain} health and you now have {self.hp}")
        self.mana += mana_gain
        print(f"You have gained {mana_gain} mana and you now have {self.mana}")
    
    def view_inventory(self):
        for item in self.inventory:
            print(f"{item}~ ", end="")


paladin = Character("Paladin", ["Mace", "Heal", "Cloak of Wisdom"], 100, 50)
thief = Character("Thief", ["Dagger", "Shadowstep", "Cloak of Invisibilitty"], 80, 30)

print(f"That {paladin.class_name} class starts with a {paladin.inventory[0]} weapon, a {paladin.inventory[1]} spell, the {paladin.inventory[2]}, and has {paladin.hp} health, {paladin.mana} mana. ")
print(f"That {thief.class_name} class starts with a {thief.inventory[0]} weapon, a {thief.inventory[1]} spell, the {thief.inventory[2]}, and has {thief.hp} health, {thief.mana} mana. ")

paladin.item_pick_up('Cheese wheel')
thief.item_pick_up("Diamond")

paladin.level_up()
thief.level_up()

paladin.view_inventory()
thief.view_inventory()


class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds.")
    # getter - encapsulates attributes from a class to the class
    # and we can only access those attributes through methods of the class objects, or children class objects
    def get_balance(self):
        return self._balance

account = BankAccount("12345")
account.deposit(1000)
account.withdraw(500)
print("Current balance:", account.get_balance())

# Modularization - separating functionality into separate files
# separates concerns and organize our code into "categories" 


class Character:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
        # manage instances of an Item class
        self.inventory = []

    def add_item(self):
        item_name = input("What are you adding to your inventory? ")
        damage = input("How powerful is that item? ")
        item = Item(item_name, damage)
        self.inventory.append(item)
##
##
class Item:
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
class CharacterManager:
    def __init__(self):
        self.characters = []

    # method to add character object to self.characters

    # method to display information about character objects in the list






