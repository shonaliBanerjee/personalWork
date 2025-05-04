#Imports
from collections.abc import KeysView
import json
import random
import time
from collections import Counter

#Setup
nextWordOptions = []
valueList = {}
firstWord = ""
lineCount = 0
firstLoop = True
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'"

with open("essays.txt") as inputFile:
  lines = inputFile.read().split("\n")
  for line in lines:
    if line.split():
      word = line.split()[0]
      if lineCount == 0:
        firstWord = word
      lineCount += 1
    else:
      continue
      
#Import Words
lineCount = 0
with open('essays.txt') as inputFile:
  for line in inputFile:
    firstWord = str(firstWord)
    line = line.strip()
    for i in range(0, len(line.split())):
      word = line.split()[i]
      for letter in word:
        if letter not in alphabet:
          word = letter
          break
      if lineCount == 0:
        lineCount += 1
        continue
      else:
        try:
          valueList[firstWord].append(word)
        except KeyError:
          valueList[firstWord] = [word]
      firstWord = word

with open('outputE.json', 'w') as outputFile:
  json.dump(valueList, outputFile, indent = 1)

#Initalise
print("I am a Markov chain generator for assorted essays by Shonali Banerjee.")
currentWord = input("What word do you want to start with? ")
textLength = input("How many words do you want to generate? ")

#Markov Chains
allWords = [word for sublist in valueList.values() for word in sublist]
for key in allWords:
  if key[0] not in alphabet:
    allWords.remove(key)

print("\n")
for p in range(10):
  if p % 2:
    wordCounts = Counter(allWords)
    titleWord = wordCounts.most_common()[-1][0]
    print (titleWord.title(), end=" ", flush = True)
    for item in allWords:
      if item == titleWord:
        allWords.remove(item)
    del wordCounts[0]
  else:
    wordCounts = Counter(allWords)
    titleWord = wordCounts.most_common(1)[0][0]
    print (titleWord.title(), end=" ", flush = True)
    for item in allWords:
      if item == titleWord:
        allWords.remove(item)
    del wordCounts[0]
print("\n")

if currentWord not in valueList and currentWord.lower() not in valueList and currentWord.title() not in valueList:
  print("That word is not in my value list. Restart the program and try a new word.")
else:
  try:
    for i in range(int(textLength)):
      time.sleep(.1)
      if firstLoop:
        if currentWord.lower() in valueList and currentWord.title() not in valueList:
          nextWordOptions.extend(valueList[currentWord.lower()])
          print (currentWord, end=" ", flush = True)
        elif currentWord.title() in valueList and currentWord.lower() not in valueList:
          nextWordOptions.extend(valueList[currentWord.title()])
          print (currentWord.title(), end=" ", flush = True)
        else:
          nextWordOptions.extend(valueList[currentWord])
          print (currentWord, end=" ", flush = True)
        firstLoop = False
      else:
        nextWordOptions.extend(valueList[currentWord])
        print (currentWord, end=" ", flush = True)
      if currentWord not in alphabet:
        for k in nextWordOptions:
          for letter in k:
            if letter not in alphabet:
              nextWordOptions.remove(k)
              break
            break
      if len(nextWordOptions) > 0:
        currentWord = random.choice(nextWordOptions)
      else:
        currentWord = "I"
      nextWordOptions = []
  except ValueError:
    print("Invalid input for text length. Restart the program and try another length.")
