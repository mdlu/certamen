import pyttsx3
from extract_round import extract_round
from reader import Reader



if __name__ == '__main__':
    
    p = "2018_yale_advanced.txt"
    yaleadv18 = extract_round(p)

    specs = ['Finals', 15]
    r = Reader(yaleadv18)

    r.read_round('Round 1')


    # zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # engine.setProperty('voice', zira)
    # engine.say('hello there')
    # engine.runAndWait()

    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice:")
    #     print(" - ID: %s" % voice.id)
    #     print(" - Name: %s" % voice.name)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)

