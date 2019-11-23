name = input ('Enter the student\'s name: ')

mark_1 = int (input ('Enter first result: '))
mark_2 = int (input ('Enter second result: '))
mark_3 = int (input ('Enter third result: '))
mark_4 = int (input ('Enter fourth result: '))
mark_5 = int (input ('Enter fifth result: '))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 +mark_5

average_mark = total_marks / 5

print ()
print('Final Mark for ' + name + ' is  ' + str (average_mark))