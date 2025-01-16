# question 8
num = int (input("Enter the number of the table you require: "))
if num<0:
    for i in range(12, -1, -1):
        prod = i*num
        print (i, 'x', num, '=', prod)
else:
    for i in range (13):
        prod = i*num
        print (num, 'x', i, '=', prod)
        i+=1