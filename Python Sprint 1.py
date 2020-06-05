# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03   06:25:09 2020

@author: Thamsanqa
"""

#Function to return DNA slc sequences.
def translateThat(seq):
    table = {
            'ATT':'I', 'ATC':'I', 'ATA':'I',
            'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'TTA':'L','TTG':'L',
            'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
            'TTT':'F', 'TTC':'F',
            'ATG':'M'
            }
    DNA = ""    

    #The if statement reads the table and get the length of the string. If it is divisible by 3 and not 0 it will match it to a codon up in the table and return its letter. 
    if len(seq):
        if len(seq)%3 != 0:
            seq = seq[0:-1]
            if len(seq)%3 != 0:
                seq = seq[0:-1]
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            DNA += table[codon]
            try:    #This is for when the user enters a codon that is not on the table it will return X
                DNA += table[codon]
            except:
                DNA += "X"
    return DNA

#Requires the user's input to put codon
DNAInput = input("Enter DNA sequence (e.g ATTCTCATA):   ")

#This prints the translated user input
print(translateThat(DNAInput))

#Function identifies the first occurrence of the lowercase a in the DNA file and changes it to A and T then prints it out to text files
def mutate():
    DNA = open("DNA.txt","r")
    normDna = open('normalDNA.txt','w')

    normalDNA = DNA.read().replace('a','A')
    normalDnaCopy = normDna.write(normalDNA)

    print(normalDNA)

    DNA.close()
    normDna.close()

    DNA = open("DNA.txt", "r")
    muteDna = open('mutatedDNA.txt','w')

    mutateDNA = DNA.read().replace('a','T')
    mutateDnaCopy = muteDna.write(mutateDNA)

    print(mutateDNA)

    DNA.close
    muteDna.close()

#This is the transalate function.
def txtTranslate(inputFile):
    readVar = txtTranslate(read_seq(inputFile))
    print(readVar)
    return readVar

#This function opens up a file and reads the input
def read_seq(inputFile):
    with open(inputFile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    return seq


txtTranslate("normalDNA.txt")
txtTranslate("mutatedDNA.txt") 