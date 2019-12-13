import functools
#from colorama import Fore, Back, Style
import json
import time
from datetime import datetime
import os
import math 
#import numpy
#_____________________________________________________________________________________________________________________
#Startup ...
os.system('rm 1234.DOR') # The removes the previous file just to keep everything clean 
display = datetime.now()
print(display)
# time variables used later in the program
hour = datetime.utcnow().hour
minit = datetime.utcnow().minute
sec = datetime.utcnow().second
print(sec)
print(minit)
print(hour)
# Opening Handshake Data.
with open("ThetaList.json", "r") as t_info:
    t_data = json.load(t_info)
    theta = t_data.get("%s" % sec)
print(theta)
#_____________________________________________________________________________________________________________________

#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return functools.reduce(lambda x,y:x+y, lst)
#_____________________________________________________________________________________________________________________

#convert hex repr to string
def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''

#_____________________________________________________________________________________________________________________
# String to intiger 
file = open("1234.rtf", "r")
s = file.read()

trasnlated = toHex(s)
refiened = toHex(trasnlated)
#print("This is the data: " + s)
#print("This is the data in Hex Format: " + trasnlated)
#print("This is the refined version: " + refiened)



file.close()
#_____________________________________________________________________________________________________________________
# Really  long number
long = 5219283133417550597608921138394131714748003987111696388844721857021695621345566328693730284546120701185550350229748838662252951341253421746795
        # Note!! Since my idea of theta is to have a changing number dependent on the data and a very large number it is computationally rigorus.
        # At the current moment python cannont handle a number that big, so I will have to shorten the lenght of the variable above to make my program work :\
#_____________________________________________________________________________________________________________________
# the encryrption process will take place here 
# RSA Encryption ...
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
# Computation for RSA TEST no.10 
p = 11
Q = 7
n = p * Q # this number should be: 77
lam_n = lcm(p-1,Q-1) # this number should be: 30
e = 19
d = e %n # this should be equal to 19 as well
# Now doing the encryption and decryption funcions
def encrypt(m):
    c = m^e%n
    return c
def decrypt(c):
    pt = c^d%lam_n
    return pt
m = int(refiened)
dat = encrypt(m)
data = dat

#answer=decrypt(c)
#print(answer)
#if answer == m:
 #   print("Sucess, Message was properally encrypted and decrypted!")
#else:
 #   print("Failure to encrypt and dectypt message.s")

 #symetric encryption ...
def Upsil(long, data):
    DaTa = str(data)
    LoNg = str(long)
    Lendata= len(DaTa)
    Upsilo = LoNg[1:Lendata]
    return Upsilo
Upsilon = Upsil(long, data)

def delt(hour,sec, Upsilon):
    deltaa =  int(Upsilon) * math.sqrt(hour*sec)
    return deltaa
delta = int(delt(hour,sec,Upsilon))
def sig(hour,minit, Upsilon):
    sigm =  int(Upsilon) * math.sqrt(minit*sec)
    return sigm
sigma = int(sig(hour,minit,Upsilon))

def symetric_encrypt(data,theta, delta, sigma):
    if theta == "+":
        EnC = data^2 + delta * sigma
    elif theta == "-":
        EnC = data^2 - delta * sigma
    elif theta == "/":
        EnC= data^2 / delta * sigma
    elif theta == "*":
        EnC = data^2 * delta * sigma
    else:
        print("Theta Error")    
    return EnC
final = symetric_encrypt(data,theta,delta,sigma)

#_____________________________________________________________________________________________________________________
# DATA WILL BE IMPUTED NTO JSON FILE HERE
cyphertext = {
         "CypherText": final,
         "Hour": hour,
         "Minute": minit,
         "seccond": sec,
         "Upsilon": Upsilon,

}
#_____________________________________________________________________________________________________________________
#Function Test
#print(final)
#______________________________________________________________________________________________________________________

# End of Program |  FILE_OUTPUT

with open('1234.JSON','w') as final_file:
    json.dump(cyphertext,final_file)