from  Child.Child import Child
from School.School import School
from Overview.Overview import Overview


# Final instantiating
# Person 1
p1 = Overview("80%", "A", "Kieran", 8, 12, "Royal Grammar School", "Newcastle Upon Tyne")
print(p1)
print()

# Person 2
p2 = Overview("20%", "B", "Alan Heslop", 31, "University", "Sunderland University", "Sunderland")
print(p2)
print()

#access repr string
print()
print("__repr__ output")
print()
print(repr(p1))
