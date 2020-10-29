from School.School import School
   
    #2nd class about the child attending the School
class Child(School): # Child class is using inheritance from the School Class
    def __init__(self, name, age, yeargroup, schoolName, location):
        self.name = name
        self.age = age
        self.yeargroup = yeargroup
        super().__init__(schoolName, location)
        self.__password = 1 #private arrtribute for the users password
        self.__pass = 20
        self.word = 30
        print ({self.name})
        #Showing that data is being passed correctly on-screen
        #print('(Initialized Child Class: {})'.format(self.name))
        #print('(Initialized Child Class: {})'.format(self.age))
        #print("{}".format(self.name))
               
    def getChildName(self):
        return self.name

    def getChildAge(self):
        return self.age

    def getChildYearGroup(self):
        return self.yeargroup
 #this string is displaying the information
    def __str__(self):
        return f"{self.name} is {self.age} and is currently is yearx  {self.yeargroup} and the school name is {self.location } {super().__str__()}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
 # all the attributes associated with the 't'
 #instantiation

chi = Child("Kieran", 12, 8, "Royal Grammar School", "Newcastle Upon Tyne")
print(repr(chi))
print()
