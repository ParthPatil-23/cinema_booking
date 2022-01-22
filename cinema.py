# billing system
# Task  is to make a cinema software for ticket booking....
# Basic information about the coustomer
name1 = input("please enter your name:- ")
age = int(input("please enter your age:- "))

# Opening the txt file to read data for seats

file1 = open("seat.txt","r")
file1 = file1.read()
file1 = file1.split("\n")

# Printing the seat number accordingly 

seat = [["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20"]
,["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B20"]
,["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20"]
,["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14", "D15", "D16", "D17", "D18", "D19", "D20"]
,["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20"]
,["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20"]
,["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20"]
,["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17", "H18", "H19", "H20"]
,["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16", "I17", "I18", "I19", "I20"]
,["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "J14", "J15", "J16", "J17", "J18", "J19", "J20"]
,["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12", "K13", "K14", "K15", "K16", "K17", "K18", "K19", "K20"]]

seat1 = int(input("How many seat do you want:- "))


# Printing Seat arrangment 
space=" "
for row in seat:
    print(space*1, end="")
    # row = [a, b, c, d, e, f, ]
    for mySeat in row:
        if mySeat not in file1:
            print(mySeat, end="  ")
        else:
            if(len(mySeat)==2):
                print("**", end="  ")
            else:
                print("*", end="  ")
    print("\n", end="")


# opening myfile to fill in seat number

file1 = open("seat.txt", "a")

# Asking for the seat number:

if seat1 == 1:
	print("\nwe are really sorry for you that you don't have friends")
	a1 = input("\nplease enter your seat number acording to the chart:- ")
	a1 +='\n'
	file1.write(a1)
	

	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

if seat1 == 2:
	a1 = input("\nplease enter your first seat number acording to the chart:- ")
	a2 = input("\nplease enter your second seat number acording to the chart:- ")
	a1 +='\n'
	a2 +='\n'
	file1.write(a1)
	file1.write(a2)

	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

	if a2[0] == "A":	
		bill = int(250 + bill)
	if a2[0] == "B":
		bill = int(250 + bill)
	if a2[0] == "C":
		bill = int(250 + bill)
	if a2[0] == "D":
		bill = int(150 + bill)
	if a2[0] == "E":
		bill = int(150 + bill)
	if a2[0] == "F":
		bill = int(150 + bill)
	if a2[0] == "G":
		bill = int(150 + bill)
	if a2[0] == "H":
		bill = int(100 + bill)
	if a2[0] == "I":
		bill = int(100 + bill)
	if a2[0] == "J":
		bill = int(100 + bill)
	if a2[0] == "K":
		bill = int(100 + bill)
	
if seat1 == 3:
	a1 = input("\nplease enter your first seat number acording to the chart:- ")
	a2 = input("\nplease enter your second seat number acording to the chart:- ")
	a3 = input("\nplease enter your third seat number acording to the chart:- ")
	a1 +='\n'
	a2 +='\n'
	a3 +='\n'
	file1.write(a1)
	file1.write(a2)
	file1.write(a3)
	

	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

	if a2[0] == "A":	
		bill = int(250 + bill)
	if a2[0] == "B":
		bill = int(250 + bill)
	if a2[0] == "C":
		bill = int(250 + bill)
	if a2[0] == "D":
		bill = int(150 + bill)
	if a2[0] == "E":
		bill = int(150 + bill)
	if a2[0] == "F":
		bill = int(150 + bill)
	if a2[0] == "G":
		bill = int(150 + bill)
	if a2[0] == "H":
		bill = int(100 + bill)
	if a2[0] == "I":
		bill = int(100 + bill)
	if a2[0] == "J":
		bill = int(100 + bill)
	if a2[0] == "K":
		bill = int(100 + bill)

	if a3[0] == "A":	
		bill = int(250 + bill)
	if a3[0] == "B":
		bill = int(250 + bill)
	if a3[0] == "C":
		bill = int(250 + bill)
	if a3[0] == "D":
		bill = int(150 + bill)
	if a3[0] == "E":
		bill = int(150 + bill)
	if a3[0] == "F":
		bill = int(150 + bill)
	if a3[0] == "G":
		bill = int(150 + bill)
	if a3[0] == "H":
		bill = int(100 + bill)
	if a3[0] == "I":
		bill = int(100 + bill)
	if a3[0] == "J":
		bill = int(100 + bill)
	if a3[0] == "K":
		bill = int(100 + bill)

if seat1 == 4:
	a1 = input("\nplease enter your first seat number acording to the chart:- ")
	a2 = input("\nplease enter your second seat number acording to the chart:- ")
	a3 = input("\nplease enter your third seat number acording to the chart:- ")
	a4 = input("\nplease enter your forth seat number acording to the chart:- ")
	a1 +='\n'
	a2 +='\n'
	a3 +='\n'
	a4 +='\n'
	file1.write(a1)
	file1.write(a2)
	file1.write(a3)
	file1.write(a4)
	

	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

	if a2[0] == "A":	
		bill = int(250 + bill)
	if a2[0] == "B":
		bill = int(250 + bill)
	if a2[0] == "C":
		bill = int(250 + bill)
	if a2[0] == "D":
		bill = int(150 + bill)
	if a2[0] == "E":
		bill = int(150 + bill)
	if a2[0] == "F":
		bill = int(150 + bill)
	if a2[0] == "G":
		bill = int(150 + bill)
	if a2[0] == "H":
		bill = int(100 + bill)
	if a2[0] == "I":
		bill = int(100 + bill)
	if a2[0] == "J":
		bill = int(100 + bill)
	if a2[0] == "K":
		bill = int(100 + bill)

	if a3[0] == "A":	
		bill = int(250 + bill)
	if a3[0] == "B":
		bill = int(250 + bill)
	if a3[0] == "C":
		bill = int(250 + bill)
	if a3[0] == "D":
		bill = int(150 + bill)
	if a3[0] == "E":
		bill = int(150 + bill)
	if a3[0] == "F":
		bill = int(150 + bill)
	if a3[0] == "G":
		bill = int(150 + bill)
	if a3[0] == "H":
		bill = int(100 + bill)
	if a3[0] == "I":
		bill = int(100 + bill)
	if a3[0] == "J":
		bill = int(100 + bill)
	if a3[0] == "K":
		bill = int(100 + bill)

	if a4[0] == "A":	
		bill = int(250 + bill)
	if a4[0] == "B":
		bill = int(250 + bill)
	if a4[0] == "C":
		bill = int(250 + bill)
	if a4[0] == "D":
		bill = int(150 + bill)
	if a4[0] == "E":
		bill = int(150 + bill)
	if a4[0] == "F":
		bill = int(150 + bill)
	if a4[0] == "G":
		bill = int(150 + bill)
	if a4[0] == "H":
		bill = int(100 + bill)
	if a4[0] == "I":
		bill = int(100 + bill)
	if a4[0] == "J":
		bill = int(100 + bill)
	if a4[0] == "K":
		bill = int(100 + bill)

if seat1 == 5:
	a1 = input("\nplease enter your first seat number acording to the chart:- ")
	a2 = input("\nplease enter your second seat number acording to the chart:- ")
	a3 = input("\nplease enter your third seat number acording to the chart:- ")
	a4 = input("\nplease enter your forth seat number acording to the chart:- ")
	a5 = input("\nplease enter your fifth seat number acording to the chart:- ")
	a1 +='\n'
	a2 +='\n'
	a3 +='\n'
	a4 +='\n'
	a5 +='\n'
	file1.write(a1)
	file1.write(a2)
	file1.write(a3)
	file1.write(a4)
	file1.write(a5)
	

	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

	if a2[0] == "A":	
		bill = int(250 + bill)
	if a2[0] == "B":
		bill = int(250 + bill)
	if a2[0] == "C":
		bill = int(250 + bill)
	if a2[0] == "D":
		bill = int(150 + bill)
	if a2[0] == "E":
		bill = int(150 + bill)
	if a2[0] == "F":
		bill = int(150 + bill)
	if a2[0] == "G":
		bill = int(150 + bill)
	if a2[0] == "H":
		bill = int(100 + bill)
	if a2[0] == "I":
		bill = int(100 + bill)
	if a2[0] == "J":
		bill = int(100 + bill)
	if a2[0] == "K":
		bill = int(100 + bill)

	if a3[0] == "A":	
		bill = int(250 + bill)
	if a3[0] == "B":
		bill = int(250 + bill)
	if a3[0] == "C":
		bill = int(250 + bill)
	if a3[0] == "D":
		bill = int(150 + bill)
	if a3[0] == "E":
		bill = int(150 + bill)
	if a3[0] == "F":
		bill = int(150 + bill)
	if a3[0] == "G":
		bill = int(150 + bill)
	if a3[0] == "H":
		bill = int(100 + bill)
	if a3[0] == "I":
		bill = int(100 + bill)
	if a3[0] == "J":
		bill = int(100 + bill)
	if a3[0] == "K":
		bill = int(100 + bill)

	if a4[0] == "A":	
		bill = int(250 + bill)
	if a4[0] == "B":
		bill = int(250 + bill)
	if a4[0] == "C":
		bill = int(250 + bill)
	if a4[0] == "D":
		bill = int(150 + bill)
	if a4[0] == "E":
		bill = int(150 + bill)
	if a4[0] == "F":
		bill = int(150 + bill)
	if a4[0] == "G":
		bill = int(150 + bill)
	if a4[0] == "H":
		bill = int(100 + bill)
	if a4[0] == "I":
		bill = int(100 + bill)
	if a4[0] == "J":
		bill = int(100 + bill)
	if a4[0] == "K":
		bill = int(100 + bill)

	if a5[0] == "A":	
		bill = int(250 + bill)
	if a5[0] == "B":
		bill = int(250 + bill)
	if a5[0] == "C":
		bill = int(250 + bill)
	if a5[0] == "D":
		bill = int(150 + bill)
	if a5[0] == "E":
		bill = int(150 + bill)
	if a5[0] == "F":
		bill = int(150 + bill)
	if a5[0] == "G":
		bill = int(150 + bill)
	if a5[0] == "H":
		bill = int(100 + bill)
	if a5[0] == "I":
		bill = int(100 + bill)
	if a5[0] == "J":
		bill = int(100 + bill)
	if a5[0] == "K":
		bill = int(100 + bill)

if seat1 == 6:
	a1 = input("\nplease enter your first seat number acording to the chart:- ")
	a2 = input("\nplease enter your second seat number acording to the chart:- ")
	a3 = input("\nplease enter your third seat number acording to the chart:- ")
	a4 = input("\nplease enter your forth seat number acording to the chart:- ")
	a5 = input("\nplease enter your fifth seat number acording to the chart:- ")
	a6 = input("\nplease enter your sixth seat number acording to the chart:- ")
	a1 +='\n'
	a2 +='\n'
	a3 +='\n'
	a4 +='\n'
	a5 +='\n'
	a6 +='\n'
	file1.write(a1)
	file1.write(a2)
	file1.write(a3)
	file1.write(a4)
	file1.write(a5)
	file1.write(a6)
	
	
	if a1[0] == "A":
		bill = int(250)
	if a1[0] == "B":
		bill = int(250)
	if a1[0] == "C":
		bill = int(250)
	if a1[0] == "D":
		bill = int(150)
	if a1[0] == "E":
		bill = int(150)
	if a1[0] == "F":
		bill = int(150)
	if a1[0] == "G":
		bill = int(150)
	if a1[0] == "H":
		bill = int(100)
	if a1[0] == "I":
		bill = int(100)
	if a1[0] == "J":
		bill = int(100)
	if a1[0] == "K":
		bill = int(100)

	if a2[0] == "A":	
		bill = int(250 + bill)
	if a2[0] == "B":
		bill = int(250 + bill)
	if a2[0] == "C":
		bill = int(250 + bill)
	if a2[0] == "D":
		bill = int(150 + bill)
	if a2[0] == "E":
		bill = int(150 + bill)
	if a2[0] == "F":
		bill = int(150 + bill)
	if a2[0] == "G":
		bill = int(150 + bill)
	if a2[0] == "H":
		bill = int(100 + bill)
	if a2[0] == "I":
		bill = int(100 + bill)
	if a2[0] == "J":
		bill = int(100 + bill)
	if a2[0] == "K":
		bill = int(100 + bill)

	if a3[0] == "A":	
		bill = int(250 + bill)
	if a3[0] == "B":
		bill = int(250 + bill)
	if a3[0] == "C":
		bill = int(250 + bill)
	if a3[0] == "D":
		bill = int(150 + bill)
	if a3[0] == "E":
		bill = int(150 + bill)
	if a3[0] == "F":
		bill = int(150 + bill)
	if a3[0] == "G":
		bill = int(150 + bill)
	if a3[0] == "H":
		bill = int(100 + bill)
	if a3[0] == "I":
		bill = int(100 + bill)
	if a3[0] == "J":
		bill = int(100 + bill)
	if a3[0] == "K":
		bill = int(100 + bill)

	if a4[0] == "A":	
		bill = int(250 + bill)
	if a4[0] == "B":
		bill = int(250 + bill)
	if a4[0] == "C":
		bill = int(250 + bill)
	if a4[0] == "D":
		bill = int(150 + bill)
	if a4[0] == "E":
		bill = int(150 + bill)
	if a4[0] == "F":
		bill = int(150 + bill)
	if a4[0] == "G":
		bill = int(150 + bill)
	if a4[0] == "H":
		bill = int(100 + bill)
	if a4[0] == "I":
		bill = int(100 + bill)
	if a4[0] == "J":
		bill = int(100 + bill)
	if a4[0] == "K":
		bill = int(100 + bill)

	if a5[0] == "A":	
		bill = int(250 + bill)
	if a5[0] == "B":
		bill = int(250 + bill)
	if a5[0] == "C":
		bill = int(250 + bill)
	if a5[0] == "D":
		bill = int(150 + bill)
	if a5[0] == "E":
		bill = int(150 + bill)
	if a5[0] == "F":
		bill = int(150 + bill)
	if a5[0] == "G":
		bill = int(150 + bill)
	if a5[0] == "H":
		bill = int(100 + bill)
	if a5[0] == "I":
		bill = int(100 + bill)
	if a5[0] == "J":
		bill = int(100 + bill)
	if a5[0] == "K":
		bill = int(100 + bill)

	if a6[0] == "A":	
		bill = int(250 + bill)
	if a6[0] == "B":
		bill = int(250 + bill)
	if a6[0] == "C":
		bill = int(250 + bill)
	if a6[0] == "D":
		bill = int(150 + bill)
	if a6[0] == "E":
		bill = int(150 + bill)
	if a6[0] == "F":
		bill = int(150 + bill)
	if a6[0] == "G":
		bill = int(150 + bill)
	if a6[0] == "H":
		bill = int(100 + bill)
	if a6[0] == "I":
		bill = int(100 + bill)
	if a6[0] == "J":
		bill = int(100 + bill)
	if a6[0] == "K":
		bill = int(100 + bill)

if seat1 >= 7:
		print("\nwe are sorry you can't book for more than 6 people because of company policy")


file1.close()


eat1 = input("\nDo you like to have something to eat while watching the movie:- ")	



# While loop if the coustmer wants to something else to eat:
while(True):


	if eat1 == "yes":
		print('''\nwe have varity of things to choose from:- 
		1. Popcorn
		2. Nachos
		3. Cold beverges''')
		food1 = int(input("\nselect the number of the food item:- "))

		if food1 == 1:
			print('''\nwe have 2 types of popcorns:
				1. simple salted popcorn  => 100 (50 extra for large)
				2. cheese popcorn         => 150 (50 extra for large)
				3. caremel salted popcorn => 200 (50 extra for large''')
			pop1 = int(input("\nselect the popcorn by their number:- ")) 
			print('''\nwe have three sizes:
					1. medium
					2. large''')
			pop_size1 = int(input("\nselect the size by their number:- "))

			if pop1 == 1:
				if pop_size1 == 1:
					bill = (100 + bill)
				elif pop_size1 == 2:
					bill = (100 + 50 + bill)


			if pop1 == 2:	
				if pop_size1 == 1:
					bill = (150 + bill)
				elif pop_size1 == 2:
					bill = (150 + 50 + bill)


			if pop1 == 3:	
				if pop_size1 == 1:
					bill = (200 + bill)
				elif pop_size1 == 2:
					bill = (200 + 50 + bill)


# Breaking the loop if the costmer dont want anything else
			eat_again = input("do you want something else:- ")
			if eat_again == "no":
				total = input("do you want your bill:- ")
				if total == "yes":
					if seat1 == 1:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1)
					if seat1 == 2:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2)
					if seat1 == 3:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3)
					if seat1 == 4:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4)
					if seat1 == 5:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5)
					if seat1 == 6:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5,a6)
					if food1 == 1:
						print("\nFood item taken :- Popcorn")
					if food1 == 2:
						print("\nFood item taken :- nachos")
					if food1 == 3:
						print("\nFood item taken :- cold beverges")
					print("your total is :- ",bill)
					break





		if food1 == 2:
			print('''\nwe have 2 types of nachos:
				1. cheese nachos  => 100 (50 extra for large)
				2. loded nachos   => 150 (50 extra for large)''')
				
			nac1 = int(input("\nselect the nachos by their number:- ")) 
			print('''\nwe have three sizes:
					1. medium
					2. large''')
			nac_size1 = int(input("\nselect the size by their number:- "))


			if nac1 == 1:
				if nac_size1 == 1:
					bill = (100 + bill)
				elif nac_size1 == 2:
					bill = (100 + 50 + bill)


			if nac1 == 2:
				if nac_size1 == 1:
					bill = (150 + bill)
				elif nac_size1 == 2:
					bill = (150 + 50 + bill)


# Breaking the loop if the costmer dont want anything else
			eat_again = input("do you want something else:- ")
			if eat_again == "no":
				total = input("do you want your bill:- ")
				if total == "yes":
					if seat1 == 1:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1)
					if seat1 == 2:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2)
					if seat1 == 3:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3)
					if seat1 == 4:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4)
					if seat1 == 5:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5)
					if seat1 == 6:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5,a6)
					if food1 == 1:
						print("\nFood item taken :- Popcorn")
					if food1 == 2:
						print("\nFood item taken :- nachos")
					if food1 == 3:
						print("\nFood item taken :- cold beverges")
					print("your total is :- ",bill)
					break



		if food1 == 3:
			print('''\nwe have 2 types of cold beverges:
				1. coca cola  => 50 (25 extra for large)
				2. fanta      => 50 (25 extra for large)''') 
			cold1 = int(input("\nselect the cold drink by their number:- ")) 
			print('''\nwe have three sizes:
					1. medium
					2. large''')
			cold_size1 = int(input("\nselect the size by their number:- "))


			if cold1 == 1:
				if cold_size1 == 1:
					bill = (50 + bill)
				elif cold_size1 == 2:
					bill = (50 + 25 + bill)


			if cold1 == 2:
				if cold_size1 == 1:
					bill = (50 + bill)
				elif cold_size1 == 2:
					bill = (50 + 25 + bill)


# Breaking the loop if the costmer dont want anything else
			eat_again = input("do you want something else:- ")
			if eat_again == "no":
				total = input("do you want your bill:- ")
				if total == "yes":
					if seat1 == 1:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1)
					if seat1 == 2:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2)
					if seat1 == 3:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3)
					if seat1 == 4:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4)
					if seat1 == 5:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5)
					if seat1 == 6:
						print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5,a6)
					if food1 == 1:
						print("\nFood item taken :- Popcorn")
					if food1 == 2:
						print("\nFood item taken :- nachos")
					if food1 == 3:
						print("\nFood item taken :- cold beverges")
					print("your total is :- ",bill)
					break





		elif food1 < 4:
			print("type between 1 to 4")

	else:
		total = input("do you want your bill:- ")
		if total == "yes":
			if seat1 == 1:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1)
			if seat1 == 2:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2)
			if seat1 == 3:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3)
			if seat1 == 4:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4)
			if seat1 == 5:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5)
			if seat1 == 6:
				print("Movie Plix Bill","\nname :- ",name1,"\nage :- ",age,"\nno of seat taken :- ",seat1,"\nseat number :- ",a1,a2,a3,a4,a5,a6)
			print("your total is :- ",bill)
			break
