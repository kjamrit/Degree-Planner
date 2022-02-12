class Courses:
    instances=[]
    def __init__(self, name, description, units):
        self.Name = name
        self.Description = description
        self.Units = units
        self.instances.append(self.__str__())

    def __str__(self):
        return '{}-{}-{}'.format(self.Name, self.Description, self.Units)


course_1 = Courses('BIOF110', 'BIOLOGY LABORATORY', 1)
course_2 = Courses('BITSF110', 'ENGINEERING GRAPHICS', 2)
course_3 = Courses('BITSF111', 'THERMODYNAMICS', 3)
course_4 = Courses('CHEMF110', 'CHEMISTRY LAB', 1)
course_5 = Courses('CHEMF111', 'GEN CHEM', 3)
course_6 = Courses('EEEF111', 'ELECTRICAL SCIENCES', 3)
course_7 = Courses('MATHF111', 'MATHEMATICS', 3)
course_8 = Courses('PHYF110', 'PHY LAB',  1)
course_9 = Courses('PHYF111', 'MEOW', 3)


print(*Courses.instances,sep="\n")

class SelectingCourses(Courses):

    def ViewAvailblCourses():
        print("The Available Courses are:")
        print("===========\n")
        print(*Courses.instances,sep="\n")


    def Addcourse(self):
        for i in Courses.instances:




# def editcourses(AddedCourses=None):
#     x=1
#     while x==1:
#         if AddedCourses is None:
#             AddedCourses = []
#             print("No course added!")
#         else:
#             print("Your added courses are:")
#             AddedCourses = AddedCourses
#
#         print(*AddedCourses,sep="\n")
#
#         ask=input("Would you like to [A]dd courses or [R]emove courses? Press any other key to go back to mainmenu :-").upper()
#         if ask=='A':
#             course = input("Enter course code to add:-").upper()
#             for I in Courses.instances:
#                 if course in I and I not in AddedCourses:
#                     AddedCourses.append(I)
#         if ask=='R':
#             course = input("Enter course code to remove:-").upper()
#             for J in AddedCourses:
#                 if course in J:
#                     AddedCourses.remove(J)
#
#         else:
#             mainmenu()
#
# def viewaddedcourses:
#     print(*AddedCourses)
#
#
#
#
#
# # def AddCourse():
# #     course=input("Enter course:-")
# #     if course not in AddedCourses:
# #         AddedCourses.append(course)
#
#
#
# # def RemoveCourse(course):
# #     if course in AddedCourses:
# #         AddedCourses.remove(course)
#
# headerBanner()
# mainmenu()