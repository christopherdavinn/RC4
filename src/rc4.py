#program RC4
#basic belum dimodifikasi
import codecs

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
        arr[i] = arr[j]
        arr[j] = arr[i]
        stream = arr[(arr[i] + arr[j]) % 256]
        yield stream

def getKeystream(kunci):
    arr = ksa(kunci)
    key = prga(arr)
    return key

def XORproccessing(input, kunci):
    #teks adalah ASCII, key adalah ASCII
    key = convertToAscii(kunci)
    keystream = getKeystream(key)

    #if input teks
    if type(input) == str:
        teks = convertToAscii(input) #array 
    elif type(input) == bytes:
        teks = input #array

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
    return codecs.decode(plainteks, 'hex_codec').decode('utf-8') #turn bytes into string



# string = "hello world"
# a = convertToAscii(string)
# print (a)
#hasil : [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

# string = "hello world"
# a = bytes(string, 'ascii')
# for byte in a:
#     print(byte, end=' ')
# print (a)
#hasil: 104 101 108 108 111 32 119 111 114 108 100 