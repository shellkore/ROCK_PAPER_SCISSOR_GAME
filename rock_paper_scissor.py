#A SIMPLE ROCK PAPER SCISSOR GAME IN PYTHON
import random
import os
def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print("WELCOME TO ROCK PAPER AND SCISSOR GAME\n")
    print("****************RULES*******************\n")
    print("Paper vs Rock -> ROCK WINS\n")
    print("Paper vs Scissors-> SCISSORS WINS\n")
    print("Rock vs Scissors -> ROCK WINS\n")
    input("PRESS ENTER KEY TO PROCEED")
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("\t\t\tGAME MODES\n 1.PLAYER VS PLAYER\t 2.PLAYER VS COMPUTER")
        choice=int(input("Enter your Choice(1-2):"))
        while(choice !=1 and choice !=2):
            print("INVALID CHOICE\nENTER AGAIN:")
            choice=int(input())
        if(choice==1):
            print("PLAYER VS PLAYER MODE\n")
        else:
            print("PLAYER VS COMPUTER MODE\n")
        print("Enter player 1 name:")
        play_1 = input()
        if(choice==1):
            print("Enter player 2 name:")
            play_2=input()
        print("\n"+play_1, "PLAYS\n")
        movp1=int(input("1.ROCK\n2.SCISSORS\n3.PAPER\nENTER YOUR PICK:"))
        print(play_1, "PICKS:")
        if(movp1==1):
            print("ROCK")
        elif(movp1==2):
            print("SCISSORS")
        else:
            print("PAPER")
        if(choice==1):
            print("PRESS ENTER FOR",play_2+"'s TURN")
            input()
            os.system('cls' if os.name=='nt' else 'clear')
            print("\n"+play_2 ,"PLAYS\n")
            movp2=int(input("1.ROCK\n2.SCISSORS\n3.PAPER \nENTER YOUR PICK:"))
            print(play_2, " PICKS:")
            if(movp2==1):
                print("ROCK\n")
            elif(movp2==2):
                print("SCISSORS\n")
            else:
                print("PAPER\n")
            if(movp1==1 and movp2==2):
                print(play_1," WINS\n")
            elif(movp1==1 and movp2==3):
                print(play_2," WINS\n")
            elif(movp1==2 and movp2==1):
                print(play_2," WINS\n")
            elif(movp1==2 and movp2==3):
                print(play_1," WINS\n")
            elif(movp1==3 and movp2==1):
                print(play_1," WINS\n")
            elif(movp1==3 and movp2==2):
                print(play_2," WINS\n")
            else:
                print("MATCH DRAW\n")
        else:
            #generating random integer between 1 and 3(inclusive)
            movc=random.randint(1,3)
            print("COMPUTER PICKS:")
            if(movc==1):
                print("ROCK")
            elif(movc==2):
                print("SCISSORS")
            else:
                print("PAPER")
            if(movp1==1 and movc==2):
                print(play_1," WINS\n")
            elif(movp1==1 and movc==3):
                print("COMPUTER WINS\n")
            elif(movp1==2 and movc==1):
                print("COMPUTER WINS\n")
            elif(movp1==2 and movc==3):
                print(play_1," WINS\n")
            elif(movp1==3 and movc==1):
                print(play_1," WINS\n")
            elif(movp1==3 and movc==2):
                print("COMPUTER WINS\n")
            else:
                print("MATCH DRAW\n")
        print("WANT TO PLAY AGAIN(Y/N):")
        ch=input()
        if(ch=='n' or ch=='N'):
            break
    print("\nTHANKS FOR PLAYING")
main()
