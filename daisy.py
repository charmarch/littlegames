# he likes me, he likes me not

import random
import math

questionsPos = [
    "Does he smell good?", "Do you think his friends are cool?", "Does he make you laugh?", "Do you like spending time with him?", "Can you guys talk for hours?", "Do you have similar values?", "Is he kind?", "Does he initiate plans?", "Does he text first?", "Does he want to see you?", "Do you like his style?", "Do you think he's hot?", "Is he interested in your opinions?", "Is he intelligent?", "Do your friends like him?", "Does he seem like an upstanding guy?", "If he gets a haircut, will you still like him?", "Is he an active listener?", "Does he give you butterflies?", "Do you get excited when he texts?", "Is he over his ex?"
]

questionsNeg = [
    "Do you feel like he's using you?", "Do your friends think you're too good for him?", "Is he only hot because he's tall?", "Are you anxiously waiting days for his next text?", "Does he give you EVIL butterflies? (like you're going to be sick or cry)", "Are you always the one to text first?", "Does he say he's super busy with school or work whenever you try to make plans?", "Does he just represent what you think you're missing in yourself?", "Do the red flags outnumber the green ones?", "Does he have poor hygiene?", "Does he bring up his ex a lot?", "Do you put off answering his texts?", "Do you actually kind of want to ghost him?"
]

posVal = "yes"
negVal = "no"

questionsDict = {q:posVal for q in questionsPos}
questionsDictNeg = {q:negVal for q in questionsNeg}
questionsDict.update(questionsDictNeg)

def numOfPetals():
    global petals
    petals = random.randint(1,50)
    print("Your daisy has " + str(petals) + " petals.")
    chooseInterval()

def getQuestions():
    global divResult
    divResult = math.ceil(petals / userInterval)
    questionList = random.sample(list(questionsDict.keys()),divResult)
    return questionList

def newInterval():
    global userInterval
    global petals
    userInterval = int(input("Choose an interval between size 1 and " + str(petals - (petNum*userInterval)) + "\n"))
    petals = petals - petNum*userInterval
    divMode()

def lastChance():
    print("Okay, he gets one last chance (and you get one more question).")
    finalQ = input("Does he make you feel good about yourself?\n")
    if finalQ == 'yes':
        print("Yayyyy!!! You guys sound like a great match. He likes YOU and you like HIM!!! :)")
        quit()
    else:
        print("That's a pretty important factor. You're better off without him.")
        quit()

def divMode():
    questions = getQuestions()
    global divResult
    global petals
    divResult = int(petals / userInterval)
    if divResult == 0:
        lastChance()
    for i in range(divResult):
        global petNum
        petNum = i+1
        userAnswer = input(str(questions[i]) + " (Answer 'yes' or 'no'.)\n")
        if userAnswer == questionsDict.get(questions[i]):
            if (divResult - i - 1) == 0:
                break
            newInt = input("Sounds like you like him! Do you want to keep going with the same interval? You have " + str(divResult - i - 1) + " question(s) left to answer with an interval this size. (Answer 'yes' or 'no')\n")
            if newInt == "no":
                newInterval()
        else:
            print("Maybe you don't actually like or need him. You don't need validation from a man! Go be free.")
            quit()
    print("Yayyyy!!! You guys sound like a great match. He likes YOU and you like HIM!!! :)")
    quit()

def chooseInterval():
    global userInterval
    userInterval = ""

    while True: 
        try:
            userInterval = int(input("Choose an interval size between 1 and " + str(petals) + " (inclusive).\n"))
        except ValueError:
            print("You must enter an integer.")
        
        if userInterval < 1 or userInterval > petals:
            print("Try another number that's in the range given.")
            continue
        else:
            break     

    petInt = petals / userInterval
    if type(petInt) is int and petInt % 2 == 0:
        print("We counted ahead for you, and we're sorry to say he likes you NOT. :(")
        quit()
    else: 
        divMode()
        quit()

if __name__ == "__main__":
    while True:
        print("Daisy is a game of 'he likes me, he likes me not'.")
        print("A number of petals is randomly generated, and it's up to you to pluck them.")
        print("To speed things up, you can choose to pluck them in whatever size of intervals you want.")
        print("But for each interval, you have to decide if YOU like HIM.")
        print("If you make it around the daisy, it means you're a match!")
        numOfPetals()