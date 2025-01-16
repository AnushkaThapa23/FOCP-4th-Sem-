
num = int (input("Enter the number of the table you require: "))
if num<0 or num>12:
    print ("Invalid input please enter a number between 0 and 12 inclusive.")
else:
    for i in range (13):
        prod = i*num
        print (i, 'x', num, '=', prod)
        i+=1