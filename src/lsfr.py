def convert(s): # Convert string to ASCII
    return ([ord(c) for c in s])

def getLsfr(kunci):
    key = convert(kunci)
    binary = ''.join(format(i, '08b') for i in key)
    print(binary)
    l = len(binary)
    #output = []
    output = ""
    outlist = []
    for i in range (0, l-1, 4):
        proses = str(int(binary[i]) ^ int(binary[i+3])) + binary[i:i+3] 
        output = output + proses
        outlist[:0] = output
    return outlist

#coba = getLsfr("halo")
#print(coba)