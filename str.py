                             # strings (str)
student = "I AM ZISHAN AHMED"  

print(student)
print(student[5])
print(len(student))

str = "Hello Python"
print(str)
print(len(str))

                    # slicing in str
str2= "one of the most loved language "
print(str2)
print(len(str2))          # 32 indecies (0 to 31 or len(str2))

print(str2[2 : 29])
print(str2[ : len(str2)])
print(str2[0 : ])
print(str2[5 : 26])
print(str[-30 : -2])          # indexing starts from back of str from -1 -2 -3 ......

                  # str functions (methods)
bio ="i am a coder i am zishan ahmed engg student of computer science"

print(bio)
print(bio.capitalize())
print(bio.upper())

print(bio.replace("coder", "champion"))

print(bio.find("zishan"))     # returns index
print(bio.count("i"))         # returns the count of i
print(bio.endswith("ce"))     # returns True if str ends with ce else False

