def headerBanner():
    print("\n" * 5)
    print("\nWelcome to Course Planner")
    print("==========================\n")


def mainmenu():
    headerBanner()
    print("What would you like to do today?")
    print("[1] View all available courses")
    print("[2] Add/Select courses")
    print("[3] View selected courses and total units taken ")
    print("[4] Add Notes to Courses")
    print("[5] Read Notes of Courses")
    print("[6] Update Notes of Courses")
    print("[7] Delete Notes of Courses")
    print("\n")
    print("[0] Quit ")
    mainCategory = input("\nEnter your option number ---->")
    if mainCategory == "1":
        AddedCourses.ViewAvailblCourses()
    elif mainCategory == "2":
        tabletShop()
    elif mainCategory == "3":
        laptopShop()
    elif mainCategory == "4":
        watchShop()
    elif mainCategory == "5":
        tvShop()
    elif mainCategory == "6":
        headphoneShop()
    elif mainCategory == "7":
        CheckOutCart()
    elif mainCategory == "8":
        headerBanner()
        Rating = input("Enter your review or complain here: ")
        input("Press any key to continue...")
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


course_1 = Courses('BIO F110 ', 'BIOLOGY LABORATORY', 1)
course_2 = Courses('BITS F110', 'ENGINEERING GRAPHICS', 2)
course_3 = Courses('BITS F111', 'THERMODYNAMICS', 3)
course_4 = Courses('CHEM F110', 'CHEMISTRY LAB', 1)
course_5 = Courses('CHEM F111', 'GEN CHEM  ', 3)
course_6 = Courses('EEE F111 ', 'ELECTRICAL SCIENCES', 3)
course_7 = Courses('MATH F111', 'MATHEMATICS', 3)
course_8 = Courses('PHY F110 ', 'PHY LAB',  1)
course_9 = Courses('PHY F111 ', 'MEOW', 3)

class AddedCourses(Courses):

    @staticmethod
    def ViewAvailblCourses():
        print("The Available Courses are:")
        print("===========\n")
        print(*Courses.instances,sep="\n")

    def AddCourses(self,):




headerBanner()
mainmenu()
