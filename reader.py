import pyttsx3
from queue import Queue

class Reader:
    """ Creates a certamen moderator. """

    def __init__(self, rounds):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine2 = pyttsx3.init()
        self.rounds = rounds
        self.score = 0

    
    def read(self, specs):
        """ The computer reads the requested section of text from the rounds the reader holds.

            Arguments:
            specs: a list specifying the particular text to be read

            Returns:
            None
        """
        
        t = ''

        if len(specs) == 2: # this is when we're reading the starting info for the round
            text = self.rounds[specs[0]][specs[1]]
        else:
            text = self.rounds[specs[0]][specs[1]][specs[2]][specs[3]]
            if specs[2] == 'Tossup' and specs[3] == 'Q':
                t = 'Tossup'

        self.engine.say(t + text.lower()) # changing to lowercase avoids issues where uppercase is read as an abbreviation
        
        #self.engine.startLoop()
     


    def tossup(self, specs):
        """ The computer goes through the process of reading the tossup, and boni, if needed.

            Arguments:
            specs: a list specifying the round and tossup number

            Returns:
            None
        """
        s = [specs[0], specs[1], 'Tossup', 'Q']
        tossup_score = 0

        self.read(s)
        self.engine.runAndWait()
        
        correct = self.answer(s)
        
        if correct:
            tossup_score += 10
            s[2] = 'Bonus 1'
            s[3] = 'Q'
            self.read(s)
            self.engine.runAndWait()
            correct1 = self.answer(s)
            if correct1:
                tossup_score += 5
            
            s[2] = 'Bonus 2'
            s[3] = 'Q'
            self.read(s)
            self.engine.runAndWait()
            correct2 = self.answer(s)
            if correct2:
                tossup_score += 5
        
        self.score += tossup_score

        self.engine.say("So that's %d points to you on tossup %d." % (tossup_score, specs[1]))
        self.engine.runAndWait()

        # try: 
        #     self.read(s)
        #     self.engine.say('Repeating:')
        #     self.read(s)
        #     self.engine.say('I will have to call time.')
        #     self.engine.say('The correct answer is:')
        #     s[3] = 'A'
        #     self.read(s)

        #     #self.engine.runAndWait()
        #     self.engine.startLoop()
        #     #self.engine.endLoop()
            
        #     return False

        # except KeyboardInterrupt:
        #     self.engine.endLoop()
        #     # self.engine.say('testing')
        #     # self.engine.startLoop()
        #     # self.engine.endLoop()
        #     #self.engine.stop()
            
        #     #self.tossup_answer(s)
        #     #self.engine.endLoop()

        #     # ADD implementation of boni if the tossup is answered correctly
            
        #     return True
    
    def answer(self, s):
        
        self.engine.say('What is your answer?')
        self.engine.runAndWait()
        x = input('Answer: ')
        
        self.engine.say('The correct answer was:')
        self.engine.runAndWait()

        s[3] = 'A'
        self.read(s)
        self.engine.runAndWait()

        self.engine.say('Was that your answer?')
        self.engine.runAndWait()

        y = input("Type 'y' or 'n': ")
        if y == 'y':
            self.engine.say('Great!')
            self.engine.runAndWait()
            
            return True
        else:
            self.engine.say('Sorry.')
            self.engine.runAndWait()

            return False


    def read_round(self, round):
        #self.read([round, 'Info'])

        for i in range(1, 21):
            s = [round, i]
            self.tossup(s)
        
        self.engine.say('Your final score is:', self.score)
        self.engine.runAndWait()

            
        #self.engine.startLoop()
        