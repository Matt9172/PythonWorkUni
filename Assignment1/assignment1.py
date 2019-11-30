__author__ = "Matthew McDougall"
__email__ = "U1961826@unimail.hud.ac.uk"
__licence__ = "The Unilicense"
__version__ = "28/11/2019"

print("Speed Camera Interface")
vehicle_type = []
vehicle_speed = ()
count = 1

while 1:
    reading = input("Input type of vehicle and speed e.g. H30 or C15: ").upper()
    if reading in "END".upper():
        break
    elif reading[0] in ("H", "L", "C",):
        vehicle_type.append(reading[0])
        print(vehicle_type)
        vehicle_speed += (reading[1:3],)
        print(vehicle_speed)
    else:
        print("Please only enter data that starts with a H, L or C and has a two digit number afterwards e.g H30")

no_of_vehicles = len(vehicle_type)
highest_speed = max(vehicle_speed)
lowest_speed = min(vehicle_speed)
avg_speed = sum(vehicle_speed) / len(vehicle_speed)
print("The number of vehicles was: ", no_of_vehicles)
print("The highest speed was: ", highest_speed, "mph")
print("The lowest speed was: ", lowest_speed, "mph")
print("The average speed was: ", avg_speed, "mph")
