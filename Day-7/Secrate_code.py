import random
import string

while True:
    print("Enter stop for stop...")
    word = input("Enter the string  = ")
    t = word
    if(word=="stop"):
        break
    elif(len(word)<=3):
        s = 0
        e = len(word)-1
        word = list(word)
        while(s<e):
            temp = word[s]
            word[s] = word[e]
            word[e] = temp
            s+=1
            e-=1
        word = "".join(word)
        print(f"\nOriginal String = {t} Secrate Code = {word}")
    
    else:
        word = list(word)
        w1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        w2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        temp = word[0]
        i = 1
        while(i<len(word)):
            word[i-1] = word[i]
            i+=1
        word[len(word)-1] = temp
        word = "".join(word)
        final_word = w1+word+w2
        print(f"\nOriginal String = {t} Secrate Code = {final_word}")

        

            
