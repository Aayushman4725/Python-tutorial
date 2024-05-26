
def write_student_info():
    student_files=open("student.txt", "w")

    while True:
        name=input("Enter your name:")
        if name=="stop":
            break
        age=input("Enter your age:")
    
        print(student_files.write("Hello my name is " + name + " and I am " + str(age) + " years old.\n"))

    student_files.close()

def read_student_info():
    student_files=open("student.txt", "r")
    print(student_files.read())
    student_files.close()

write_student_info()