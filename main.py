import string
import random 
import time
import os 

def removePunctuation(inputString):
    translator = str.maketrans("", "", string.punctuation)
    return inputString.translate(translator)

def getWords():
    with open("data.txt","r") as file:
        lines = file.readlines()
        file.close()
    text = ""
    for line in lines:
        text += line.rstrip()
    return removePunctuation(text.lower()).split()

def getWordsFromList(wordsList,howMany=10):
    chosenWords = []
    for wordNumber in range(howMany):
            chosenWords.append(wordsList[wordNumber])
            wordsList.pop(wordNumber)
            if wordsList == []:
                break
    return wordsList,chosenWords

def countdownToStart():
    print("The Quiz starts in 10")
    for i in range(9,0,-1):
        print(i)
        time.sleep(1)
    os.system("cls")

def main():
        words = getWords()
        random.shuffle(words)
        correctWordsFromFile = []
        condition = True
        countdownToStart()    
        startTime = time.perf_counter()
        userInputs = []
        while condition:
            words,randomWords = getWordsFromList(words)
            for word in randomWords:
                print(word,end=" ")
                correctWordsFromFile.append(word)
            print()
            userInputs.append(input(" : "))
            if words == [] or (time.perf_counter() - startTime > 12):
                condition = False
                endTime = time.perf_counter()
        userWords = []
        for line in userInputs:
            for word in line.split():
                userWords.append(word)
        correctWords = 0
        leastList = correctWordsFromFile
        if len(userWords) < len(leastList):
            leastList = userWords
        for wordIndex in range(len(leastList)):
            if userWords[wordIndex] == correctWordsFromFile[wordIndex]:
                correctWords += 1
        print(f"Your Typing Speed is {len(userWords)}/min or {len(userWords)/60}/sec. The Accuracy is {correctWords} of {len(correctWordsFromFile)}, You finished in {endTime - startTime} seconds.")
        

main()

