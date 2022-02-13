#program RC4

#basic belum dimodifikasi


def convertToAscii(string):
    return ([ord(c) for c in s])

def convertToChar():
    return 0

def KSA(kunci):
    n_kunci = len(kunci)
    #larik S [0,1,2, ... , 255]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + kunci[i % n_kunci]) % 256
        #swap
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        #swap
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K