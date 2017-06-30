# Project:      Homework No. 4 (SharpClaireHW04Sec02.py)
# Name:         Claire "Boof" Sharp
# Date:         11/14/16
# Description:  This program grabs the user's preferred coffee, 
#				weight, location, and shipping methood, then
#				sends that information to S&H, tax, and subTotal
#				to calculate the order costs, then prints the
#				final costs to the user.

def main():
	# Formalities!
	print("Welcome to Konditorei Coffee!")
	
	# Determines the user's coffee preference.
	strCoffeeType = "Null"
	while strCoffeeType == "Null":
		strCoffeeType = str(input("Would you like Jonestown Brew (JB) or Plymoth Jolt (PJ)? "))
		if strCoffeeType.upper() in ["JB", "PJ"]:
			strCoffeeType = strCoffeeType.upper()
		else:
			print("Invalid input! You must choose either JB or PJ.")
			strCoffeeType = "Null"
		print()
	
	# Determines the weight desired
	fltWeight = 0.0
	while fltWeight == 0.0:
		try:
			fltWeight = float(input("How many pounds of coffee would you like? "))
			if fltWeight > 0.0:
				fltWeight = fltWeight
			else:
				print("You must select a positive order amount.")
				fltWeight = 0.0
		except ValueError:
			print("Please use only numerical values, with or without decimals.")
		print()
	
	# Determines the shipping method
	strShipMethod = "Null"
	while strShipMethod == "Null":
		strShipMethod = str(input("Would you like to use overnight(ON), two-day(2D), or standard(ST) shipping? "))
		if strShipMethod.upper() in ["ON", "2D", "ST"]:
			strShipMethod = strShipMethod.upper()
		else:
			print("Invalid input. Please choose ON, 2D or ST.")
			strShipMethod = "Null"
		print()
	
	# Determines shipping location.
	strShipCity = str(input("What city is the order being shipped to? "))
	strShipState = str(input("And to which state? (e.g. AK, MA, WA etc) "))
	
	# Determine payment type.
	strPayType = "Null"
	while strPayType == "Null":
		strPayType = str(input("How would you like to pay? Paypal(PP), Credit(CC) or Check(CK)? "))
		if strPayType.upper() == "PP":
			fltPayCost = 1.03
		elif strPayType.upper() == "CC":
			fltPayCost = 1.05
		elif strPayType.upper() == "CK":
			fltPayCost = 0.98
		else:
			print("Invalid input. Please choose PP, CC, or CK.")
			strPayType = "Null"
		print()
	
	fltTax = tax(strShipState)
	fltSnH = SnH(fltWeight, strShipMethod)
	fltSubtotal = subTotal(strCoffeeType, fltWeight, fltTax, fltPayCost)
	
	# Prints all pertinent info. Not bothering to expand the payment type or shipping method because why.
	if strCoffeeType == "JB":
		print("Your order of ", fltWeight, "pounds of Jonestown Brew via ", strPayType, "has been processed.")
	else:
		print("Your order of", fltWeight, "pounds of Plymoth Jolt via", strPayType, "has been processed.")
	print("Costs of shipping", strShipMethod, "to", strShipCity, ", ", strShipState, ":")
	print("Subtotal: $", fltSubtotal)
	print("---- Tax: $", round(((fltSubtotal / fltTax) * (fltTax - 1)),2))
	print("Shipping: $", fltSnH)
	print("-- Total: $", round((fltSubtotal + fltSnH),2))

def SnH(fltWeight, strShipMethod):
	# Determines cost of shipping.
	if strShipMethod == "ON":
		return round((20.00 + 2.50 + (0.93 * fltWeight)), 2)
	elif strShipMethod == "2D":
		return round((13.00 + 2.50 + (0.93 * fltWeight)), 2)
	else:
		return round((2.50 + (0.93 * fltWeight)),2)

def tax(strShipState):
	# Determines tax, based on user's state.
	if strShipState in ["WA", "CA", "TX"]:
		return 1.09
	elif strShipState in ["OR", "FL"]:
		return 1.00
	else:
		return 1.07
	
def subTotal(strCoffeeType, fltWeight, fltTax, fltPayCost):
	# Determines subtotal given most of the user inputs.
	if strCoffeeType == "JB":
		return round(((10.50 * fltWeight) * fltPayCost * fltTax), 2)
	else:
		return round(((16.95 * fltWeight) * fltPayCost * fltTax), 2)
main()
