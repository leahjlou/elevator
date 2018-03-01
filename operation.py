import time

from models import Building
from random import randint, choice


def open_building():
    building = Building(elevators=6, floors=20)

    # randomly add people into building for simulation
    people = 11
    for person in range(0, people):
        location = randint(0, building.floor_count - 1)
        destination_options = [x for x in range(0, building.floor_count) if x != location]
        destination = choice(destination_options)

        building.add_person(location, destination)

    for person in building.people:
        building.deploy_elevator(person)
        time.sleep(.5)
