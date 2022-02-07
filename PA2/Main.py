from unicodedata import name
from DES import *
import matplotlib.pyplot as plt
import numpy as np
from inputgen import *


# print(d,"\n")
# print(np.shape(RoundCipherText))

#print(plaintexts_list)

def hamming_distance(firstlist,secondlist):                 # calculate hamming siatance between two strings / bit list
        HD=0
        for i in range(len(firstlist)):
            if firstlist[i] != secondlist[i]: 
                HD+=1
        return HD

def getAllRCText(K,plaintexts):      # get all round cipher text for all plaintext
    allRCText = []
    for Pt in plaintexts:
        D = K.encrypt(Pt)            # Encrypt with plain  text
        allRCText.append(RoundCipherText.copy())
        RoundCipherText.clear()
    return allRCText


def getHDlist(allRCText, startHD):   # generate hamming distance of base cipher text wrt to all cipher texts of 16 rounds
    HDlist = []
    HDlist.append(startHD)
    Base = allRCText[0]
    restcmp = allRCText[1:]

    for i in range(len(Base)-1):
        HD = []
        for j in range(len(restcmp)):
            HD.append(hamming_distance(Base[i],restcmp[j][i]))
        HDlist.append(HD)
    return HDlist
        



def plotgraph(X, Name):
    print(Name,"\n")
    for s,kk in enumerate(X):
        print('Round '+str(s),kk,sep=' ')
    plot_lis=tuple(X)  
    fig = plt.figure()                           # plot the box whisker plot
    plt.boxplot(plot_lis,positions=[l for l in range(0,17)])
    fig.suptitle(Name)
    plt.xlabel('Rounds')
    plt.ylabel('HD')
    fig.savefig(Name+'.png')
    plt.show()

# first experiment one base plaintext with 5 other plain text having HD 1 wrt base plaintext

nameexp1 = "Encrypting one base plaintext and 5 other \n plain text having HD 1 wrt base plaintext with common key"

# plaintext from inputgen file
plaintexts = plaintexts_list

#print(plaintexts[0])

key = b"theencky"
K = des(key=key)
# generate round cipher text

allRCText = getAllRCText(K,plaintexts)
#print(np.shape(plaintexts))
# round 0 HD = 1
HDlist = getHDlist(allRCText,[1,1,1,1,1])

plotgraph(HDlist,nameexp1)

# 2nd experiment one base plaintext with 5 other plain text having HD increasing from 1 to 5 wrt base plaintext

print("\n===========================================\n")

nameexp2 = "Encrypting one base plaintext and 5 other plain text \n having HD increasing from 1 to 5 wrt base plaintext with common key"

# plaintext from inputgen file
plaintexts = plaintexts_HD_list

#print(plaintexts[0])

key = b"theencky"
K = des(key=key)
# generate round cipher text

allRCText = getAllRCText(K,plaintexts)
#print(np.shape(plaintexts))
# round 0 HD = inc from 1 to 5
HDlist = getHDlist(allRCText,[1,2,3,4,5])

plotgraph(HDlist,nameexp2)

print("\n===========================================\n")

nameexp3 = "Encrypting one base plaintext with a base key \n and 5 keys having one HD wrt base key"

# uisng plaintext from inputgen file as keys with 1 HD
Keys = plaintexts_list 

#print(plaintexts[0])

plaintext = [b"theencky"]

# generate round cipher text
# for each key generate all round cipher text
allRCText = []
for key in Keys:
    K = des(key=key)
    allRCText.append(getAllRCText(K,plaintext)[0])


#print(np.shape(allRCText))
# round 0 HD = 0 since common PT
HDlist = getHDlist(allRCText,[0,0,0,0,0])

plotgraph(HDlist,nameexp3)



