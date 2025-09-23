import time
question = ["What color is the sky on a clear day?",
            "How many days are there in a week?",
            "What planet do we live on?"]
answer = ["C","B","A"]
option = [["A. Red","B. Orange","C. Blue","D. Green"],
          ["A. 4","B. 7","C. 8","D. 3"],
          ["A. Earth","B. Mars","C. Jupitor","D. Mercury"]]

i = 0
sum = 0
correct = 0
wrong = 0
while(i<len(question)):
    
    print(question[i])
    print(option[i])

    ans = str(input("Enter Your Option = "))
    if(ans == answer[i]):
        sum+=5
        correct+=1
    else:
        sum+=0
        wrong+=1
    i+=1
    if(i==len(question)):
        print("Calculating Your Score...")
    else:
        print("Displaying Your Question...")
    time.sleep(1)

print("Total Score You Got = ",sum)
print("Total Correct answer = ",correct)
print("Total wrong answer = ",wrong)

        



