import time
import pyttsx3

curr = time.localtime()
hour = curr.tm_hour
minute = curr.tm_min
second = curr.tm_sec
date = curr.tm_mday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = curr.tm_wday
month = curr.tm_mon
year = curr.tm_year

print(hour, ":", minute, ":", second, " ", date, " ", days[day], " ", month, " ", year)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # choose different voice
engine.setProperty('rate', 130)            # speed
engine.setProperty('volume', 1)            # volume (0.0 to 1.0)

if 0 <= hour < 12:
    text = f"Hello, Harsh. Good Morning, Time is {hour} hour {minute} minute {second} second"
    print(text)
    engine.say(text)
    engine.runAndWait()

elif 12 <= hour <= 15:
    text = f"Hello, Harsh. Good Afternoon, Time is {hour} hour {minute} minute {second} second"
    print(text)
    engine.say(text)
    engine.runAndWait()

elif 15 < hour <= 20:
    text = f"Hello, Harsh. Good Evening, Time is {hour} hour {minute} minute {second} second"
    print(text)
    engine.say(text)
    engine.runAndWait()

else:
    text = f"Hello, Harsh. Good Night, Time is {hour} hour {minute} minute {second} second"
    print(text)
    engine.say(text)
    engine.runAndWait()


