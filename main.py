#!/usr/bin/env python3

""" A simple 20 Questions game  

TODO
    - say "a" or "an" appropriatly
    - add more functions
    - split function out into modules
    - play with classes (maybe)
    - use SQLlite for the db
    - use a NoSQL db
    - webify with Flask
    - use github for backup
DONE
    - change to python3 - DONE
     - python3 at the top - DONE
     - print() - DONE
     - the whole utf8 thing... - DONE
    - use 'git' to track - DONE
   
"""

import json
import os
import time

happy_to_play = True
while happy_to_play:
    #
    # Start a new game...
    #
    os.system('clear')
    print("\n\n\n\n")
    print( "This is a little game. I will guess the creature that")
    print("you are thinking of in 20 questions or less!")
    print(" ")
    q = []
    # Grab database of questions from disk - or start a new one
    try:
        with open('20q.txt') as data_file:
#             q = byteify(json.load(data_file))
             q = json.load(data_file)

        pass
    except IOError as e:
        print("No saved data 20q.txt file found, so creating a new database...\n")
        # animals names in the database are all lower case, and 
        # don't include "an" or "a" 
        q.append(["Does it quack?", "duck", "pig"])

    # Inits
    curr = 0
    questions = 0
    not_there_yet = True
    happy_to_play = True

    while not_there_yet:
            questions = questions + 1
            print(q[curr][0], " - answer Y or N")
            ans = input().upper()
            if ans == "Y":
                    branch=1
            else:
                    branch=2

            # We have either a string with the name, or an int pointing 
            # to a new question..
            if isinstance (q[curr][branch], str):
                    guess = str(q[curr][branch])
                    print("I guess, a", guess, "- am I right? (Y or N)")
                    ans = input().upper()
                    if ans == "Y":
                        print("Yah! I got your animal in ", questions, " questions.\n\n\n")
                        not_there_yet = False
                    elif ans == "N":
                        print("What is it?")
                        animal = input()
                        print(animal)
                        # trim off any "a" or "an" from the answer
                        # ACTUALLY - it might be a better idea to *add* the 
                        # appropriate a/an if one isn't supplied.
                        animal_head = animal.split()[0].lower()
                        if (animal_head == "a") or (animal_head == "an"):
                            animal = ' '.join(animal.split()[1:])
                        else:
                            animal = animal

                        print("Thanks! Now, give me a new question that will be true for a", animal, " , but not for a ", q[curr][branch])
                        question = input()
                        # add in this new question
                        q.append([question, animal, guess])
                        # A little "trick" with 'len' allows us to get the 
                        # index of the item we just added                            
                        # to update the old question...
                        q[curr][branch]=len(q)-1

                        # and save the new database of questions and answers...
                        with open('20q.txt', 'w') as outfile:
                            json.dump(q, outfile)
                    else:
                            not_there_yet = False
                            print("Quitting...")

                    not_there_yet = False
                    questions = 0
                    curr = 0
                    print("\n\n\nThanks! Now, do you want to play again? (Y or N)")
                    ans = input().upper()
                    if ans == "N":
                        happy_to_play =  False
                    else:
                        print("Cool! We will restart in a second...")
                        time.sleep(2)

            else:
                            # OK, deeper down the tree.... 
                            type(q[curr][branch])
                            curr = int(q[curr][branch])
print("OK, bye!")
exit