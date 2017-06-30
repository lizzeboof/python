# Project:      Lab 5 (SharpClaireLab05Sec02.py)
# Name:         Claire Sharp
# Date:         24/10/16
# Description:  The program "NumeroLogic" gathers the user's name
#				and outputs the "score" of its letters combined,
#				where "a"=1, "b"=2, "d"=4 etc...
#
#				The program "WordCalc" gathers a sentence input,
#				parses it, and then outputs the average word length
#				in that sentence.

def NumeroLogic():
	
    # Collects the user's name.
    strUserName = str(input("Please enter your name: ")).lower()
    intNameScore = 0

    # Converts each letter to a nominal value
    # (ord follows in alphebetical order, starting at 97)
    for i in strUserName:
        intNameScore += ord(i) - 96

    # Prints the nominal value of the user's name, then bids them adieu.
    print("The numerical value of your name is ", intNameScore, ".")
    print("Thanks and have a nice day.")

    # Test data:
    # Kate = 11+1+20+5 = 37
    # Jerry = 10+5+18+18+25 = 76
    # Bob = 2+15+2 = 19

def WordCalc():
	
	# Setting a running total.
	intLetterTotal = 0
	
	# Collects the user's input in the form of a sentence.
	strUserSentence = str(input("What is the sentence you would like to calculate? : "))
	
	# Splits the sentence into words and then counts the words in it.
	lstUsrSentCut = strUserSentence.split()
	intWordTotal = len(lstUsrSentCut)
	
	# Counts the total number of letters in the sentence.
	for i in lstUsrSentCut:
		intLetterTotal += len(i)
	
	# Prints the length of the input, in words and characters, 
	# then calculating and then printing the average.
	print ("Your sentence was ", intLetterTotal, " characters.")
	print ("With ", intWordTotal, " words.")
	intLetterAvg = intLetterTotal / intWordTotal
	print ("And your average word length was ", round(intLetterAvg, 2), ".")
	
	# TEST DATA
	# "Now I am become death destroyer of worlds"
	# - 34 letters, 8 words. Avg: 4.25
	# "No man should escape our universities without knowing how little he knows"
	# - 62 letters, 12 words. Avg: 5.17
	
WordCalc()
