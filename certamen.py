
def extract_round(path):
    f = open(path, 'r').read()
    qanda = {}
    questions = {}
    newquestions = {}
    temp = f.split('\n')
    temp = [item.strip() for item in temp]

    baserounds = ['Round 1', 'Round 2', 'Round 3', 'Semis', 'Finals']

    # finds the indices separating each round
    ind = {}
    ind['Round 1'] = temp.index('Advanced – Preliminary Round 1')-1
    ind['Round 2'] = temp.index('Advanced – Preliminary Round 2')-1
    ind['Round 3'] = temp.index('Advanced – Preliminary Round 3')-1
    ind['Semis'] = temp.index('Advanced – Semifinal Round')-1
    ind['Finals'] = temp.index('Advanced – Final Round')-1
    for i in baserounds:
        ind['Extra Myth %s' % (i)] = temp.index('EXTRA MYTHOLOGY', ind[i])
        ind['Extra Hist %s' % (i)] = temp.index('EXTRA HISTORY', ind[i])
        ind['Extra Lit %s' % (i)] = temp.index('EXTRA LITERATURE', ind[i])
        ind['Extra Lang %s' % (i)] = temp.index('EXTRA LANGUAGE', ind[i])

    # creates a list of the names of the rounds to use as keys in dictionaries
    rounds = []
    for i in baserounds:
        rounds.append(i)
        rounds.append('Extra Myth %s' %(i))
        rounds.append('Extra Hist %s' %(i))
        rounds.append('Extra Lit %s' %(i))
        rounds.append('Extra Lang %s' %(i))
    
    # maps a list of all the strings in a round to the round's name as a key
    for i in range(len(rounds)-1):
        qanda[rounds[i]] = temp[ind[rounds[i]]:ind[rounds[i+1]]]
    qanda['Extra Lang Finals'] = temp[ind[rounds[len(rounds)-1]]:]
    
    # within each of the main rounds, maps each set of questions/bonuses to each question number
    for round in baserounds:
        tester = qanda[round]
        questions[round] = {}
        questions[round][0] = []
        
        #takes out beginning information
        k = 0
        questions[round]['Info'] = []
        while True:
            if tester[k][:3] == '1. ':
                break
            questions[round]['Info'].append(tester[k])
            k += 1

        for qnum in range(1, 20):
            questions[round][qnum] = []
            while True:
                try:
                    space = tester[k].index(' ')
                    if tester[k][:space+1] == '%d. ' % (qnum+1):
                        break
                except:
                    pass
                questions[round][qnum].append(tester[k])
                k += 1
        # individually handle question 20
        questions[round][20] = []
        while True:
            try:
                questions[round][20].append(tester[k])
                k += 1
            except:
                break

    # split each question into the tossup and boni
    for round in baserounds:
        newquestions[round] = {}
        newquestions[round]['Info'] = ' '.join(questions[round]['Info'])
        qtexts = [questions[round][i+1] for i in range(20)]
        
        questionnumber = 0
        for qtext in qtexts:
            questionnumber += 1
            newquestions[round][questionnumber] = {}
    
            b1 = 0
            b2 = 0
            for qline in qtext[2:]:
                if qline[:3] == 'B1:':
                    b1 = qtext.index(qline)
                elif qline[:3] == 'B2:':
                    b2 = qtext.index(qline)

            newquestions[round][questionnumber]['Tossup'] = {}
            newquestions[round][questionnumber]['Bonus 1'] = {}
            newquestions[round][questionnumber]['Bonus 2'] = {}

            tossup = [word for word in qtext[:b1] if word != '']
            bonus1 = [word for word in qtext[b1:b2] if word != '']
            bonus2 = [word for word in qtext[b2:] if word != '']

            for item in [tossup, bonus1, bonus2]:
                #print(item)
                z = 0
                
                while True:
                    #nopunct = item[z].translate(['(',')','/', ',', ' ', '-'])
                    nopunct = item[z]
                    #print(nopunct)
                    if nopunct.upper() == nopunct:
                        hold = z
                        break
                    z += 1

                if item == tossup:
                    newquestions[round][questionnumber]['Tossup']['Q'] = ' '.join(item[:hold])
                    newquestions[round][questionnumber]['Tossup']['A'] = ' '.join(item[hold:])
                elif item == bonus1:
                    newquestions[round][questionnumber]['Bonus 1']['Q'] = ' '.join(item[:hold])
                    newquestions[round][questionnumber]['Bonus 1']['A'] = ' '.join(item[hold:])
                else:
                    newquestions[round][questionnumber]['Bonus 2']['Q'] = ' '.join(item[:hold])
                    newquestions[round][questionnumber]['Bonus 2']['A'] = ' '.join(item[hold:])
            # Eunus and Cleon: bad because bonus 1 and 2 are combined
            # 'tigridos' hint removed
            # what to do for other proctor notes? like 'I will now pause before tossup 20'

    return newquestions


if __name__ == '__main__':
    
    p = "2018_yale_advanced.txt"
    yaleadv18 = extract_round(p)

    #test cases
    print(yaleadv18['Finals']['Info'])
    # for round in ['Round 1', 'Round 2', 'Round 3', 'Semis', 'Finals']:
    #     for q in range(1, 21):
    #         for format in ['Tossup', 'Bonus 1', 'Bonus 2']:
    #             for qa in ['Q', 'A']:
    #                 print(yaleadv18[round][q][format][qa])
    print(yaleadv18['Round 1'][5]['Tossup']['Q'])
    print(yaleadv18['Finals'][20]['Bonus 1']['A'])
    print(yaleadv18['Semis'][10]['Bonus 2']['Q'])
