#Lab 9
hv = input("Horizontal or Vertical? ")

num = int(input("How long? "))

sym = input("What symbol? ")

if(hv =='v'):
    for i in range(num):
        print(sym)
if(hv =='h'):
    for i in range(num): 
        print( end = sym + " " )
    
