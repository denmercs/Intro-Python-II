# Write a class to hold player information, e.g. what room they are in
# currently.


### REFACTORED ###
# class Player:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location

#     def get_name(self):
#         return self.name

#     def get_location(self):
#         return self.location

#     def set_location(self, new_location):
#         self.location = new_location

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)

        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")

    def add_item_in(self, item):
        self.inventory.append(item)
        print(f"Added {item.name} to inventory \n")

    def remove_item_in(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                print(f"you dropped {item.name}\n")
                return item
            else:
                return None

    def list_inventory(self):
        if self.inventory == []:
            print("Invetory: Empty\n")
        else:
            inventory = ", ".join([item.name for item in self.inventory])
            print(f"Inventory: {inventory}\n")

    def item_locate(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
            else:
                return None
