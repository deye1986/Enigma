from math import trunc

def enigma():
    '''cypher'''
    
    message = input('INPUT MESSAGE TO BE CODED (CTRL + C to quit) \n >>> ')
    if message == '':
        enigma()
    else:
        message = message.upper()
        message = message.strip()
        message = message.replace(' ', '') # because of a traceback on line83, whitespace issues.

        numb = []

        for sign in message:
            number = ord(sign) - 65
            numb.append(number)

        #Input settings
        rotorI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        rotorII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        rotorIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        reflektor = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        plugboard = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]
        rotIstart = 7
        rotIIstart = 24
        rotIIIstart = 2

        
        def shiftstart(seq, n):
            '''initialize the rotor'''
            return seq[n:] + seq[:n]

        def shift(seq, n, rn, numb):
            '''Rotate the enigma dials'''
            if rn == 1:
                n = -n % len(seq)

            elif rn == 2:
                n = - trunc(n/25) % len(seq)
                
            elif rn == 3:
                n = - trunc(n/675) % len(seq)
            
            return seq[n:] + seq[:n]

        
        def rotorrev(seq):
            '''Going back through the rotor after reflektion  '''
            rotorrev = ['empty']*26
            for i in range(26):
                rotorrev[seq[i]] = i
            
            return rotorrev

    
        def rotor(seq, rev, numb, rn):
            ''' Going through the rotor'''
            number = []
            rotorreverse = ['empty']*26           
            if rev == 0:
                for i in range(len(numb)):
                    rotation = shift(seq, i, rn, numb)
                    number.append(rotation[numb[i]])
                    
            elif rev == 1:
                for i in range(len(numb)):
                    rotation = shift(seq, i, rn, numb)
                    seqrev = rotorrev(rotation)
                    number.append(seqrev[numb[i]])
                
            return number
        
        def refPlug(list, numbIII):
            '''Going through the reflektor or plugboard  '''
            ref = []
            for i in range(len(numbIII)):
                ref.append(list[numbIII[i]])
                
            return ref

        #Enigma
        rotorIM = shiftstart(rotorI, rotIstart)
        rotorIIM = shiftstart(rotorII, rotIIstart)
        rotorIIIM = shiftstart(rotorIII, rotIIIstart)

        seq = refPlug(plugboard, numb)
        seqI = rotor(rotorIM, 0, seq, 1)
        seqII = rotor(rotorIIM, 0, seqI, 2)
        seqIII = rotor(rotorIIIM, 0, seqII, 3) 
        seqIV = refPlug(reflektor, seqIII)
        seqVI = rotor(rotorIIIM, 1, seqIV, 3)
        seqVII = rotor(rotorIIM, 1, seqVI, 2)
        seqVIII = rotor(rotorIM, 1, seqVII, 1)
        seqIX = refPlug(plugboard, seqVIII)

        
        new_mes = []
        for i in range(len(seqIX)):
            word = chr(seqIX[i]+65)
            new_mes.append(word)

        print(''.join(new_mes))

while(1):
    enigma()