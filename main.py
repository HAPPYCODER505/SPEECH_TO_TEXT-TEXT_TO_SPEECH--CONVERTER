#Hello friends the main aim of this python project is to convert speech to text and text to speech.
#I used 3 bessic modules :
# ---> pyttsx3,speech_recognition and pyaudio..:)
#But using some good modules will make some better projects like computer_voice_assitant,library management system etc...
#lets start



print("Welcome to 'SPEECH TO TEXT AND TEXT TO SPEECH MODEL''")
print("Setup....")
#creating  option for user...
#text to speech or speech to text....
print("what model you need?? 'Speech to text' or  'Text to speech")
print("press 'T' for text to speech or press'S' for speech to text")
A=input()
#apply if & else (a besic code.....) 
if A=='T':

    # importing modules..
    import pyttsx3
    import speech_recognition as sr

    # set up .....
    a = input("please enter your name")
    b = input("enter whitch type of voice you need.'0' for male and '1' for fe male")
    if b == '0':
        b == 0
    else:
        b == 1

    en = pyttsx3.init('sapi5')
    # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
    voices = en.getProperty('voices')
    en.setProperty('voice', voices[int(b)].id)


    # Let's creat our speak func...
    def speak(audio):
        en.say(audio)
        en.runAndWait()


    def text():
        T = input("enter your text")
        while (T != 'OUT'):
            T = input("enter your text")

            speak(T)


    if __name__ == '__main__':
        text()
else:
    import  speech_recognition as sr
    import  pyaudio
    import pyttsx3



    def takecommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listning....")
            r.pause_threshold = 1
            # if you want to change some speech recog functionality then pres 'ctrl' and click on 'pause_thrsehold'..
            audio = r.listen(source)
        try:
            print("Recognizing....")
            take = r.recognize_google(audio, language='en-in')
            print(f"user said: {take}\n")
        except Exception as a:
            print(a)

            print("say that again please")
            return "None"
    if __name__ == '__main__':
        a = input("please enter your name")
        while True:
         takecommand()









