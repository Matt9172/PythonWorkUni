__author__ = "Matthew McDougall"
__email__ = "U1961826@unimail.hud.ac.uk"
__licence__ = "The Unilicense"
__version__ = "28/11/2019"

print("Speed Camera Interface")
vehicle_type = []
vehicle_speed = []
count = 1

while count: 1
reading = input("Input type of vehicle and speed e.g. H30 or C15" + str())
if reading[0] in ("H", "L", "C",):
    vehicle_type.append(reading[0])
if reading[1:3]


    max = max(vehicle_speed)
    min = min(vehicle_speed)
    avg = sum(vehicle_speed) / len(vehicle_speed)
    rounded = round(avg, 2)