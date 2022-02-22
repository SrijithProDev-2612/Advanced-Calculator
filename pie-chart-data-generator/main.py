print("Hi!")
print("""
Pie chart is a way of representing data which shows the percentage and proportion of
provided data. A pie chart consists of sectors of a circle. The size of each sector
is directly proportional to the component part or information it represents.
""")
print("I can help you with generating datas for a pie chart...")
option = input("Enter P to continue: ")

def option1():
    if option == ("P"):
        print("You can only enter up to an maximum of 6 datas only!..")
        option1 = int(input("Enter data no 1: "))
        option2 = int(input("Enter data no 2: "))
        option3 = int(input("Enter data no 3, enter END once done: "))
    
    if option3 == ("END"):
        print("working fine, move further...")
    
    else:
        option4 = int(input("Enter data no 4, enter 0 if done: "))
        option5 = int(input("Enter data no 5, enter 0 if done: "))
        option6 = int(input("Enter data no 6, enter 0 if done: "))
        
    confirmation = input("Enter Y to continue, N to abort: ")
    
    if confirmation == "Y":
        totalvalue1 = sum = option1+ option2+ option3+ option4+ option5+ option6
        sum2 = option1 / totalvalue1
        sum3 = option2 / totalvalue1
        sum4 = option3 / totalvalue1
        sum5 = option4 / totalvalue1
        sum6 = option5 / totalvalue1
        sum7 = option6 / totalvalue1
        finalanswer1 = sum = sum2 * 360
        finalanswer2 = sum = sum3 * 360
        finalanswer3 = sum = sum4 * 360
        finalanswer4 = sum = sum5 * 360
        finalanswer5 = sum = sum6 * 360
        finalanswer6 = sum = sum7 * 360
        print("Central angle = ")
        print(totalvalue1)
        print("----------")
        print(sum2)
        print(sum3)
        print(sum4)
        print(sum5)
        print(sum6)
        print(sum7)
        print("----------")
        print("Therefore, the sector angles of the given data is listed below in ascending order....")
        print(finalanswer1)
        print(finalanswer2)
        print(finalanswer3)
        print(finalanswer4)
        print(finalanswer5)
        print(finalanswer6)
        
    
    if confirmation == "N":
        print("Process Aborted")
    
if option == ("P"):
    option1()
