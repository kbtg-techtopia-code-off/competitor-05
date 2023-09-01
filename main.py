import random
# Rock-paper-scissors-lizard-Spock in Python

# The key idea of this program is to equate the strings
def name_to_number(name):
    if(name == 'rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        return 0
    
# number to name function
def number_to_name(number):
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        return 'rock'
    
def play():
    
    while True:
        # play Rock-paper-scissors-lizard-Spock in Python
        # get input from player
        # show list options like 1. Rock 2. Spock 3. Paper 4. Lizard 5. Scissors
        # get input from player
        # convert name to player_number using name_to_number
        # compute random guess for comp_number using random.randrange()
        # compute difference of player_number and comp_number modulo five
        # use if/elif/else to determine winner
        # convert comp_number to name using number_to_name
        # print results
        # print a blank line to separate consecutive games


        print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
        print("1. Rock")
        print("2. Spock")
        print("3. Paper")
        print("4. Lizard")
        print("5. Scissors")
        print("6. Exit Game")

        player_choice = int(input("Enter your choice: "))
        if(player_choice == 6):
            break
        else:
            if(player_choice == 1):
                player_choice_name = 'rock'
            elif(player_choice == 2):
                player_choice_name = 'Spock'
            elif(player_choice == 3):
                player_choice_name = 'paper'
            elif(player_choice == 4):
                player_choice_name = 'lizard'
            elif(player_choice == 5):
                player_choice_name = 'scissors'
            else:
                player_choice_name = 'rock'

            print("Player chooses " + player_choice_name)
            player_number = name_to_number(player_choice_name)
            comp_number = random.randrange(0, 5)
            comp_choice_name = number_to_name(comp_number)
            print("Computer chooses " + comp_choice_name)
            difference = (comp_number - player_number) % 5
            if(difference == 0):
                print("Player and computer tie!")
            elif(difference == 1 or difference == 2):
                print("Computer wins!")
            elif(difference == 3 or difference == 4):
                print("Player wins!")
            else:
                print("Player and computer tie!")
            print("")
            print("")


def main():
    play()


if __name__ == '__main__':
    main()

            

