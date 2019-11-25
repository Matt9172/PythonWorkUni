print("Welcome to the sweet shop!")
print("Please enter the prices of your sweets below.")

item_1 = int(input('Enter first price: '))
item_2 = int(input('Enter second price: '))
item_3 = int(input('Enter third price: '))
item_4 = int(input('Enter fourth price: '))
item_5 = int(input('Enter fifth price: '))

total = item_1 + item_2 + item_3 + item_4 + item_5
average = total / 5
print("Your total is", total, "p")
print("The average is", average, "p")
print("The most expensive item cost", max(item_1,  item_2,  item_3,  item_4, item_5), "p")
print("The cheapest item cost", min(item_1,  item_2,  item_3,  item_4, item_5), "p")
