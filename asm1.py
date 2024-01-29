#code Asm 1
full_name = str(input('Enter your full name: '))

# ENTER credits for each subject
math_credits = int(input("Enter the number of math credits:  "))
literature_credits = int(input("Enter the number of literature credits:  "))
english_credits = int(input("Enter the number of English credits:  "))

# Enter points for each subject
math_point = float(input("Enter your number of math point:  ")) # float data type because points can be comma points
literature_point = float(input("Enter your number of literature point:  "))
english_point = float(input("Enter your number of English point:  "))

# List to store student information
infomation_student1 = [full_name, math_credits, literature_credits, english_credits, math_point, literature_point, english_point]


credits = [math_credits, literature_credits, english_credits]
total_of_credits = sum(credits) # variable to store the total number of credits for all subjects

point_st = [math_point, literature_point, english_point]


def avg_point(credits, diem_st):
    sum_point = 0
    for i in range(len(credits)):
        sum_point += credits[i] * diem_st[i]
    avg = sum_point / total_of_credits
    return avg


avg_p = avg_point(credits, point_st) # bien de luu chu du lieu ham tra ve



def GPA_point(name, point):
    print("Student name:" + name)
    print("GPA : " + str(point))
    try:
        file = open('Ngoc/GPA', 'w')
        file.write("Student name:" + name + "\n" "GPA :" + str(point))
    except:
        print("This file has some problems!!!")

GPA_point(full_name, avg_p)

print("The GPA: ", avg_p)