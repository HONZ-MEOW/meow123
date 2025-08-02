from function01 import *
from StudentClass import *
printSt("john")

x={"Chinese":100,"Math":95,"English":99}
tests_dict={"Monthly Exam 01":x,"Monthly Exam 02":{"Chinese":98,"Math":55,"English":19},"Monthly Exam 03":{"Chinese":96,"Math":63,"English":79}}
student01 = Student(tests_dict,"john","1")
student01.ShowStudentInfo()