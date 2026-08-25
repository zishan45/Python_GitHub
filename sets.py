student = {1, "ZISHAN", "CSE", 7.66, "6th Sem"}

print(student)
print(type(student))

student.add("Muzaffarpur")            # randomly adds elements at any index
print(student)

student.remove(7.66)                  # removes the selected element 
print(student)

student.pop()                         # deletes random element from set
student.add("CGPA: 7.66")
print(student)

rgpv = {7.14, 7.57, 7.67, 8.17, "CGPA: 7.66"}

print(student.union(rgpv))           # union function of sets is used to concat two sets
print(rgpv.intersection(student))


