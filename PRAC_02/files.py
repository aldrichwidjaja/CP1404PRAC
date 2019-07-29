get_name = str(input("Enter your name: "))
outfile = open("OUTPUT_NAME.txt", mode='w')
print ("{}".format(get_name), file=outfile)
outfile.close()
#---------------------------------------------------#
if outfile.mode != "r":
    get_file = open("OUTPUT_NAME.txt", mode="r")
    content=get_file.read()
    print(content)
    get_file.close()
#---------------------------------------------------#
answer = 0
file = open("numbers.txt",mode="r")

for line in file:
    answer += (int(line))

print (answer)
file.close()
#---------------------------------------------------#
ans = 0
openfile = open("num2.txt",mode="r")
for line2 in openfile:
    edit = line2.split()
    c = [int(e) for e in edit]
    total= sum(c)
    print (total)


