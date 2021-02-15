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

#current_names = '_jim_donna_bryce_greg_joel_'
#first names
current_names = '__babe_essa_essa_cabot_ziggy_urkle_keith_flizbit_bye_mag'\
'_russell_allen_rodney_matthew_richard_sherna_shamus_wood_barrey_pu_alan_sid'\
'_paul_pud_eric_randy_sheri_bransio_rako_jane_craig_bruce_cindy_stevenip_sarai'\
'_richard_alex_margaret_sandra_laura_steve_susan_paul_irene_irene_rita_rita'\
'_rita_stephan_carl_mickey_lefke_steve_lorna_marta_lisa_marina_valerie_janet'\
'_eayan_connie_lynn_jennifer_ron_gary_sylvia_joanne_troy_malayah_karl_bob'\
'_mark_guy_helen_rebecca_tom_james_'

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
secondletter = ['_']
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
        if firstletter[m] == letter_1 and secondletter[m] == letter_2:
            break
    if firstletter[m] == letter_1 and secondletter[m] == letter_2:
        pairs[m] = pairs[m] + 1
    else:
        firstletter.append(letter_1)
        secondletter.append(letter_2)
        pairs.append(1)

#for p in range (0, len(pairs)):
#    print (firstletter[p], " ", nextletter[p], " ", pairs[p])
#print(startwith)

goagain = 'y'
while goagain == 'y':
    #enter first letter of name
    newname = '_'
    randname = 'x'
    while randname != 'y' and randname != 'n':
        randname = input("Do you want a random first letter? y or n")
        print(randname)
    if randname == 'y':
        #pick random first letter
        currentletter = letters[int(random_1()*26)+1]
        #print(currentletter)
    elif randname == 'n':
        #prompt for first letter
        currentletter = input("Enter first letter of the name")

    newname = newname + currentletter
    # generate name
    while currentletter != '_':
        # find next letter based on pairs that start with current letter
        # find how often pairs start with the letter
        for q in range (0, 27):
            if currentletter == letters[q]:
                howoften = startwith[q]
                #print(howoften)
                break
        if howoften == 0:
            #pick a random next letter
            nextletter = letters[int(random_1()*27)]
            #print(nextletter)
        else:
            #pick a random number from 1 to howoften and find nextletter
            count = int(random_1()*howoften)+1
            np = 0
            while count > 0:
                np = np+1
                if firstletter[np] == currentletter:
                    count = count - pairs[np]
            nextletter = secondletter[np]
        newname = newname + nextletter
        currentletter = nextletter
        
    print(newname)
    goagain = input("Do you want to generate another name? y or n")
        


    
        
    


