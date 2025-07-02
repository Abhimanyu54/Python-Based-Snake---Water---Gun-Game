import random 

computer = random.choice([1,0,-1])
user = input("Enter Your Response: ")
dict = {"s" : 1, "w" : 0, "g" : -1}
rev_dict = {1 : "Snake", 0 : "Water", -1 : "Gun"}

you = dict[user]

print(f"The User Choosed {rev_dict[you]} and The Computer Choosed {rev_dict[computer]}")

if (computer == you):
    print("THE MATCH IS DRAW! WELL PLAYED")
else: 
    if (computer == 1 and you == -1):
        print("Congrats, You won the game")

    elif (computer == 1 and you == 0):
        print("LOOSE!! Better Luck Next Time")

    elif (computer == 0 and you == 1):
        print("Congrats, You won the game")

    elif (computer == 0 and you == -1):
        print("LOOSE!! Better Luck Next Time")

    elif (computer == -1 and you == 0):
        print("Congrats, You won the game")

    elif (computer == -1 and you == 1):
        print("LOOSE!! Better Luck Next Time")

    else:
        print("ERROR IN READING THE RESPONSE")