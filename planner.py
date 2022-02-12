def headerBanner():
    print("\n" * 5)
    print("\nWelcome to Course Planner")
    print("==========================\n")


def mainmenu():
    headerBanner()
    print("What would you like to do today?")
    print("[1] View all available courses")
    print("[2] Enroll/Remove my courses")
    print("[3] View selected courses and total units taken ")
    print("[4] Add Notes to Courses")
    print("[5] Read Notes of Courses")
    print("[6] Update Notes of Courses")
    print("[7] Delete Notes of Courses")
    print("\n")
    print("[0] Quit ")
    mainCategory = input("\nEnter your option number ---->")
    if mainCategory == "1":
        SelectingCourses.ViewAvailblCourses()
    elif mainCategory == "2":
        editcourses()
    elif mainCategory == "4":
        addnotes()
    elif mainCategory == "0":
        exit()

class Courses:
    instances=[]
    def __init__(self, name, description, units):
        self.Name = name
        self.Description = description
        self.Units = units
        self.instances.append(self.__str__())

    def __str__(self):
        return 'Course Code-->{}     CourseName-->{}     Units-->{}'.format(self.Name, self.Description, self.Units)

AddedCourses = []

course_1 = Courses('BIOF110', 'BIOLOGY LABORATORY', 1)
course_2 = Courses('BITSF110', 'ENGINEERING GRAPHICS', 2)
course_3 = Courses('BITSF111', 'THERMODYNAMICS', 3)
course_4 = Courses('CHEMF110', 'CHEMISTRY LAB', 1)
course_5 = Courses('CHEMF111', 'GEN CHEM  ', 3)
course_6 = Courses('EEEF111', 'ELECTRICAL SCIENCES', 3)
course_7 = Courses('MATHF111', 'MATHEMATICS', 3)
course_8 = Courses('PHYF110', 'PHY LAB',  1)
course_9 = Courses('PHYF111', 'MEOW', 3)

class SelectingCourses(Courses):

    @staticmethod
    def ViewAvailblCourses():
        while True:
            print("The Available Courses are:")
            print("===========\n")
            print(*Courses.instances,sep="\n")
        else:
            mainmenu()

def editcourses():
    # x=1
    # while x==1:
    #
    #     print(*AddedCourses,sep="\n")

        ask=input("Would you like to [A]dd courses or [R]emove courses? Press any other key to go back to mainmenu :-").upper()
        if ask=='A':
            course = input("Enter course code to add:-").upper()
            for I in Courses.instances:
                if course in I and I not in AddedCourses:
                    AddedCourses.append(I)
        if ask=='R':
            course = input("Enter course code to remove:-").upper()
            for J in AddedCourses:
                if course in J:
                    AddedCourses.remove(J)

        else:
            mainmenu()

def addnotes():
    print(*AddedCourses, sep="\n")
    ccode = input("Enter course code you want to enter notes for:  ").upper()
    for I in AddedCourses:
        if ccode in I:
            note=input("Enter the notes and gmeet links")
            I = f''
            print(I)
            print("Succesfully added")

    print(*AddedCourses, sep="\n")






headerBanner()
mainmenu()

