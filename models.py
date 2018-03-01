class Building:
    seconds_of_operation = 28800
    elevator_count = 4
    floor_count = 20
    floors = []
    elevators = []
    people = []

    def __init__(self, elevators=None, floors=None):
        self.elevator_count = elevators if elevators else self.elevator_count
        self.floor_count = floors if floors else self.floor_count

        # associate elevators with building
        self.elevators = [Elevator(uid=x) for x in range(0, self.elevator_count)]

        # not sure it'll be needed, but saved for later
        self.floors = [num for num in range(0, self.floor_count)]

    def add_person(self, location, destination, weight=None):
        self.people.append(Person(location, destination, weight))

    def deploy_elevator(self, person):
        pass

    def find_nearest_elevator(self, location, destination):
        ideal_elevator = [rec for rec in self.elevators if rec.location == location and not rec.in_transit]
        if ideal_elevator:
            # if an ideal elevator is found, return the first result
            return ideal_elevator[0]

        # rank elevators by distance from location and sort
        by_rank = [(rec, rec.transit_distance(destination)) for rec in self.elevators]
        by_rank.sort(key=lambda rec: rec[1])

        return by_rank[0][0]


class Elevator:
    trip_count = 0
    floors_passed = 0
    location = 0
    destination = 0
    trip_limit = 100
    weight_limit = 2000

    occupied = False
    in_transit = False
    doors_open = False
    service_required = False
    track_weight = False

    def __init__(self, uid):
        self.id = uid

    def status_check(self):
        if self.trip_count > self.trip_limit:
            self.service_required = True

    def report_location(self):
        print(self.location)

    def transit_distance(self, destination):
        if self.in_transit:
            displacement = self.location - destination
            if displacement < 0:
                distance = abs(self.location - self.destination) + self.destination - destination
            else:
                distance = displacement
            return distance

        else:
            distance = abs(self.location - destination)

        return distance


class Person:
    def __init__(self, location, destination, weight=None):
        self.location = location
        self.destination = destination
        self.weight = weight if weight else None

    def call_elevator(self):
        pass
