from myclass import Student
from chef import chef
from chinesechef import chinesechef

student1=Student("Prudvi",22,"CSE",False) #object creation for the class

print(student1.department)

mychef=chef()
mychef.make_a_chicken()
mychinesechef=chinesechef()
mychinesechef.make_a_chicken()
mychinesechef.make_a_friedrice()
mychinesechef.make_a_special_dish()