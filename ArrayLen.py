
tableau = ["B", "O", "N", "J", "O", "U", "R"]
nb = len(tableau)
print("nb élémets du tableau ? " + str(nb))
print("len(tableau) = " + str(len(tableau)))
mot = ""

for i in range(0, nb):
    print("tableau[" + str(i) + "] = " + tableau[i])
    mot = mot + str(tableau[i]) 
print("mot = " + mot)

print("tableau[" + str(len(tableau)) )

print("tableau[" + str(len(tableau)) + "] = " )

print(str(tableau[len(tableau)])) # the program generates an error cause there's no element corresponding to the index = 7, that is there is no element: tableau[7]

print("tableau[" + str(len(tableau)) + "] = " + str(tableau[len(tableau)]))

