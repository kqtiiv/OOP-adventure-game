from room import Room
from character import Enemy
from character import Friend
from rpginfo import RPGInfo

# info and credits
spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = "Katie Wan"
RPGInfo.credits()

# config rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.set_item("cheese")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
ballroom.set_item("tie")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")
dining_hall.set_item("spoon")

garden = Room("Garden")
garden.set_description("A beautiful green space with fragrant flowers")
garden.set_item("rose")

bedroom = Room("Bedroom")
bedroom.set_description("A dark, chilly room with blacked out windows")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(bedroom, "south")
bedroom.link_room(ballroom, "north")
dining_hall.link_room(garden, "south")
garden.link_room(dining_hall, "north")

#config characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh...rghfk...brains...")
dave.set_weakness("cheese")
dave.give_items("cup")

python = Enemy("Python", "A slithering snake that speaks in python")
python.set_conversation("print('Ssssssssssssss')")
python.set_weakness("cup")
python.give_items("venom drop")

trojan = Enemy("Trojan Horse", "A seemingly friendly horsie...")
trojan.set_conversation("Hey friend! What a lovely day it is today.")
trojan.set_weakness("tie")
trojan.give_items("horseshoe")
trojan.give_items("tulip")

tom = Friend("Tom", "A lovely guy, who attempts to talk to others in english")
tom.set_conversation("This place is creepy! I'm pretty sure I saw someone in the kitchen throwing cheese out the window!")

neumann = Friend("John von Neumann", "A Hungarian and American mathematician, physicist, computer scientist, engineer and polymath - The full package!")
neumann.set_conversation("01110100 01101001 01100101 00100000 01101000 01101111 01110010 01110011 01100101")


#set character in rooms
ballroom.set_character(tom)
kitchen.set_character(dave)
dining_hall.set_character(neumann)
garden.set_character(trojan)
bedroom.set_character(python)


#config player
current_room = dining_hall

inventory = []

#game loop
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        print(f"There is {item}! To take, use the command 'take'")
    
    command = input("> ").lower()
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        combat_item = input("What item would you like to fight with: ").lower()
        if combat_item in inventory:
            battle = inhabitant.fight(combat_item)
            if type(battle) == list:
                print(f"Enemies defeated: {battle[0]}\nEnemies left: {battle[1]-battle[0]}")
            elif not battle:
                print("Restart to play again!")
                break
            else:
                print("Victory!")
                break
        else:
            print("This item is not in your inventory!")
    elif command == "steal":
        items = ", ".join(inhabitant.get_items())
        item = input("Which item would you like to steal: " + items).lower()
        rob = inhabitant.steal(item)
        if rob:
            inventory.append(item)
    elif command == "take":
        if item is not None:
            inventory.append(current_room.take_item())
            print("You put " + item + " in your inventory")
            print("Type 'view inventory' to view your items.")
        else:
            print("There is no item for you to take!")
    elif command == "view inventory":
        print("Inventory: " + ", ".join(inventory))
            
        

