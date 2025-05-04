#Imports
import random
from collections import Counter

#Variables
people = []
eliminate = []
rounds = 1

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

#Setup Dictionaries
with open('people.txt') as peopleFile:
  for line in peopleFile:
    line = line.strip()
    parts = line.split(",")
    people.append(parts)

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

print ("""Welcome to Guess Who.

To play, pick a person from the character sheet and let the computer guess who you're thinking of.

Type 'yes' or 'no' to answer the questions. Any other input will not be accepted.

I only have one guess at the character's identity. Good luck.""")

while len(people) != 0:
  smartEye = random.randint(0,9)
  smartHair = random.randint(0,9)
  smartAccessory = random.randint(0,9)
  smartLength = random.randint(0,9)
  smartShirt = random.randint(0,9)
  smartMood = random.randint(0,9)
  smartShape = random.randint(0,9)

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

  if len(wrongEye) < len(eyeColours) - 1:
    eyeAnswer = input(f"\nDoes your character have {eyeGuess} eyes?\n")
    eyeAnswer = eyeAnswer.lower()
  else:
    for i in eyeColours:
      if i not in wrongEye:
        eyeAnswer = "none"

  if len(wrongHair) < len(hairColours) - 1:
    hairAnswer = input(f"\nDoes your character have {hairGuess} hair?\n")
    hairAnswer = hairAnswer.lower()
  else:
    for i in hairColours:
      if i not in wrongHair:
        hairAnswer = "none"

  if len(wrongAccessory) < len(accessories) - 1:
    if accessoryGuess == "glasses" or accessoryGuess == "earrings":
      accessoryAnswer = input(f"\nIs your character's accessory {accessoryGuess}?\n")
    elif accessoryGuess == "none":
      accessoryAnswer = input("\nDoes your character have no accessory?\n")
    else:
      accessoryAnswer = input(f"\nIs your character's accessory a {accessoryGuess}?\n")
    accessoryAnswer = accessoryAnswer.lower()
  else:
    for i in accessories:
      if i not in wrongAccessory:
        accessoryAnswer = "none"

  if len(wrongLength) < len(hairLengths) - 1:
    if lengthGuess == "long" or lengthGuess == "braided":
      lengthAnswer = input(f"\nIs your character's hair {lengthGuess}?\n")
    elif lengthGuess == "medium":
      lengthAnswer = input(f"\n Does your character have {lengthGuess} length hair?")
    else:
      lengthAnswer = input(f"\nDoes your character have {lengthGuess} hair?\n")
    lengthAnswer = lengthAnswer.lower()
  else:
    for i in hairLengths:
      if i not in wrongLength:
        lengthAnswer = "none"

  if len(wrongShirt) < len(shirtTypes) - 1:
    if shirtGuess == "unbuttoned":
      shirtAnswer = input(f"\nIs your character's shirt {shirtGuess}?\n")
    elif shirtGuess == "tank":
      shirtAnswer = input(f"\nIs your character's shirt a {shirtGuess} top?\n")
    elif shirtGuess == "hoodie":
      shirtAnswer = input(f"\nIs your character wearing a {shirtGuess}?\n")
    else:
      shirtAnswer = input(f"\nIs your character's shirt a {shirtGuess}?\n")
    shirtAnswer = shirtAnswer.lower()
  else:
    for i in shirtTypes:
      if i not in wrongShirt:
        shirtAnswer = "none"
        
  if len(wrongMood) < len(moods) - 1:
    moodAnswer = input(f"\nIs your character {moodGuess}?\n")
    moodAnswer = moodAnswer.lower()
  else:
    for i in moods:
      if i not in wrongMood:
        moodAnswer = "none"

  if len(wrongShape) < len(faceShapes) - 1:
    shapeAnswer = input(f"\nDoes your character have a {shapeGuess} face?\n")
    shapeAnswer = shapeAnswer.lower()
  else:
    for i in faceShapes:
      if i not in wrongShape:
        shapeAnswer = "none"

  if (eyeAnswer != "yes" and eyeAnswer != "no" and eyeAnswer != "none") or (hairAnswer != "yes" and hairAnswer != "no" and hairAnswer != "none") or (accessoryAnswer != "yes" and accessoryAnswer != "no" and accessoryAnswer != "none") or (lengthAnswer != "yes" and lengthAnswer != "no" and lengthAnswer != "none") or (shirtAnswer != "yes" and shirtAnswer != "no" and shirtAnswer != "none") or (moodAnswer != "yes" and moodAnswer != "no" and moodAnswer != "none") or (shapeAnswer != "yes" and shapeAnswer != "no" and shapeAnswer != "none"):
    print ("You entered incorrect input.")
    break

  print()

  if eyeAnswer == "yes":
    print ("I guessed eye colour right!")
    for i in eyeColours:
      if i != eyeGuess:
        wrongEye.append(i)
  elif eyeAnswer == "no":
    print ("I guessed eye colour wrong.")
    wrongEye.append(eyeGuess)
    
  if hairAnswer == "yes":
    print ("I guessed hair colour right!")
    for i in hairColours:
      if i != hairGuess:
        wrongHair.append(i)
  elif hairAnswer == "no":
    print ("I guessed hair colour wrong.")
    wrongHair.append(hairGuess)

  if accessoryAnswer == "yes":
    print ("I guessed accessory type right!")
    for i in accessories:
      if i != accessoryGuess:
        wrongAccessory.append(i)
  elif accessoryAnswer == "no":
    print ("I guessed accessory type wrong.")
    wrongAccessory.append(accessoryGuess)

  if lengthAnswer == "yes":
    print ("I guessed hair length right!")
    for i in hairLengths:
      if i != lengthGuess:
        wrongLength.append(i)
  elif lengthAnswer == "no":
    print ("I guessed hair length wrong.")
    wrongLength.append(lengthGuess)

  if shirtAnswer == "yes":
    print ("I guessed shirt type right!")
    for i in shirtTypes:
      if i != shirtGuess:
        wrongShirt.append(i)
  elif shirtAnswer == "no":
    print ("I guessed shirt type wrong.")
    wrongShirt.append(shirtGuess)

  if moodAnswer == "yes":
    print ("I guessed mood right!")
    for i in moods:
      if i != moodGuess:
        wrongMood.append(i)
  elif moodAnswer == "no":
    print ("I guessed mood wrong.")
    wrongMood.append(moodGuess)

  if shapeAnswer == "yes":
    print ("I guessed face shape right!")
    for i in faceShapes:
      if i != shapeGuess:
        wrongShape.append(i)
  elif shapeAnswer == "no":
    print ("I guessed face shape wrong.")
    wrongShape.append(shapeGuess)
  
  for entry in people:
    if eyeAnswer == "yes" and entry[1] != eyeGuess:
      eliminate.append(entry)
    elif eyeAnswer == "no" and entry[1] == eyeGuess:
      eliminate.append(entry)
    elif hairAnswer == "yes" and entry[2] != hairGuess:
      eliminate.append(entry)
    elif hairAnswer == "no" and entry[2] == hairGuess:
      eliminate.append(entry)
    elif accessoryAnswer == "yes" and entry[3] != accessoryGuess:
      eliminate.append(entry)
    elif accessoryAnswer == "no" and entry[3] == accessoryGuess:
      eliminate.append(entry)
    elif lengthAnswer == "yes" and entry[4] != lengthGuess:
      eliminate.append(entry)
    elif lengthAnswer == "no" and entry[4] == lengthGuess:
      eliminate.append(entry)
    elif shirtAnswer == "yes" and entry[5] != shirtGuess:
      eliminate.append(entry)
    elif shirtAnswer == "no" and entry[5] == shirtGuess:
      eliminate.append(entry)
    elif moodAnswer == "yes" and entry[6] != moodGuess:
      eliminate.append(entry)
    elif moodAnswer == "no" and entry[6] == moodGuess:
      eliminate.append(entry)
    elif shapeAnswer == "yes" and entry[7] != shapeGuess:
      eliminate.append(entry)
    elif shapeAnswer == "no" and entry[7] == shapeGuess:
      eliminate.append(entry)

  for entry in eliminate:
    if entry in people:
      people.remove(entry)

  eliminate = []
  bestEye = []
  bestHair = []
  bestAccessory = []
  bestLength = []
  bestShirt = []
  bestMood = []
  bestShape = []

  if len(people) < 5:
    if len(people) == 0:
      print("Liar, liar, pants on fire.")
      break
      
    guess = random.choice(people)
    guessName = guess[0]
  
    nameAnswer = input(f"\nIs your character {guessName}?\n")
    nameAnswer = nameAnswer.lower()
  
    if nameAnswer != "yes" and nameAnswer != "no":
      print ("You entered incorrect input.")
      break
    else:
      if nameAnswer == "yes":
        print("\nWoohoo! I win. Good game.")
        print(f"It took me {rounds} rounds of questioning.")
        break
      else:
        if len(people) == 0:
          print("Liar, liar, pants on fire.")
          break
        else:
          print(f"\nOh no. You win. Good game.")
      break
  else:
    rounds += 1
    continue

else:
  print("Liar, liar, pants on fire.")
