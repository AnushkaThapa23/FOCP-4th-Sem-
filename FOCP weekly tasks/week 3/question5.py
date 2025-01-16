#question 5
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    p1 = input ("Enter your new password: ")
    p2 = input ("Enter your new password again: ")
    if p1 == p2:
        if len (p1)>=8 and len (p1)<=12:
            if p1 not in BAD_PASSWORDS:
                print ("Password set")
            else:
                print ("Password is too common")
        else:
            print ("Password must be 8-12 characters")
    else:
        print ("Error: Passwords do not match")