items = int(input("how many items do you want to buy"))

total = 0
for i in range (0, items):
    itemname = input("what is the item")
    price = float(input("How much is it "))
    print("thanks for purchasing"+ itemname)
    total = total + price

print("your total is:"+ str (total))