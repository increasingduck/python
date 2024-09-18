def printLetterGrade():
    grade = float(input("please enter grade"))
    if grade >= 99:
        print("A+")
    if grade < 99 and grade >= 96:
        print("A")
    if grade > 89 and grade >= 93:
        print("A-")
    if grade <= 89 and grade > 86:
        print("B+")
    if grade < 86 and grade >= 84:
        print("B")

    
if __name__ == "__main__":
    printLetterGrade()