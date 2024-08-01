import random
'''
1 for Snake
-1 for water
0 for Gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your Choice: ") #take input from user in the form of 's,g,u'.
youDict = {'s':1,'w':-1,'g':0}
reverseDict = {1:'snake',-1 :'water',0:'gun'}
you =youDict[youstr]
print(f"you choose {reverseDict[you]} \n Computer Choose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")

else:
    if(computer == -1 and you==1):
        print("you win")
    elif(computer == -1 and you==0):
        print("you lose! Try again.")
    elif(computer == 1 and you==-1):
        print("you lose! Try again.")
    elif(computer == 1 and you==0):
        print("you win!")
    elif(computer == 0 and you==-1):
        print("you win!")
    elif(computer == 0 and you==1):
        print("you lose!")
    else:
        print("Something went Wrong!!!")