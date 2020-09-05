#!/usr/bin/env python

import random

def rpsAi(): #Method for chosing the ai play
    aiChoice = ["rock", "paper", "scissors"]
    aiSelection = random.choice(aiChoice);
    return aiSelection

def rpsPlay(userPlay, aiPlay): #method for playing the game
    if (userPlay == "rock"):
            if(aiPlay == "rock"):
                print ("Tie!")
            elif (aiPlay == "scissors"):
                print ("Player Wins!")
            else:
                print ("Computer Wins!")
    elif(userPlay == "scissors"):
            if(aiPlay == "rock"):
                print("Computer Wins!")
            elif(aiPlay == "scissors"):
                print("Tie!")
            else:
                print("Player Wins!")
    else:
            if(aiPlay == "rock"):
                print("Player Wins!")
            elif(aiPlay == "scissors"):
                print("Computer Wins")
            else:
                print ("Tie!")

def valid(userInput): #determine if the user gave a valid play
    if (userInput == "rock"):
        return True
    elif (userInput == "scissors"):
        return True
    elif (userInput == "paper"):
        return True
    else:
        return False

def play():#play the game
    userInput = raw_input ("What is your move? (rock, paper, scissors)  ")
    validInput = valid(userInput);
    while (not validInput):
        userInput = raw_input ("Please enter a valid input, Case Sensitive, (rock, paper, scissors) ")
        validInput = valid(userInput)
    ai = rpsAi();
    rpsPlay(userInput, ai)

def playAgain():#decide if you want to play again
    validInput = False;
    while(not validInput):
        play = raw_input("Would you like to play again, Yes/No? ")
        if (play == "Yes"):
            validInput = True
            return True
        elif (play == "No"):
            validInput = True
            return False;
        else:
            print ("Please enter a valid input Yes or No")
            validInput = False
        

play()
again = playAgain()

while (again == True):
     play()
     again = playAgain()
