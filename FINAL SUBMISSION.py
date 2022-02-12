def headerBanner():
    print("\nWelcome to Course Planner")
    print("==========================\n")

def mainmenu():
    headerBanner()
    print("What would you like to do today?")
    print("[1] View all available courses")
    print("[2] Enroll in/Remove my courses")
    print("[3] View selected courses and Total Units Taken ")
    print("[4] Add Notes to Courses")
    print("[5] Read Notes of Courses")
    print("[6] Update Notes of Courses")
    print("[7] Delete Notes of Courses")
    print("\n")
    print("[0] Quit ")
    mainCategory = input("\nEnter your option number ---->")
    if mainCategory == "1":
        Courses.viewavailblcourses()
    elif mainCategory == "2":
        Courses.editcourses()
    elif mainCategory == "3":
        Courses.viewenrolledcourses()
    elif mainCategory == "4":
        Courses.addnotes()
    elif mainCategory == "5":
        Courses.readnotes()
    elif mainCategory == "6":
        Courses.updatenotes()
    elif mainCategory == "7":
        Courses.deletenotes()
    elif mainCategory == "0":
        exit()
    else:
        wronginput()

def wronginput():
    print("Enter Valid Input")
    i = input("Press enter to go back to Main Menu")
    mainmenu()

allcourses={}
AddedCourses = []

class Courses:
    instances = []
    def __init__(self, name, description, units):
        self.Name = name
        self.Description = description
        self.Units = units
        allcourses[self]=self.str()
        self.instances.append(self.__str__())

    def str(self):
        return [self.Name, self.Description, self.Units]

    def __str__(self):
        return 'Course Code-->{}     CourseName-->{}     Units-->{}'.format(self.Name, self.Description, self.Units)

    @staticmethod
    def viewavailblcourses():
        print("The Available Courses are:")
        print("===========\n")
        print(*Courses.instances,sep="\n")
        i=input("Press enter to go back to Main Menu")
        mainmenu()

    @classmethod
    def editcourses(cls):

        ask = input("Would you like to [A]dd courses or [R]emove courses? Press any other key to go back to mainmenu :-").upper()
        if ask == 'A':
            coursecode = input("Enter course-code to add:-").upper()
            for I in allcourses.values():
                if coursecode == I[0] and coursecode not in AddedCourses:
                    AddedCourses.append(I)
                    print("Course added successfully")
        if ask == 'R':
            coursecode = input("Enter course-code to remove:-").upper()
            for J in AddedCourses:
                if coursecode == J[0]:
                    AddedCourses.remove(J)
                    print("Course removed successfully")
                    i = input("Press enter to go back to Main Menu")
                    mainmenu()

        else:
            mainmenu()

    @staticmethod
    def viewenrolledcourses():
        print("Your Enrolled Courses are:")
        print(*AddedCourses, sep="\n")
        print("===========\n")
        S=0
        for U in AddedCourses:
            S+=U[2]
        print ("Your Total Units are",S)
        print("===========\n")
        i = input("Press enter to go back to Main Menu")
        mainmenu()

    @staticmethod
    def addnotes():
        print(*AddedCourses, sep="\n")
        print("===========\n")
        coursecode = input("Enter course code you want to enter notes for:  ").upper()
        for I in AddedCourses:
            if coursecode == I[0]:
                note=input("Enter the notes and gmeet links for this course--->")
                X={"Notes": [note]}
                I.append(X)
                print("Succesfully added")
            else:
                print("Add Courses first")

        print(*AddedCourses, sep="\n")
        i = input("Press enter to go back to Main Menu")
        mainmenu()

    @staticmethod
    def readnotes():
        coursecode = input("Enter course code you want to read notes of:  ").upper()
        for I in AddedCourses:
            if coursecode == I[0] and len(I)>=4:
                print(I[3])
            else:
                print("Add Courses first")
        i = input("Press enter to go back to Main Menu")
        mainmenu()

    @staticmethod
    def updatenotes():
        coursecode = input("Enter course code you want to update notes of:  ").upper()
        for I in AddedCourses:
            if coursecode == I[0] and len(I)>=4:
                updatenote = input("Enter what you'd like to add--->")
                I[3]["Notes"].append(updatenote)
                print("Notes Updated")
            else:
                print("Add Courses first")
        i = input("Press enter to go back to Main Menu")
        mainmenu()

    @staticmethod
    def deletenotes():
        coursecode = input("Enter course code you want to DELETE notes of:  ").upper()
        for I in AddedCourses:
            if coursecode == I[0] and len(I)>=4:
                I.remove(I[3])
                print("Notes deleted")
            else:
                print("Add Courses first")
        i = input("Press enter to go back to Main Menu")
        mainmenu()

course_1 = Courses('BIOF110', 'BIOLOGY LABORATORY', 1)
course_2 = Courses('BITSF110', 'ENGINEERING GRAPHICS', 2)
course_3 = Courses('BITSF111', 'THERMODYNAMICS', 3)
course_4 = Courses('CHEMF110', 'CHEMISTRY LAB', 1)
course_5 = Courses('CHEMF111', 'GEN CHEM  ', 3)
course_6 = Courses('EEEF111', 'ELECTRICAL SCIENCES', 3)
course_7 = Courses('MATHF111', 'MATHEMATICS', 3)
course_8 = Courses('PHYF110', 'PHY LAB',  1)
course_9 = Courses('PHYF111', 'MEOW', 3)

mainmenu()

#SUBMISSION BY AMRIT KUMAR JHA
