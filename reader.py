import pyttsx3

class Reader:
    """ Creates a certamen moderator. """

    def __init__(self, rounds):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 140)
        self.rounds = rounds
    
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
        self.engine.runAndWait()

        return None


    def tossup(self, specs):
        """ The computer goes through the process of reading the tossup, and boni, if needed.

            Arguments:
            specs: a list specifying the round and tossup number

            Returns:
            None
        """
        s = [specs[0], specs[1], 'Tossup', 'Q']
        try:
            self.read(s)
            self.engine.say('Repeating:')
            self.read(s)
            self.engine.say('I will have to call time.')
            self.engine.say('The correct answer is:')
            s[3] = 'A'
            self.read(s)

        except KeyboardInterrupt:
            self.engine.endLoop()
            print('interrupted! how rude')
            self.engine.stop()
            # engine.startLoop(False)
            # engine.say('Answer please.')

            # engine.iterate()
            # engine.endLoop()

            # engine.say('The correct answer is:')
            # s[3] = 'A'
            # read(engine, rounds, s)
            # engine.say('Was that your answer?')
            # engine.runAndWait()
        
        return None
    
    def read_round(self, round):
        self.read([round, 'Info'])

        for i in range(1, 21):
            s = [round, i]
            self.tossup(s)