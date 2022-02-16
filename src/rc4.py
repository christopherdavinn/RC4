#program RC4
#basic belum dimodifikasi
import codecs
import lsfr

def convertToAscii(string):
    return ([ord(c) for c in string])

def convertToChar(values):
    #input berupa list
    string = "".join([chr(c) for c in values])
    return string

def ksa(kunci):
    n_kunci = len(kunci)
    #larik S [0,1,2, ... , 255]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + kunci[i % n_kunci]) % 256
        #swap
        S[i], S[j] = S[j], S[i]
    return S

def prga(arr):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + arr[i]) % 256
        #swap
        temp = []
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        stream = arr[(arr[i] + arr[j]) % 256]
        yield stream

def getKeystream(kunci):
    temp = lsfr.getLsfr(kunci)
    arr = ksa(temp)
    keyStream = prga(arr)
    return keyStream

def XORproccessing(input, kunci):
    #teks adalah ASCII, key adalah ASCII
    key = convertToAscii(kunci)
    keystream = getKeystream(key)

    #if input teks
    if type(input) == str:
        teks = convertToAscii(input) #to array of ascii number
        print("dia teks")
    else:
        teks = input

    result = []
    for i in teks:
        xor = i ^ next(keystream) #XOR
        val = ("%02X" % xor)
        result.append(val)
    toString = ''.join(result)
    return toString

def enkripsi(plainteks, kunci):
    cipherteks = XORproccessing(plainteks, kunci)
    return cipherteks

def dekripsi(cipherteks, kunci):
    cipherteks = codecs.decode(cipherteks, 'hex_codec')
    plainteks = XORproccessing(cipherteks, kunci)
    return codecs.decode(plainteks, 'hex_codec').decode('utf-8') #turn bytes type into string type