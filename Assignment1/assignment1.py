__author__ = "Matthew McDougall"
__email__ = "U1961826@unimail.hud.ac.uk"
__licence__ = "The Unilicense"
__version__ = "28/11/2019"

print("Speed Camera Interface")
vehicle_type = ()
vehicle_speed = ()
count = 1
speed_limit_violations = ()
while 1:
    reading = str(input("Input type of vehicle and speed e.g. H30 or C15: ").upper())

    if reading[0] in ("H", "L", "C",):
        vehicle_type += (reading[0],)
        print(vehicle_type)
        reading_number = int(reading[1:])
        vehicle_speed += (reading_number,)
        print(vehicle_speed)
        if reading_number > 50:
            speed_limit_violations += (reading_number,)

    if reading in "END".upper():
        break
    else:
        print("Please only enter data that starts with a H, L or C and has a two digit number afterwards e.g H30")

no_of_vehicles = len(vehicle_type)
highest_speed = max(vehicle_speed)
lowest_speed = min(vehicle_speed)
avg_speed = sum(vehicle_speed) / len(vehicle_speed)
speed_limit_percentage = ('{0:.2f}%'.format((len(speed_limit_violations) / len(vehicle_speed) * 100)))
print("Number of vehicles: ", no_of_vehicles)
print("Highest speed: ", highest_speed, "mph")
print("Lowest speed: ", lowest_speed, "mph")
print("Average speed: ", round(avg_speed, 1), "mph")

print("Speed Limit Violations:", len(speed_limit_violations), '(', speed_limit_percentage, ')')
