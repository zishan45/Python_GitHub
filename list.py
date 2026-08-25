team = ["rohit", "virat", "rishabh", "sky", "hardik", "dube", "jadeja", "axar", "kuldeep", "arshdeep", "bumrah"]        # playing 11 of T20 Wc 2024

print(team)     # list
print(team[6])

team.append("siraj")                    # note: it can append only one value at end of list           

print(team)

print(len(team))

team.insert(12, "samson")               # inserts data in the required index of list
team.insert(13, "chahal")
team.insert(14, "jaiswal")
print(team)

print("our squad:")
print("team in ascending:", team.sort())                # sorts list in ascending order
print("team in desc:", team.sort(reverse= True))        # sorts list in decending order
print(team.reverse())                                   # reverse the list and print last idx element 1st

team.append("khaleel")
team.remove("khaleel")                  # removes the selected element from list  (element selected)

print(team.reverse())
team.append("rinku")
team.append("jitesh")                   # appends or insert at last
print(team)

print(team.pop(16))                     # removes the selected index element   (index selected)
print(team)
