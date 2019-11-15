try:
    print("welcome, please enter a number of students")
    number_of_students = int (input ())
    if  number_of_students < 1:
        print("please enter a number greater than zero")
    else:
        number_of_rooms = number_of_students // 24
        remainder =  number_of_students % 24

        if remainder != 0:
            number_of_rooms += 1

        if number_of_rooms ==1:
            print("You will need", number_of_rooms, "room")
        else:
            print("You will need", number_of_rooms, "rooms")
except ValueError:
    print("Please enter a whole number")
