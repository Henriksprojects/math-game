# -*- coding: utf-8 -*-
from random import randint
import sys, os
# print("Multiplikations-spelet")

os.system('clear')
print("Välkommen till Multiplikations-spelet ! \n")




def choose_tabell(prompt):
    while True:
        try:
            tabell = int(input(prompt))
        except ValueError:
            print("Du måste skriva in ett tal.")
            continue

        if tabell < 0:
            print("Du måste skriva ett positivt tal.")
            continue
        else:
            return tabell
            break


# print "tabell: %s" % tabell
def calculate(tabell, randomnr):
        right_answer = tabell * randomnr
        # print "right_answer: %s" % right_answer
        return right_answer

def get_answer(tabell, randomnr):
    while True:
        try:
            your_answer = int(input('%s * %s?  \n' % (tabell, randomnr)))
        except ValueError:
            print("Du måste skriva in ett tal.")
            continue

        if your_answer < 0:
            print("Du måste skriva ett positivt tal.")
            continue
        else:
            break
    return your_answer
    # your_answer = input('%s * %s? \n' % (tabell, randomnr))

def practice_5(tabell):
    count = 0
    number_of_right_answers = 0
    while count < 75:
        randomnr = randint(0, 9)
        # print "randomnr: %s" % randomnr
        right_answer = calculate(tabell, randomnr)
        # print("%s * %s ?  " % (tabell, randomnr))
        your_answer = get_answer(tabell, randomnr)
        if your_answer == right_answer:
            number_of_right_answers += 1
            print("Rätt!")
        else:
            print ("Fel! Rätt svar är: %s" % right_answer)
        count += 1  # This is the same as count = count + 1
    return number_of_right_answers  

def print_score(rights):
      if rights == 75:
          print("ALLA RÄTT !!!! ")
      else:
          print("Antal Rätt %s." % rights)

# Main program starts here
tabell = choose_tabell("Vilken tabell vill du öva på?  \n")
rights = practice_5(tabell)
print_score(rights)
