# Further expand you character class
# Create a class to manage your characters
# give that class the option to add a character
# and display each character

# # Create a new attribute on your 
# import random
# class Character:
# # create a class for an RPG character (or whatever youd like if youre not a nerd)
# # give the class attributes
# # instatiate 2 objects from the class
# # print out the attributes for each of your objects
#     def __init__(self, class_name, inventory, hp, mana):
        
#         self.class_name = class_name
#         self.inventory = inventory
#         self.hp = hp
#         self.mana = mana
    
    
#     def item_pick_up(self, item):
#         items = self.inventory.append(item)
#         print(f"You have pickedup {item}")
#         pass
    
#     def level_up(self):
#         hp_level = [7, 13]
#         mana_level = [2, 8]
#         hp_gain = random.choice(hp_level)
#         mana_gain = random.choice(mana_level)
#         self.hp += hp_gain
#         print(f"You have gained {hp_gain} health and you now have {self.hp}")
#         self.mana += mana_gain
#         print(f"You have gained {mana_gain} mana and you now have {self.mana}")
    
#     def view_inventory(self):
#         for item in self.inventory:
#             print(f"{item}~ ", end="")
    
#     def characters_active(self):
        

# paladin = Character("Paladin", ["Mace", "Heal", "Cloak of Wisdom"], 100, 50)
# thief = Character("Thief", ["Dagger", "Shadowstep", "Cloak of Invisibilitty"], 80, 30)
# witch = Character("Witch", ["Wand", "Evil Laugh", "Magic Potion"], 70, 65)
# archer = Character("Archer", ["Bow", "Snipe", "Silet Boots"], 90, 20)

# print(f"That {paladin.class_name} class starts with a {paladin.inventory[0]} weapon, a {paladin.inventory[1]} spell, the {paladin.inventory[2]}, and has {paladin.hp} health, {paladin.mana} mana. ")
# print(f"That {thief.class_name} class starts with a {thief.inventory[0]} weapon, a {thief.inventory[1]} spell, the {thief.inventory[2]}, and has {thief.hp} health, {thief.mana} mana. ")

# paladin.item_pick_up('Cheese wheel')
# thief.item_pick_up("Diamond")

# paladin.level_up()
# thief.level_up()

# paladin.view_inventory()
# thief.view_inventory()






class dnd:
    
    def __init__(self):
        charavt

        # What if we make the paladin attack a rabbit and if it kills the rabbit it calls that level up method
        # and levels up
        # sounds awesome, dont know how to do that yet lol
        # what are our main classes? not like "thief" but like class character_creation or whatever
        
        # we could give it an attack stat then if attack is greater then 
        # active_characters
        # classes should be predefined
        #choose_class
        #manage_party
        #level_up 
        #attack_rabbit
        
        
# class Character:
#     def __init__(self, name, class_name):
#         self.name = name
#         self.class_name = class_name
#         # manage instances of an Item class
#         self.inventory = []

#     def add_item(self):
#         item_name = input("What are you adding to your inventory? ")
#         damage = input("How powerful is that item? ")
#         item = Item(item_name, damage)
#         self.inventory.append(item)

# class Item:
    
#     def __init__(self, name, damage):
#         self.name = name
#         self.damage = damage
        

# class CharacterManager:
#     def __init__(self):
#         self.characters = []

#     # method to add character object to self.characters

#     # method to display information about character objects in the list

class party:
    
    def characters(self, witch, paladin):
        self.thief = thief 
        self.paladin = paladin 
        self.witch = witch 

thief = ("dagger", "Potion of Invisibility", "Shadow-step")

print(self.thief)
print(thief.witch)

# I think were we are going wrong is by trying to jam too much into each class rather than modulizing it more

# IE 
# class Character:
#   def inventory(self, weapon, potion, apparel)

#   def stats(hp, mana, stamina) etc


# essentially

# yeah pretty much
#So have a class for the character calling different methods that create our character 
# then do a class that has them do stuff ie pick up item, level up, kill all the rabbits
# i this instance based on the class is the damage of the attack and what potion your throwing
# I was just ready to build a whole game
# class Action:
# fr, whats hard about oop is how you have to think about it
#its like your building it with no regard to the user, Like no matter what they do this is what my program is doing haha where s ive been taking input and tweaking my code to adapt with the user input


#  def attack(self, class)
# yeah i think we were just overthinking and were very hopeful about what we could get done in 15 mins


# def throw_potion(self, class)