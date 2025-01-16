# question 3 
p1 = input ("Enter your new password: ")
p2 = input ("Enter your new password again: ")
if p1 == p2:
    if len (p1)>=8 and len (p1)<=12:
        print ("Password set")
    else:
        print ("Error: Password must be 8-12 characters")