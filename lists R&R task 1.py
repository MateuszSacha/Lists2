#lists R&R task 1

names=[]
for count in range(8):
    name = input("Enter your name:")
    names.append(name)
for each in names:
    print(each)
change = input("name do you want to change?:")
if change == 3:
    names[3] = "michelle"
for each in names:
    print(each)
