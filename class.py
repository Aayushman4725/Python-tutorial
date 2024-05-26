class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


def getInfo():
    while True:
        student_list=[]
        name=input("Enter your name:")
        if name=="stop":
            break
        age=input("Enter your age:")
        gpa=input("Enter your gpa:")


        student_list.append(Student(name,str(age),str(gpa)))
       
        student_file=open("student2.txt","a")
        for student in student_list:
            student_file.write(str("Name: "+student.name + "\n" +"Age: "+ student.age + "\nGPA: " + student.gpa + "\n\n"))

        

getInfo()