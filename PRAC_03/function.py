def main():
    countalpha = do_stuff()
    count = len(countalpha)
    while count < 6 or count > 12:
        print("Invalid password! Password must be between 6 and 12")
        countalpha = do_stuff()
        count = len(countalpha)
    for i in range(count):
        print('*', end='')


def do_stuff():
    pythonista = str(input("Please input any words"))
    return pythonista

main()