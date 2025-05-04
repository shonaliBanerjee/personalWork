#Imports
import random
from collections import Counter

#Variables
people = []
userPeople = []
eliminate = []
userEliminate = []
computerRounds = 0
humanRounds = 0

wrongEye = []
wrongHair = []
wrongAccessory = []
wrongLength = []
wrongShirt = []
wrongMood = []
wrongShape = []

bestEye = []
bestHair = []
bestAccessory = []
bestLength = []
bestShirt = []
bestMood = []
bestShape = []

correctPerson = []
correctName = ""
correctEye = ""
correctHair = ""
correctAccessory = ""
correctLength = ""
correctShirt = ""
correctMood = ""
correctShape = ""

humanWrongEye = []
humanWrongHair = []
humanWrongAccessory = []
humanWrongLength = []
humanWrongShirt = []
humanWrongMood = []
humanWrongShape = []

humanBestEye = []
humanBestHair = []
humanBestAccessory = []
humanBestLength = []
humanBestShirt = []
humanBestMood = []
humanBestShape = []

humanEyeGuess = ""
humanHairGuess = ""
humanAccessoryGuess = ""
humanLengthGuess = ""
humanShirtGuess = ""
humanMoodGuess = ""
humanShapeGuess = ""

#Setup Dictionaries
with open('people.txt') as peopleFile:
  for line in peopleFile:
    line = line.strip()
    parts = line.split(",")
    people.append(parts)

userPeople = people.copy()

eyeColours = [people[i][1] for i in range(0, len(people) - 1)]
eyeColours = list(set(eyeColours))
hairColours = [people[i][2] for i in range(0, len(people) - 1)]
hairColours = list(set(hairColours))
accessories = [people[i][3] for i in range(0, len(people) - 1)]
accessories = list(set(accessories))
hairLengths = [people[i][4] for i in range(0, len(people) - 1)]
hairLengths = list(set(hairLengths))
shirtTypes = [people[i][5] for i in range(0, len(people) - 1)]
shirtTypes = list(set(shirtTypes))
moods = [people[i][6] for i in range(0, len(people) - 1)]
moods = list(set(moods))
faceShapes = [people[i][7] for i in range(0, len(people) - 1)]
faceShapes = list(set(faceShapes))

#Pick Person
correctPerson = random.choice(people)
correctName = correctPerson[0]
correctEye = correctPerson[1]
correctHair = correctPerson[2]
correctAccessory = correctPerson[3]
correctLength = correctPerson[4]
correctShirt = correctPerson[5]
correctMood = correctPerson[6]
correctShape = correctPerson[7]


#Functions
def guessEyeColour():
  smartEye = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestEye.append(people[i][1])
      eyeGuess = Counter(bestEye).most_common(1)[0][0]

  else:
    if smartEye != 0:
      for i in range(0, len(people) - 1):
        bestEye.append(people[i][1])
        eyeGuess = Counter(bestEye).most_common(1)[0][0]
    else:
      while True:
        eyeGuess = random.choice(eyeColours)
        if eyeGuess in wrongEye:
          continue
        else:
          break
  return eyeGuess


def guessHairColour():
  smartHair = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestHair.append(people[i][2])
      hairGuess = Counter(bestHair).most_common(1)[0][0]

  else:
    if smartHair != 0:
      for i in range(0, len(people) - 1):
        bestHair.append(people[i][2])
        hairGuess = Counter(bestHair).most_common(1)[0][0]
    else:
      while True:
        hairGuess = random.choice(hairColours)
        if hairGuess in wrongHair:
          continue
        else:
          break
  return hairGuess


def guessAccessory():
  smartAccessory = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestAccessory.append(people[i][3])
      accessoryGuess = Counter(bestAccessory).most_common(1)[0][0]

  else:
    if smartAccessory != 0:
      for i in range(0, len(people) - 1):
        bestAccessory.append(people[i][3])
        accessoryGuess = Counter(bestAccessory).most_common(1)[0][0]
    else:
      while True:
        accessoryGuess = random.choice(accessories)
        if accessoryGuess in wrongAccessory:
          continue
        else:
          break
  return accessoryGuess


def guessHairLength():
  smartLength = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestLength.append(people[i][4])
      lengthGuess = Counter(bestLength).most_common(1)[0][0]

  else:
    if smartLength != 0:
      for i in range(0, len(people) - 1):
        bestLength.append(people[i][4])
        lengthGuess = Counter(bestLength).most_common(1)[0][0]
    else:
      while True:
        lengthGuess = random.choice(hairLengths)
        if lengthGuess in wrongLength:
          continue
        else:
          break
  return lengthGuess


def guessShirtType():
  smartShirt = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestShirt.append(people[i][5])
      shirtGuess = Counter(bestShirt).most_common(1)[0][0]

  else:
    if smartShirt != 0:
      for i in range(0, len(people) - 1):
        bestShirt.append(people[i][5])
        shirtGuess = Counter(bestShirt).most_common(1)[0][0]
    else:
      while True:
        shirtGuess = random.choice(shirtTypes)
        if shirtGuess in wrongShirt:
          continue
        else:
          break
  return shirtGuess


def guessMood():
  smartMood = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestMood.append(people[i][6])
      moodGuess = Counter(bestMood).most_common(1)[0][0]

  else:
    if smartMood != 0:
      for i in range(0, len(people) - 1):
        bestMood.append(people[i][6])
        moodGuess = Counter(bestMood).most_common(1)[0][0]
    else:
      while True:
        moodGuess = random.choice(moods)
        if moodGuess in wrongMood:
          continue
        else:
          break
  return moodGuess


def guessFaceShape():
  smartShape = random.randint(0, 9)

  if len(people) <= 10:
    for i in range(0, len(people) - 1):
      bestShape.append(people[i][7])
      shapeGuess = Counter(bestShape).most_common(1)[0][0]

  else:
    if smartShape != 0:
      for i in range(0, len(people) - 1):
        bestShape.append(people[i][7])
        shapeGuess = Counter(bestShape).most_common(1)[0][0]
    else:
      while True:
        shapeGuess = random.choice(faceShapes)
        if shapeGuess in wrongShape:
          continue
        else:
          break
  return shapeGuess


def askEyeColour():
  global computerRounds
  if len(wrongEye) < len(eyeColours) - 1:
    while True:
      eyeAnswer = input(f"\nDoes your character have {eyeGuess} eyes?\n")
      eyeAnswer = eyeAnswer.lower()

      if eyeAnswer == "yes" or eyeAnswer == "no" or eyeAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in eyeColours:
      if i not in wrongEye:
        eyeAnswer = "none"
  computerRounds += 1
  return eyeAnswer


def askHairColour():
  global computerRounds
  if len(wrongHair) < len(hairColours) - 1:
    while True:
      hairAnswer = input(f"\nDoes your character have {hairGuess} hair?\n")
      hairAnswer = hairAnswer.lower()

      if hairAnswer == "yes" or hairAnswer == "no" or hairAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in hairColours:
      if i not in wrongHair:
        hairAnswer = "none"
  computerRounds += 1
  return hairAnswer


def askAccessory():
  global computerRounds
  if len(wrongAccessory) < len(accessories) - 1:
    while True:
      if accessoryGuess == "glasses" or accessoryGuess == "earrings":
        accessoryAnswer = input(
            f"\nIs your character's accessory {accessoryGuess}?\n")
      elif accessoryGuess == "none":
        accessoryAnswer = input("\nDoes your character have no accessory?\n")
      else:
        accessoryAnswer = input(
            f"\nIs your character's accessory a {accessoryGuess}?\n")
      accessoryAnswer = accessoryAnswer.lower()

      if accessoryAnswer == "yes" or accessoryAnswer == "no" or accessoryAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in accessories:
      if i not in wrongAccessory:
        accessoryAnswer = "none"
  computerRounds += 1
  return accessoryAnswer


def askHairLength():
  global computerRounds
  if len(wrongLength) < len(hairLengths) - 1:
    while True:
      if lengthGuess == "braided":
        lengthAnswer = input(f"\nIs your character's hair {lengthGuess}?\n")
      elif lengthGuess == "medium":
        lengthAnswer = input(
            f"\nDoes your character have {lengthGuess} length hair?\n")
      else:
        lengthAnswer = input(
            f"\nDoes your character have {lengthGuess} hair?\n")
      lengthAnswer = lengthAnswer.lower()

      if lengthAnswer == "yes" or lengthAnswer == "no" or lengthAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in hairLengths:
      if i not in wrongLength:
        lengthAnswer = "none"
  computerRounds += 1
  return lengthAnswer


def askShirtType():
  global computerRounds
  if len(wrongShirt) < len(shirtTypes) - 1:
    while True:
      if shirtGuess == "unbuttoned":
        shirtAnswer = input(f"\nIs your character's shirt {shirtGuess}?\n")
      elif shirtGuess == "tank":
        shirtAnswer = input(
            f"\nIs your character's shirt a {shirtGuess} top?\n")
      elif shirtGuess == "hoodie":
        shirtAnswer = input(f"\nIs your character wearing a {shirtGuess}?\n")
      else:
        shirtAnswer = input(f"\nIs your character's shirt a {shirtGuess}?\n")
      shirtAnswer = shirtAnswer.lower()

      if shirtAnswer == "yes" or shirtAnswer == "no" or shirtAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in shirtTypes:
      if i not in wrongShirt:
        shirtAnswer = "none"
  computerRounds += 1
  return shirtAnswer


def askMood():
  global computerRounds
  if len(wrongMood) < len(moods) - 1:
    while True:
      moodAnswer = input(f"\nIs your character {moodGuess}?\n")
      moodAnswer = moodAnswer.lower()

      if moodAnswer == "yes" or moodAnswer == "no" or moodAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in moods:
      if i not in wrongMood:
        moodAnswer = "none"
  computerRounds += 1
  return moodAnswer


def askFaceShape():
  global computerRounds
  if len(wrongShape) < len(faceShapes) - 1:
    while True:
      shapeAnswer = input(f"\nDoes your character have a {shapeGuess} face?\n")
      shapeAnswer = shapeAnswer.lower()

      if shapeAnswer == "yes" or shapeAnswer == "no" or shapeAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in faceShapes:
      if i not in wrongShape:
        shapeAnswer = "none"
  computerRounds += 1
  return shapeAnswer


def eliminatePerson(entry, randomQuestion):
  if randomQuestion == 0:
    if eyeAnswer == "yes" and entry[1] != eyeGuess:
      eliminate.append(entry)
    elif eyeAnswer == "no" and entry[1] == eyeGuess:
      eliminate.append(entry)

  elif randomQuestion == 1:
    if hairAnswer == "yes" and entry[2] != hairGuess:
      eliminate.append(entry)
    elif hairAnswer == "no" and entry[2] == hairGuess:
      eliminate.append(entry)

  elif randomQuestion == 2:
    if accessoryAnswer == "yes" and entry[3] != accessoryGuess:
      eliminate.append(entry)
    elif accessoryAnswer == "no" and entry[3] == accessoryGuess:
      eliminate.append(entry)

  elif randomQuestion == 3:
    if lengthAnswer == "yes" and entry[4] != lengthGuess:
      eliminate.append(entry)
    elif lengthAnswer == "no" and entry[4] == lengthGuess:
      eliminate.append(entry)

  elif randomQuestion == 4:
    if shirtAnswer == "yes" and entry[5] != shirtGuess:
      eliminate.append(entry)
    elif shirtAnswer == "no" and entry[5] == shirtGuess:
      eliminate.append(entry)

  elif randomQuestion == 5:
    if moodAnswer == "yes" and entry[6] != moodGuess:
      eliminate.append(entry)
    elif moodAnswer == "no" and entry[6] == moodGuess:
      eliminate.append(entry)

  elif randomQuestion == 6:
    if shapeAnswer == "yes" and entry[7] != shapeGuess:
      eliminate.append(entry)
    elif shapeAnswer == "no" and entry[7] == shapeGuess:
      eliminate.append(entry)


def checkEyeAnswer():
  if eyeAnswer == "yes":
    #print ("\nI guessed eye colour right!")
    for i in eyeColours:
      if i != eyeGuess:
        wrongEye.append(i)
  elif eyeAnswer == "no":
    #print ("\nI guessed eye colour wrong.")
    wrongEye.append(eyeGuess)


def checkHairAnswer():
  if hairAnswer == "yes":
    #print ("\nI guessed hair colour right!")
    for i in hairColours:
      if i != hairGuess:
        wrongHair.append(i)
  elif hairAnswer == "no":
    #print ("\nI guessed hair colour wrong.")
    wrongHair.append(hairGuess)


def checkAccessoryAnswer():
  if accessoryAnswer == "yes":
    #print ("\nI guessed accessory type right!")
    for i in accessories:
      if i != accessoryGuess:
        wrongAccessory.append(i)
  elif accessoryAnswer == "no":
    #print ("\nI guessed accessory type wrong.")
    wrongAccessory.append(accessoryGuess)


def checkLengthAnswer():
  if lengthAnswer == "yes":
    #print ("\nI guessed hair length right!")
    for i in hairLengths:
      if i != lengthGuess:
        wrongLength.append(i)
  elif lengthAnswer == "no":
    #print ("\nI guessed hair length wrong.")
    wrongLength.append(lengthGuess)


def checkShirtAnswer():
  if shirtAnswer == "yes":
    #print ("\nI guessed shirt type right!")
    for i in shirtTypes:
      if i != shirtGuess:
        wrongShirt.append(i)
  elif shirtAnswer == "no":
    #print ("\nI guessed shirt type wrong.")
    wrongShirt.append(shirtGuess)


def checkMoodAnswer():
  if moodAnswer == "yes":
    #print ("\nI guessed mood right!")
    for i in moods:
      if i != moodGuess:
        wrongMood.append(i)
  elif moodAnswer == "no":
    #print ("\nI guessed mood wrong.")
    wrongMood.append(moodGuess)


def checkShapeAnswer():
  if shapeAnswer == "yes":
    #print ("\nI guessed face shape right!")
    for i in faceShapes:
      if i != shapeGuess:
        wrongShape.append(i)
  elif shapeAnswer == "no":
    #print ("\nI guessed face shape wrong.")
    wrongShape.append(shapeGuess)


def askPerson():
  global correctPerson
  global computerRounds

  if len(people) == 0:
    correctPerson = "Liar, liar, pants on fire."

  guess = random.choice(people)
  guessName = guess[0]

  nameAnswer = input(f"\nIs your character {guessName}?\n")
  nameAnswer = nameAnswer.lower()

  if nameAnswer != "yes" and nameAnswer != "no":
    correctPerson = "You entered incorrect input."
  else:
    if nameAnswer == "yes":
      correctPerson = f"\nWoohoo! I win. Good game.\n\nIt took me {computerRounds} questions."
    else:
      if len(people) == 0:
        correctPerson = "Liar, liar, pants on fire."
      else:
        correctPerson = f"\nOh no. You win. Good game."


def playerAskEyeColour():
  global humanRounds
  global humanEyeGuess
  eyeOptions = []

  for item in userPeople:
    if item[1] not in eyeOptions:
      eyeOptions.append(item[1])

  humanEyeGuess = (
      f"My character could have {eyeOptions} eyes. Please type your guess for eye colour."
  )

  if len(wrongEye) < len(eyeColours) - 1:
    while True:
      eyeAnswer = input(f"\nDoes your character have {eyeGuess} eyes?\n")
      eyeAnswer = eyeAnswer.lower()

      if eyeAnswer == "yes" or eyeAnswer == "no" or eyeAnswer == "none":
        break

      else:
        print("You entered incorrect input.")
        continue
  else:
    for i in eyeColours:
      if i not in wrongEye:
        eyeAnswer = "none"
  humanRounds += 1
  return eyeAnswer


print("""Welcome to Guess Who.

To play, pick a person from the character sheet and let the computer guess who you're thinking of. The computer will also pick a character and answer your questions and guesses.

Type 'yes' or 'no' to answer the questions, and pick from the typing options such as 'red' or 'long' when asking questions. Any other input will not be accepted.

Each of you only has one guess at the character's identity. Good luck.""")

while len(people) != 0:
  #Guessing
  randomQuestion = random.randint(0, 6)
  #playerAskEyeColour()

  if randomQuestion == 0:
    eyeGuess = guessEyeColour()
    eyeAnswer = askEyeColour()
    checkEyeAnswer()

  elif randomQuestion == 1:
    hairGuess = guessHairColour()
    hairAnswer = askHairColour()
    checkHairAnswer()

  elif randomQuestion == 2:
    accessoryGuess = guessAccessory()
    accessoryAnswer = askAccessory()
    checkAccessoryAnswer()

  elif randomQuestion == 3:
    lengthGuess = guessHairLength()
    lengthAnswer = askHairLength()
    checkLengthAnswer()

  elif randomQuestion == 4:
    shirtGuess = guessShirtType()
    shirtAnswer = askShirtType()
    checkShirtAnswer()

  elif randomQuestion == 5:
    moodGuess = guessMood()
    moodAnswer = askMood()
    checkMoodAnswer()

  elif randomQuestion == 6:
    shapeGuess = guessFaceShape()
    shapeAnswer = askFaceShape()
    checkShapeAnswer()

  for entry in people:
    eliminatePerson(entry, randomQuestion)

  for entry in eliminate:
    if entry in people:
      people.remove(entry)

  eliminate = []
  bestEye = []
  bestHair = []
  bestAccessory = []
  bestShirt = []
  bestLength = []
  bestMood = []
  bestShape = []

  #Being Asked

  if len(people) <= 1:
    askPerson()
    print(correctPerson)
    break
  else:
    continue

else:
  print("Liar, liar, pants on fire.")
