import wave

def namer(letter: str) -> str:
    return "Waveform Genesis - " + letter + ".wav"

wordlist=[]
outfile = "output.wav"

inputstr=input("Enter Word: ")

for i in inputstr.upper():
    if i == 'A':
        wordlist.append(namer("A"))
    elif i == 'B':
        wordlist.append(namer("b1"))
    elif i == 'C':
        wordlist.append(namer("C1"))
    elif i == 'D':
        wordlist.append(namer("D"))
    elif i == 'E':
        wordlist.append(namer("e1"))
    elif i == 'F':
        wordlist.append(namer("F"))
    elif i == 'G':
        wordlist.append(namer("G"))
    elif i == 'H':
        wordlist.append(namer("H"))
    elif i == 'I':
        wordlist.append(namer("I"))
    elif i == 'J':
        wordlist.append(namer("J"))
    elif i == 'K':
        wordlist.append(namer("K"))
    elif i == 'L':
        wordlist.append(namer("L"))
    elif i == 'M':
        wordlist.append(namer("M"))
    elif i == 'N':
        wordlist.append(namer("N"))
    elif i == 'O':
        wordlist.append(namer("O"))
    elif i == 'P':
        wordlist.append(namer("P"))
    elif i == 'Q':
        wordlist.append(namer("Q"))
    elif i == 'R':
        wordlist.append(namer("R1"))
    elif i == 'S':
        wordlist.append(namer("S"))
    elif i == 'T':
        wordlist.append(namer("T1"))
    elif i == 'U':
        wordlist.append(namer("U"))
    elif i == 'V':
        wordlist.append(namer("V"))
    elif i == 'W':
        wordlist.append(namer("W"))
    elif i == 'X':
        wordlist.append(namer("X"))
    elif i == 'Y':
        wordlist.append(namer("Y"))
    elif i == 'Z':
        wordlist.append(namer("Z"))
    else:
        wordlist.append("sp.wav")
    wordlist.append("small.wav")

data= []
for infile in wordlist:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()
