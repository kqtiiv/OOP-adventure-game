class Character():
    enemies_defeated = 0
    win_condition = 0

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.items = []

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def get_items(self):
        return self.items
    
    def give_items(self, item):
        self.items.append(item)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.status = "alive"
        Character.win_condition += 1

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            self.status = "unconscious"
            Character.enemies_defeated += 1
            if Character.enemies_defeated == Character.win_condition:
                return True
            else:
                return [Character.enemies_defeated, Character.win_condition]
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    
    def steal(self, item):
        if self.status == "alive":
            print("Cannot steal from an awake enemy")
            return False
        elif len(self.items) == 0:
            print("No item to steal!")
            return False
        elif item in self.items:
            print("Successfully stolen " + item)
            return True
        else:
            print("Failed to steal item")
            return False
        
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)



