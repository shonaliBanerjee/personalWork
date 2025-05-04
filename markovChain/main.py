#Imports
import json
import logging
import random
import time

#Setup
nextWordOptions = []
valueList = {}
firstWord = ""
lineCount = 0
firstLoop = True
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'"
punctuation = ""

#logging.basicConfig(format='%(asctime)s %(message)s')
#logging.warning('is when the dictionary program began.')
with open("sherlockholmes.txt") as inputFile:
  lines = inputFile.read().split("\n")
  for line in lines:
    if line.split():
      word = line.split()[0]
      if lineCount == 0:
        firstWord = word
      lineCount += 1
    else:
      continue
with open("sherlockholmes.txt") as inputFile:
  lines = inputFile.read().split("\n")
  for line in lines:
    word = line.split()
    for word in line:
      for letter in word:
        if letter not in alphabet and letter not in punctuation:
          punctuation = punctuation + letter
        else:
          continue
      
#Import Words
lineCount = 0
with open('sherlockholmes.txt') as inputFile:
  for line in inputFile:
    firstWord = str(firstWord)
    line = line.strip()
    for i in range(0, len(line.split())):
      word = line.split()[i]
      #for letter in word:
        #if letter not in alphabet:
          #word = letter
          #break
      if lineCount == 0:
        lineCount += 1
        continue
      else:
        try:
          valueList[firstWord].append(word)
        except KeyError:
          valueList[firstWord] = [word]
      firstWord = word

#logging.basicConfig(format='%(asctime)s %(message)s')
#logging.warning('is when the dictionary program ended')

with open('output.json', 'w') as outputFile:
  json.dump(valueList, outputFile, indent = 1)

#Initalise
print("I am a Markov chain generator for the Sherlock Holmes stories by Arthur Conan Doyle.")
currentWord = input("What word do you want to start with? ")
textLength = input("How many words do you want to generate? ")

#Markov Chain
if currentWord not in valueList and currentWord.lower() not in valueList and currentWord.title() not in valueList:
  print("That word is not in my value list. Restart the program and try a new word.")
else:
  try:
    #logging.basicConfig(format='%(asctime)s %(message)s')
    #logging.warning('is when the writing program began.')
    for i in range(int(textLength)):
      if firstLoop:
        print("\n")
        if currentWord.lower() in valueList and currentWord.title() not in valueList:
          nextWordOptions.extend(valueList[currentWord.lower()])
          time.sleep(.1)
          print (currentWord, end=" ", flush = True)
        elif currentWord.title() in valueList and currentWord.lower() not in valueList:
          nextWordOptions.extend(valueList[currentWord.title()])
          time.sleep(.1)
          print (currentWord.title(), end=" ", flush = True)
        else:
          nextWordOptions.extend(valueList[currentWord])
          time.sleep(.1)
          print (currentWord, end=" ", flush = True)
        firstLoop = False
      else:
        randomLine = random.randint(0, 100)
        if randomLine == 10 or currentWord[0] == "“":
          print("\n\n")
        nextWordOptions.extend(valueList[currentWord])
        time.sleep(.1)
        print (currentWord, end=" ", flush = True)
        #if currentWord[-1] == "“":
          #print("\n\n")
      if currentWord[0] in punctuation or currentWord[-1] in punctuation:
        for k in nextWordOptions:
          for letter in k:
            if letter in punctuation:
              nextWordOptions[:] = (value for value in nextWordOptions if value != k)
              break
            else:
              continue
      if len(nextWordOptions) > 0:
        currentWord = random.choice(nextWordOptions)
      else:
        currentWord = "I"
      nextWordOptions = []
  except ValueError:
    print("Invalid input for text length. Restart the program and try another length.")
