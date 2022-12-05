import random

def gamewin(comp,you ):
    if comp==you:
        return None
    elif comp=='p':
        if you=='r':
             return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
             return False
        elif you=='r':
            return True
    elif comp=='r':
        if you=='s':
             return False
        elif you=='p':
            return True

print("comp turn:paper(p)  rock(r) or secissors(s)  ? ")
randno=random.randint(1,3)#random intiger
print(randno)
if randno==1:
    comp='p'
elif randno==2:
    comp='r'
elif randno==3:
    comp='s'

you=input("player :paper(p)  rock(r) or secissors(s)  ? ")

a=gamewin(comp,you)

print(f"computer choose  {comp}")
print(f"computer choose   {you}")
if a == None:
    print("the game is tie")
elif a:
    print("the winner")
else:
    print("you lose")