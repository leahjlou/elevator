from models import Building
from random import randint, choice


def open_building():
    building = Building(elevators=6, floors=20)
    print(building.elevators)

    # randomly add people into building for simulation
    people = 11
    for person in range(0, people):
        loc = randint(0, building.floor_count - 1)
        dest_options = range(0, loc) + range(loc + 1, building.floor_count)
        dest = choice(dest_options)

        building.add_person(loc, dest)

    for person in building.people:
        print(person)
