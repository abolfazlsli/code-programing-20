from datetime import datetime


def out():
    exitTime={"Exit":datetime.now()}
    return exitTime
def enter():
    enterTime={"Enter":datetime.now()}
    return enterTime
def show():
    op=open("log.txt")
    s=op.read()
    print(s)



o=open("log.txt" , "a+")

while True:
    command = input("Enter the 1 to set Enter time and set 2 for exit time: ")
    name = input ("Whats your name : ")
    o.write("name: " + name)
    if command == "1" or command == 1 : o.write(enter())
    elif command=="r":show()
    else : o.write(out())
    o.close()
