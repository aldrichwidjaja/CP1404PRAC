price = []
numitem= int(input("Please input number of items: "))
for i in range(numitem):
    priceinput = int(input("Price of item :"))
    price.append(priceinput)
sumprice = sum(price)
if sumprice >100 :
    print("total price: ", sumprice-sumprice*0.10)
else:
    print("total price: ", sumprice)
