# import pyttsx3
# import time
# # engin = pyttsx3.init()
# # voices = engin.getProperty('voices')
# # engin.setProperty('voices',voices[0].id)
# # engin.setProperty('rate',130)
# # engin.setProperty('volume',1)

# for i in range(10):
#     engin = pyttsx3.init()
#     text = f"This is attempt number {i+1}"
#     print(text)
#     engin.say(text)
#     engin.runAndWait()   # Important! Forces engine to finish before next loop
    
#     time.sleep(.1) 

# from gtts import gTTS
# import os

# text = "Hello Harsh, this is a test of gTTS."
# tts = gTTS(text=text, lang='en')
# tts.save("test.mp3")

# # Play it (Windows)
# os.system("start test.mp3")


# from gtts import gTTS
# import os
# import time

# for i in range(10):
#     text = f"This is attempt number {i+1}"
#     tts = gTTS(text=text, lang='en')
#     filename = f"voice{i}.mp3"
#     tts.save(filename)

#     # Play on Windows (change for Mac/Linux if needed)
#     os.system(f"start {filename}")

    # time.sleep(2)  # wait for playback to finish before next


# from gtts import gTTS
# import pygame
# import time

# pygame.init()

# for i in range(10):
#     text = f"This is attempt number {i+1}"
#     tts = gTTS(text=text, lang='en')
#     filename = f"voice{i}.mp3"
#     tts.save(filename)

#     pygame.mixer.music.load(filename)
#     pygame.mixer.music.play()

#     # Wait until audio finishes
#     while pygame.mixer.music.get_busy():
#         time.sleep(0.1)


from gtts import gTTS
import pygame
import io
import time

pygame.init()

for i in range(10):
    text = f"This is attempt number {i+1}"
    
    # Generate speech in memory
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)  # go to start of file
    
    # Load and play with pygame
    pygame.mixer.music.load(fp, "mp3")
    pygame.mixer.music.play()
    
    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


