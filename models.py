import time


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
        elevator = self.find_nearest_elevator(person.location, person.destination)
        elevator.queue_trip(person.destination)

    def find_nearest_elevator(self, location, destination):
        ideal_elevator = [rec for rec in self.elevators if
                          rec.location == location and not rec.in_transit and not rec.service_required]
        if ideal_elevator:
            # if an ideal elevator is found, return the first result
            return ideal_elevator[0]

        # rank elevators by distance from location and sort
        by_rank = [(rec, rec.transit_distance(destination)) for rec in self.elevators if not rec.service_required]
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

    floor_queue = []
    trip_queue = []

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

    def queue_trip(self, destination):
        init_floor = self.destination if self.in_transit else self.location
        self.trip_queue.append([x for x in range(init_floor, destination)])
        self.floor_queue.extend([x for x in range(init_floor, destination)])

    def deploy(self):
        self.destination = self.trip_queue[self.trip_count][:-1]
        self.in_transit = True
        
        for floor in self.trip_queue[self.trip_count]:
            time.sleep(1)
            self.location = floor
            self.floors_passed += 1
            print(self.location)

            if self.destination == floor:
                self.arrival()

        self.trip_count += 1

    def arrival(self):
        self.doors_open = True
        time.sleep(5)
        self.doors_open = False

        if len(self.trip_queue) > self.trip_count:
            self.deploy()


class Person:
    def __init__(self, location, destination, weight=None):
        self.location = location
        self.destination = destination
        self.weight = weight if weight else None

    def call_elevator(self):
        pass
