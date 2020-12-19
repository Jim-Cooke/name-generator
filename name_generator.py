# Name Generator program
# import library with random function
import random
import time
import math
import array

#build 27x27 table of letters in names and letters that follow
# _ to z
# OR
# use table of firstletter, nextletter, number
# (a,b)= number of times b comes after a in words
# (a,b)=1 initial value
# startwith[] = total number of pairs that start with that letter
#use random number rand()*startwith[n] to find the letter after n

#my random function
def random_1 ():
    r = random.random()
    t = time.time()
    # print(r, " ", t)
    rs = r + t
    # print(rs)
    rs = rs - math.floor(rs)
    return rs

current_names = '_carol_alice_bob_bill_'

letters = '_abcdefghijklmnopqrstuvwxyz'
startwith = [0]
for n in range (0, 27):
    startwith.append(0)

# print(startwith)

#fill 27x27 table
#grid = {}
#for n in range (0, 27):
#    for m in range (0, 27):
#        grid[(n, m)]=1

firstletter = ['_']
nextletter = ['_']
pairs = [0]
#append to these three lists

for n in range (0, len(current_names)-1):
    letter_1 = current_names[n]
    letter_2 = current_names[n+1]
    #list of how often a letter is first in a pair
    for q in range (0, 27):
        if letter_1 == letters[q]:
            startwith[q] = startwith[q] + 1
            break
    # print(letter_1)
    # create table of pairs and how often they occur
    for m in range (0, len(pairs)):
        if firstletter[m] == letter_1 and nextletter[m] == letter_2:
            break
    if firstletter[m] == letter_1 and nextletter[m] == letter_2:
        pairs[m] = pairs[m] + 1
    else:
        firstletter.append(letter_1)
        nextletter.append(letter_2)
        pairs.append(1)

#for p in range (0, len(pairs)):
#    print (firstletter[p], " ", nextletter[p], " ", pairs[p])
#print(startwith)

#enter first letter of name
newname = '_'
randname = 'x'
while randname != 'y' and randname != 'n':
    randname = input("Do you want a random first letter?")
    #print(randname)
if randname == 'y':
    #pick random first letter
    currentletter = letters[int(random_1()*26)+1]
elif randname == 'n':
    #prompt for first letter
    currentletter = input("Enter first letter of the name")

newname = newname + currentletter

#print(newname)

        


    
        
    


