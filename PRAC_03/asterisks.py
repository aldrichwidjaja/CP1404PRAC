pythonista = str(input("Please input any words"))
countalpha = len(pythonista)
while countalpha <6 or countalpha>12:
    print("Password doesn't meet a minimum length set by a program")
    pythonista = str(input("Please input any words"))
    countalpha = len(pythonista)
for i in range(countalpha):
    print('*', end='')