
class School(): #defines a class in python, this is the school class
    def __init__(self, schoolName, location):
        self.schoolName = schoolName # set attributes for the class
        self.location = location # set attributes for the class
        #print('(Initialized School Class: {})'.format(self.schoolName)) # simply a debugging statement to see if the schoolname has correctly passed in a string
 

    def getSchoolName(self):# Defining the method schoolname
        return self.schoolName
        
    def getSchoolLocation(self):#Defining the method schoollocation
        return self.location

    
    def __str__(self): # I am using str to return the school name and location
        return f"School Name: {self.schoolName}. School Location: {self.location}"
    
    # repr method below, showing 2 options of printing the item
    def __repr__(self): # I am using the reper method below to pass the same details as the string
        #return f" {self.schoolName}, {self.location}"
        return "school name: {}, Location {}".format(self.schoolName, self.location)
        
    # Prints using the REPR function too.
    # instantiating the items for printing 
sch = School("Royal Grammar School", "Newcastle Upon Tyne") 
print("Below is an example of passing __repr__")
print(repr(sch)) # Print the repr string
print()