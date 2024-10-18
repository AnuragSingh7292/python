class Student:
    def __init__(self):
        self.name = ""
        self.reg_no = ""
        self.branch = ""
        self.age = 0
        self.cgpa = 0.0

def info(n):
    students = []
    print("\tEnter the student information")
    for i in range(n):
        student = Student()
        print("\n\nEnter the information of student [{}]\n".format(i+1))
        student.name = input("Enter the name.... ")
        student.reg_no = input("Enter the reg_no.... ")
        student.branch = input("Enter the branch name.... ")
        student.age = int(input("Enter the age.... "))
        student.cgpa = float(input("Enter the CGPA.... "))
        students.append(student)
    return students

def show(students):
    for i, student in enumerate(students):
        print("\n***************************************")
        print("\nInformation of student [{}]".format(i+1))
        print("Name:- ", student.name)
        print("Reg_no:- ", student.reg_no)
        print("Branch:- ", student.branch)
        print("Age:- ", student.age)
        print("CGPA:- ", student.cgpa)

def name(students):
    name = input("\nEnter the name to search... ")
    found = False
    for i, student in enumerate(students):
        if student.name == name:
            found = True
            print("\n***************************************")
            print("\nInformation of student [{}]".format(i+1))
            print("Name:- ", student.name)
            print("Reg_no:- ", student.reg_no)
            print("Branch:- ", student.branch)
            print("Age:- ", student.age)
            print("CGPA:- ", student.cgpa)
    if not found:
        print("\n***************************************")
        print("invalid input")

def reg_no(students):
    reg_no = input("\nEnter the registration to search... ")
    found = False
    for i, student in enumerate(students):
        if student.reg_no == reg_no:
            found = True
            print("\n***************************************")
            print("\nInformation of student [{}]".format(i+1))
            print("Name:- ", student.name)
            print("Reg_no:- ", student.reg_no)
            print("Branch:- ", student.branch)
            print("Age:- ", student.age)
            print("CGPA:- ", student.cgpa)
    if not found:
        print("\n***************************************")
        print("invalid input")

def main():
    n = int(input("enter the size... "))
    students = info(n)
    while True:
        print("\n***************************************")
        print("1.Enter for show the data.\n2.Enter the for using the name.\n3.Enter the for using registration no.\n4.Enter for exit.\nEnter the choice.....")
        choice = int(input())
        if choice == 1:
            print("\n***************************************")
            show(students)
        elif choice == 2:
            print("\n***************************************")
            name(students)
        elif choice == 3:
            print("\n***************************************")
            reg_no(students)
        elif choice == 4:
            print("\n***************************************")
            print("\nCoding is fun...!!")
            print("\nsuccessfully exits !!")
            break
        else:
            print("\n***************************************")
            print("Invalid input")

if __name__ == "__main__":
    main()


