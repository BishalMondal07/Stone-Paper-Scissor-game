import random
objects = ["Stone", "Paper", "Scissor"]
Comp = random.choice(objects)

S = ("Stone")
P = ("Paper")
Ss = ("Scissor")

print("Computer turn : S(for stone), P(for paper), Ss(for sicssor)")
b = input("Player 1 turn : Type S(for Stone), P(for Paper), Ss(Sicssor) :")

print("Computer played" , Comp)

if (Comp == S and b == "S") :
    print("It's a tie game !")
elif (Comp == P and b == "P") :
    print("It's a tie game !")
elif (Comp == Ss and b == "Ss") :
    print("It's a tie game !")
    
elif (Comp == P and b == "S") :
    print("Sorry, You have lost the game !")
elif (Comp == Ss and b == "P") :
    print("Sorry, You have lost the game !")
elif (Comp == S and b == "Ss") :
    print("Sorry, You have lost the game !")
    
elif (Comp == P and b == "Ss") :
    print("Congarulations, You have won the game !")
elif (Comp == Ss and b == "S") :
    print("Congarulations, You have won the game !")
elif (Comp == P and b == "S") :
    print("Congarulations, You have won the game !")

print("Thankyou For Playing !")
