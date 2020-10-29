from Child.Child import Child
from School.School import School
 
 # 3rd class will show the attendance, grade and bring back all data
class Overview(Child, School): #multiple inheritence
    def __init__(self, attendance, grade, name, age, yeargroup, schoolName, location):
        self.attendance = attendance
        self.grade = grade
        super().__init__(name, age, yeargroup, schoolName, location)
        #print('(Initialized Overview Class: {})'.format(self.name))

    def getAttendance(self):
        return self.attendance

    def getGrade(self):
        return self.grade
    
    # inherited
    # __Str__ informal representation
    def __str__(self): # STR method to print out an easily readable sentence.
        return f"{self.name}s attendance has been oustanding, acheiving an overall attendance of: {self.attendance}. He is currently Aged: {self.age} and is in YearGroup:  {self.yeargroup} and his overall grade for the year is: {self.grade} - he attends the school in {self.location} and the name of the school is {self.schoolName}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"