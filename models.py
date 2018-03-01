class Building:
    seconds_of_operation = 28800
    elevator_count = 4
    floor_count = 20

    def __init__(self, elevators=None, floors=None):
        self.elevator_count = elevators if elevators else self.elevator_count
        self.floor_count = floors if floors else self.floor_count


class Elevator:
    trip_count = 0
    floors_passed = 0
    location = 0
    safe_trips = 100
    weight_limit = 2000

    occupied = False
    in_transit = False
    doors_open = False
    service_required = False
    track_weight = False

    def status_check(self):
        if self.trip_count > self.safe_trips:
            self.service_required = True

    def report_location(self):
        print(self.location)


class Person:
    def __init__(self, location, destination, weight=None):
        self.location = location
        self.destination = destination
        self.weight = weight if weight else None
