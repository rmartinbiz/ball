import pandas as pd
#may not need these- test to clarify!!!
import linecache
import random

# Use this for multi value dict for player positions https://thispointer.com/python-dictionary-with-multiple-values-per-key/

#
def inningPopulate(num_players, num_innings):
    print("Yes you hit the inningPopulate function, innings are ", num_innings)
    return()

def whosMissing(missingKids):
    while missingKids>0:
        kidcount=1
        absentKid = str(input("Who's missing kid # xx ")) #get name of missing kid and iterate
        print(absentKid)
        kidcount +=1
        missingKids-=1
        #flip availabilitry of missing kid 1 in df_thunder to no
        #ENHANCEMENT- print "set availability of missing kid n to no"
    return()

expected_players = int(input("Hello, how many players are you expecting to play today? "))
# print (expected_players)
if expected_players < 12:
    whosMissing(12-expected_players)

expected_innings = int(input("...and how many innings do you want me to draft? "))
print (expected_innings)


#inningPopulate(expected_players, expected_innings)

#num_missing_players = 12-total_players
#while loop to gather the first name of missing players- repeat missing_player # of times
# name_missing_player_ =  tuple(input("enter the name of X player AND LOOP X num times? "))
## mark missing player with Y in absent field

#ENHANCEMENT- could total players by number of rows in player column
#Enahancvement- move from XLS to liteweight DB