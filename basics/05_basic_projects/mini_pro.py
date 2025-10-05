## stone paper seisor game ##

import random

dict={"s":1, "p":0, "si":-1,}
revdict={1:"stone",0:"paper",-1:"scissor"}

def game_intro():
    print("="*41)
    print("🎮 Welcome to Stone, Paper, Scissor Game!")
    print("="*41)
    print("-"*42)
    print("INSTRUCTION:")
    print("🏁 The Tournament is of 10 rounds")
    print("Choose from (s=stone, p=paper , si=scissor)")
    print("Type 'exit' to leave the game")
    print("-"*42)

def play_game():
    rounds = 0
    max_rounds = 10
    wins=0
    losses=0
    draws=0

    while True:
        if rounds >= max_rounds:
            print("\n"+"🏁"*31)
            print("🏁 10 rounds completed.")
            print(f"✅ Wins: {wins}")
            print(f"❌ Losses: {losses}")
            print(f"🤝 Draws: {draws}")
            if(wins>losses):
                print(f"📊 Final decision: you win the tournament by {wins} wins.")
            elif(wins<losses):
                print(f"📊 Final decision: you lose the tournament by {losses} losses.")
            else:
                print(f"📊 Final decision: The tournament is draw by {wins} wins & {losses} losses")
            print(f"👋 Thankyou you for playing!")
            print("🏁"*31)
            break
        print("\n")
        comp=random.choice([1,0,-1])
        youstr=input(f"Round {rounds+1} - Enter your choice:").strip().lower()
        
        if(youstr=="exit"):
            print("\n"+"🏁"*31)
            print("Exited manually.")
            print(f"✅ Wins: {wins}")
            print(f"❌ Losses: {losses}")
            print(f"🤝 Draws: {draws}")
            if(wins>losses):
                print(f"📊 Final decision: you win the tournament by {wins} wins.")
            elif(wins<losses):
                print(f"📊 Final decision: you lose the tournament by {losses} losses.")
            elif(wins==losses):
                print(f"📊 Final decision: The tournament is draw by {wins} wins & {losses} losses")
            print(f"👋 Thankyou you for playing!")
            print("🏁"*31)
            break

        
        if youstr not in dict:
            print("❌ Invalid input. Please enter 's=stone', 'p=paper', or 'si=scissor'.")
            continue

        you= dict[youstr]
        print(f"🧑 Your choice: {revdict[you]}\n💻 Computer's choice: {revdict[comp]}")

        if (comp==you):
            print("it's a draw 🤝.")
            draws+=1 
        elif (comp==1 and you==0)or\
                (comp==0 and you==-1)or\
                (comp==-1 and you==1):
            print("you win! ✅")
            wins+=1  
        else:
            print("you lose! ❌")
            losses+=1

        rounds += 1  

def replay():
    while True:
        reply=input("Do you want to play again? (yes/no): ").strip().lower()
        if reply=="yes":
            return True
        elif reply=="no":
            print("See you again!")
            return False
        else:
            print("Please enter yes or no.")

while True:
    game_intro()
    play_game()
    if not replay():
        break

