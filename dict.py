student = {
    "name": "Zishan Ahmed",
    "age": "21",                     #21 int
    "course": "B.tech",              #Note: only colon is allowed in bw keys and values.
    "subjects" : {                   #Note: in nested dictionary the 2nd dict will have colon not equal to
        "CS 301" : "EEE's",
        "CS 302" : "DISCRETE STRUCTURE",
        "CS 303" : "DATA STRUCTURE",
        "CS 304" : "DS",
        "CS 305" : "OOPM"
    }
}

print(student) 

print(student["name"])
print(student["age"])
print(student["course"])
print(student["subjects"])

print(student["subjects"] ["CS 303"])       # nested dictionary key access

                                    # PRACTICE SET (Q3)

marks ={}

marks1 = int(input("Enter 1st Subject Marks:"))
marks.update({"physics" : marks1})

marks2 = int(input("Enter 2nd Subject Marks:"))
marks.update({"chemistry" : marks2})

marks3 = int(input("Enter 3rd Subject Marks:"))
marks.update({"maths" : marks3})

print(marks)
