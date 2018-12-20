#A SIMPLE ROCK PAPER SCISSOR GAME IN PYTHON
import random
def main():
    print("WELCOME TO ROCK PAPER AND SCISSORS GAME\n")
    print("Paper vs Rock -> ROCK WINS\n")
    print("Paper vs Scissors-> SCISSORS WINS\n")
    print("Rock vs Scissors -> ROCK WINS\n")
    while True:
        print("GAME MODES\n 1.PLAYER VS PLAYER\n 2.PLAYER VS COMPUTER")
        choice=int(input("Enter your Choice(1-2):"))
        while(choice<=0 or choice>2):
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
        print(play_1, " PLAYS\n")
        movp1=int(input("1.ROCK\n2.SCISSORS\n3.PAPER\nENTER YOUR PICK:"))
        print(play_1, "PICKS:")
        if(movp1==1):
            print("ROCK")
        elif(movp1==2):
            print("SCISSORS")
        else:
            print("PAPER")
        if(choice==1):
            print(play_2 ," PLAYS\n")
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
