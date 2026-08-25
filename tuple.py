scores = (52, 14, 36, 48, 92, 55, 9)                   # tuple

print("Rohit Scores in WC 2024: ", scores) 

intro = ("zishan", 20, "B.tech", "CSE", 7.66, "will he be placed: YES", 7.66, 7.66, 7.66)          # clear it tuple can store different type of data
print(intro)
print(type(intro))

# NOTE: (vvi)  list elements can be accessed and updated as well, but in tuple we can only access we can't update it.

# print(intro[3])     # access is allowed
# intro[4] = 7.8      # error, not possible in tuple to update the element

print(intro.index("CSE"))         # case sensitive (cse no) -> CSE,    it returns index of element
print(intro.count(7.66))


