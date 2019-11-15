

temp_list = []
print("Welcome to the weather station")
try:
    for counter in range(6):
        print (counter)
        reading = float(input("Please enter temp: " + str(counter + 1)))
        temp_list.append(reading)
    print(temp_list)
    print("Max temp is",max(temp_list))
    print("Min temp is",min(temp_list))

    print(round(sum(temp_list) / len(temp_list),2))
except ValueError:
    print("Numbers only")