import random

def genPass(passLength, keyPhraseString):
    resultList = []
    for i in range(passLength):
        randomInt = random.randint(0, len(keyPhraseString) - 1)
        resultList.append(keyPhraseString[randomInt])
    return "".join(resultList)

def options(optChars, optIntegers, optPunctuation):
    keyPhraseString = ""
    if optChars == "y":
        keyPhraseString += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if optIntegers == "y":
        keyPhraseString += "0123456789"
    if optPunctuation == "y":
        keyPhraseString += "!#$%()*+,-./:?@^_`{|}~"
    return keyPhraseString

while True:
    try:
        countPass = int(input("How many passwords would you like to generate?: "))
        passLength = int(input("Length of password: "))
        break
    except Exception:
        print("Invalid input. Needs to be an integer.")

while True:
    optChars = input("Chars [Y/N]: ").lower()
    optIntegers = input("Integers [Y/N]: ").lower()
    optPunctuation = input("Punctuation [Y/N]: ").lower()
    if (optChars == "y" or optChars == "n") and (optIntegers == "y" or optIntegers == "n") and (optPunctuation == "y" or optPunctuation == "n"):
        pass
    else:
        print("Invalid input! Options need to be 'y' or 'n'.")
        continue

    if optChars == "n" and optIntegers == "n" and optPunctuation == "n":
        print("You have to check at least one option.")
        continue
    else:
        break

keyPhraseString = options(optChars, optIntegers, optPunctuation)
print("\n=== Generated Passwords ===")
for i in range(countPass):
    print(genPass(passLength, keyPhraseString))
print("===========================")