from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []

def playing(player):

    traversal_path = []

    visited_dict = {}
    visited_set = set()
    path = Stack()

    oposite_directions = {"s": "n", "n": "s", "e": "w", "w": "e"}

    while len(visited_set) < len(room_graph):
        current = player.current_room
        visited_set.add(current)
        # path.push(current.id)
        # traversal_path.append(current)

        # if current.id not in visited_set:
        # print(current.id)
        # visited_set.add(current.id)
        visited_dict[current.id] = {}

        # if len(current.get_exits()) == 1:
        #     direction = current.get_exits()
        #     path.pop()
        #     previous_room = path.stack[-1]
        #     visited_dict[current.id][direction] = previous_room
        #     player.travel(previous_room)

        unvisited = Queue()
        for direction in current.get_exits():
            if current.get_room_in_direction(direction) not in visited_set:
                # visited_dict[current.id][direction] = False
                # unvisited.enqueue(direction)
                unvisited.enqueue(direction)

        if unvisited.size() > 0:
            # direction = unvisited.dequeue()
            direction = unvisited.dequeue()
            path.push(direction)
            traversal_path.append(direction)
            player.travel(direction)
            
        else:
            # for direction in visited_dict[current.id]:
            #     if visited_dict[current.id][direction] == False:
            #         visited_dict[current.id][direction] = player.current_room.get_room_in_direction(direction)
            #         player.travel(direction)
            previous_room = path.pop()
            traversal_path.append(oposite_directions[previous_room])
            player.travel(oposite_directions[previous_room])
            
            

    return traversal_path

traversal_path = playing(player)


# player.current_room = world.starting_room
# print(player.current_room)
# playing(player)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
