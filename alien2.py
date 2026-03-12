#Matthew Cerniglia. Complete Project
#This program is a game that is played by choosing from given colors to gain points. The game can be can be continued to keep adding points and will end when done playing.
print('')
print('ALIENS HAVE INVADED, CHOOSE WHAT COLOR ALIEN TO CATCH AND EARN POINTS') #intro
player_score=0 #sets player score to 0
print('') #spacing
def play_game(): #is the function for the actual game. gives options of colors to chose from. takes in player score and adds certain amount depending on player input
    global player_score 
    print("Player please choose what alien to capture: Blue, Purple, or Orange") 
    color = input().capitalize()
    if color == 'Blue': 
        player_score += 10
        print('+10')
    elif color == 'Orange': 
        player_score += 20
        print('+20')
    elif color == 'Purple': 
        player_score += 30
        print('+30')
    else:                   #if one of the three choices weren't put in, nothing is added.
        print("Wrong Answer, No Points")
while True:                 #is the loop to continue playing the game. Condition of Y to be met to keep playing. 15 second timer before cmd window closes. Displays score between rounds and at end.
    play_game()
    print(f'Your Score: {player_score}') 
    answer = input('Play Again? Y/N:').upper() 
    if answer != 'Y': 
        print(f'Final Score: {player_score}, Thanks for Playing!')
        exit(0)
        

    
                

