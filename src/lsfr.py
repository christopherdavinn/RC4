def convert(s): # Convert string to ASCII
    return ([ord(c) for c in s])

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

def convertToAscii(string):
    return ([ord(c) for c in string])

def getLsfr(kunci):
    #key = convert(kunci) #array of ASCII number
    binary = ''.join(format(i, '08b') for i in kunci)
    l = len(binary)
    output = ""
    outlist = []
    for i in range (0, l-1, 4):
        proses = str(int(binary[i]) ^ int(binary[i+3])) + binary[i:i+3] 
        output = output + proses
    #turn to string
    outlist = [output[i:i+8] for i in range(0, l-1, 8)]
    result = bits2string(outlist)
    result = convertToAscii(result)
    return result #ascii number