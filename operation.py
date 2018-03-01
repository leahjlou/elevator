from models import Building


def open_building():
    building = Building(elevators=6, floors=20)
    print(building.elevators)
