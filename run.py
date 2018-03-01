import sys

from operation import open_building

command = sys.argv[1]

if command == 'elevators':
    open_building()
