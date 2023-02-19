### sorting_hat ###

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Do you like Dawn or Dusk?")
print("\n  1) Dawn")
print("  2) Dusk")
Q1 = int(input())

if Q1 == 1:
    Gryffindor +=1
    Ravenclaw +=1
elif Q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("ERROR")
print("When I’m dead, I want people to remember me as:")
print(" \n1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

Q2 = int(input())

if Q2 == 1:
    Hufflepuff += 1
elif Q2== 2:
    Slytherin += 1
elif Q2== 3:
    Ravenclaw +=1
elif Q2 == 4:
    Gryffindor +=1
else: 
    print("ERROR")

print("Which kind of instrument most pleases your ear?")
print(" \n1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

Q3 = int(input())

if Q3 == 1:
    Slytherin += 1
elif Q3== 2:
     Hufflepuff += 1
elif Q3== 3:
    Ravenclaw +=1
elif Q3 == 4:
    Gryffindor +=1
else: 
    print("ERROR")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("Entras a la casa de Gryffindor")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("Entras a la casa de Ravenclaw")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("Entras a la casa de Hufflepuff")
else:
    print("Entras a la casa de Slytherin")