sweets=int(input("number of sweets in the tub?"))
students=int(input("Total number of students? "))
sweets_per_student=sweets//students
left=sweets%students
print(f"Each student will get {sweets_per_student} sweets and there will be {left} sweets left over")