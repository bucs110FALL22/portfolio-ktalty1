print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15) #This is a never-ending decimal

rate = input("Please input the exchange value: ")
rate = float(rate)
amount = input("Please input the amount to exchage: ")
amount = float(amount)
result = (rate * amount) - 3
print("You have recieved $", result, "back")
