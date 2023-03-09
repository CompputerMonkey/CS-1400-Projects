investmentAmount = int(input("enter starting investment ammount: "))
paymentAmount = int(input("enter the monthly payment amount: "))
monthlyIntrestRate = int(input("enter anual intrest rate: "))/12
numMonths = int(input("enter how many years: "))*12
monthlyIntrestRate *= 0.01

futureValue = (investmentAmount * (1+monthlyIntrestRate)**numMonths) + (paymentAmount * (((1+monthlyIntrestRate)**numMonths-1) / monthlyIntrestRate) * (1+monthlyIntrestRate))

print(futureValue)