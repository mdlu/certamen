import pyttsx3
from extract_round import extract_round
from reader import Reader


# engine = pyttsx3.init()
# def onStart(name):
#    print('starting', name)
# def onWord(name, location, length):
#    print('word', name, location, length)
# def onEnd(name, completed):
#    print('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
# engine = pyttsx3.init()
# # engine.connect('started-utterance', onStart)
# # engine.connect('started-word', onWord)
# # engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()

if __name__ == '__main__':
    
    p = "2018_yale_advanced.txt"
    yaleadv18 = extract_round(p)

    specs = ['Finals', 15]
    r = Reader(yaleadv18)

    r.read_round('Round 3')

    # e = pyttsx3.init()
    
    # e.say('hello')
    # e.startLoop()
    # #e.iterate()
    # e.stop()
    # e = pyttsx3.init()
    # e.say('goodbye')

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

