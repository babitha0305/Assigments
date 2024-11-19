Name = input("Enter your name: ")
Student_ID = input("Enter your ID: ")
print(Name)
print(Student_ID)

print("NOW KNOW YOUR GRADES")


def grade(n):

    if n <= 100 and n > 90:
        return "A"
    elif n <= 90 and n > 80:
        return "B"
    elif n <= 80 and n > 70:
        return "C"
    elif n <= 70 and n > 60:
        return "D"
    elif n <= 60 and n > 50:
        return "FAIL"
    else:
        return "INVALID"
def overall(n) :
    if n<=500 and n>400:
        return 'A'
    elif n<=400 and n>300:
        return 'B'
    elif n<=300 and n>200:
        return 'c'
    elif n<=200 and n>100:
        return 'D'
    else :
        print("Invalid")
    
 


print("The overall garde and the average of all the subjects are :")

MATH = int(input("Enter marks for MATH (out of 100): "))
print("the grade of MATHS is ",grade(MATH))
PHY = int(input("Enter marks for PHY (out of 100): "))
print("the grade of PHY is ",grade(PHY))
CHEM = int(input("Enter marks for CHEM (out of 100): "))
print("the grade of CHEM is ",grade(CHEM))
ENG = int(input("Enter marks for ENG (out of 100): "))
print("the grade of ENG is ",grade(ENG))
BIO = int(input("Enter marks for BIO (out of 100): "))
print("the grade of BIO is ",grade(BIO))

total_marks = MATH + PHY + CHEM + ENG + BIO
print("The total marks are : ",total_marks)

print("THE AVERAGE")
average_marks = total_marks / 5
print("Average marks:", average_marks)

print("Overall grade based on average marks:", grade(average_marks))

print("THE OVERALL GARDE: ")


print("Overall grade based on total marks:", overall(total_marks))



