import time
from gtts import gTTS
import pygame
import io

# Initialize pygame mixer
pygame.mixer.init()

def speak(text):
    # Generate speech in memory
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # Load sound from memory using Sound object
    sound = pygame.mixer.Sound(fp)
    sound.play()

    # Wait until sound is finished
    while pygame.mixer.get_busy():
        time.sleep(0.1)

# Questions, answers, and options
question = ["What color is the sky on a clear day?",
            "How many days are there in a week?",
            "What planet do we live on?"]
answer = ["C","B","A"]
option = [["A. Red","B. Orange","C. Blue","D. Green"],
          ["A. 4","B. 7","C. 8","D. 3"],
          ["A. Earth","B. Mars","C. Jupiter","D. Mercury"]]

i = 0
score = 0
correct = 0
wrong = 0

while i < len(question):
    print(question[i])
    speak(question[i])
    time.sleep(1)
    print(option[i])
    speak(" , ".join(option[i]))

    ans = input("Enter Your Option = ")
    if ans.upper() == answer[i]:
        score += 5
        correct += 1
        speak("Correct Answer!")
    else:
        wrong += 1
        speak("Wrong Answer!")

    i += 1
    if i == len(question):
        print("Calculating Your Score...")
        speak("Calculating your score")
    else:
        print("Displaying Your Question...")
        speak("Next Question")
    time.sleep(1)

print("Total Score You Got = ", score)
print("Total Correct answer = ", correct)
print("Total wrong answer = ", wrong)
speak(f"You scored {score} points. Correct answers {correct}, wrong answers {wrong}.")
