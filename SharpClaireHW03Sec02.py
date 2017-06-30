# Project:      Homework 3 (SharpClaireHW03Sec02.py)
# Name:         Claire Sharp
# Date:         11/01/16
# Description:  This program allows a user to perform
#				several types of interactions with a
#				simulated bank account.

def main():
	
	# Sets variables that will be used later.
	fltAcctBal = 1000.00
	strTransaction = "null"
	intWithdrawTicker = 0
	intDepositTicker = 0
	intSCTicker = 0
	fltWithdrawAmt = 0.00
	fltDepositAmt = 0.00
	fltSCAmt = 0.00
	
	# Collects the dollar amount of the transaction.
	while strTransaction.lower() != "end":
		strTransaction = str(input("Please enter the amount of this transaction (or end to exit): $"))
		if strTransaction.lower() != "end":
			fltTransAmt = float(strTransaction)
			print()
			
			# If the transaction amount is valid, collects the transaction type.
			if fltTransAmt > 0.00:
				strTransType = str(input("What type of transaction would you like to perform? "))
				print()
				
				# Handy help command, telling you your options!
				while strTransType.lower() == "help":
					print("Transaction options: deposit, withdraw, servicecharge")
					print()
					strTransType = str(input("What type of transaction would you like to perform? "))
			
				# Handles deposits. Simple enough.
				if strTransType.lower() == "deposit":
					fltAcctBal += fltTransAmt
					intDepositTicker += 1
					fltDepositAmt += fltTransAmt
					print("Deposit received. ", intDepositTicker, " deposits processed for a total of $", fltDepositAmt, ".")
					print("Your updated balance is: $", fltAcctBal)
					print()
			
				# Handles withdrawal, likewise.
				elif strTransType.lower() == "withdraw":
					if fltAcctBal >= fltTransAmt:
						fltAcctBal -= fltTransAmt
						intWithdrawTicker += 1
						fltWithdrawAmt += fltTransAmt
						print("Withdrawal received. ", intWithdrawTicker, " withdrawals processed for a total of $", fltWithdrawAmt, ".")
						print("Your updated balance is: $", fltAcctBal)
						print()
										
					# Charges a $10 service charge if there are insufficient funds for a withdrawal.
					else:
						fltAcctBal -= 10.00
						fltSCAmt += 10.00
						intSCTicker += 1
						print("Error: Insufficient funds. A service charge has been collected.")
						print(intSCTicker, " service charges processed, for a total of $", fltSCAmt, ".")
						print("Your updated balance is: $", fltAcctBal)
						print()
			
				# Handles manual service charges.
				elif strTransType.lower() == "servicecharge":
					fltAcctBal -= fltTransAmt
					fltSCAmt += fltTransAmt
					intSCTicker += 1
					print("Thank you, service charge deducted.")
					print(intSCTicker, " service charges processed, for a total of $", fltSCAmt, ".")
					print("Your updated balance is: $", fltAcctBal)
					print()
				
				# Error handler for unknown inputs.
				else:
					print("ERROR: UNKNOWN COMMAND - ", strTransType)
					print()
			
			# Error handler for zero or negative transactions.
			else:
				print("ERROR: INVALID TRANSACTION AMOUNT.")
				print()
		
		# Closing text once the user ends the program.
		else:
			print("Total No. of deposits: ", intDepositTicker)
			print("Total No. of withdrawals: ", intWithdrawTicker)
			print("Total No. of service charges: ", intSCTicker)
			print("Total depositted: $", fltDepositAmt)
			print("Total withdrawn: $", fltWithdrawAmt)
			print("Total collected from service charges: $", fltSCAmt)
			print("Final account balance: $", fltAcctBal)
			print()
			print("Thank you, and have a wonderful day!")
main()
