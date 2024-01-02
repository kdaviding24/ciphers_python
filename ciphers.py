alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def vigenere_decode(message, phrase):
    message_decoded = ''
    count = 0
    for i in range(len(message)):
        if message[i].upper() in alpha:
            if i > len(phrase) - 1:
                message_decoded += alpha[(alpha.index(message[i].upper()) - 26) + alpha.index(phrase[count%len(phrase)].upper())]
                count += 1
            else:
                message_decoded += alpha[(alpha.index(message[i].upper()) - 26) + alpha.index(phrase[i].upper())]
        else:
            message_decoded += message[i]
    return message_decoded
print(vigenere_decode('ymlok cp fbb ejv', 'dog'))

def vigenere_encode(message,phrase):
    code = ''
    count = 0
    for i in range(len(message)):
        if message[i].upper() in alpha:
            if i > len(phrase)- 1:
                code += alpha[alpha.index(message[i].upper()) - alpha.index(phrase[count%len(phrase)].upper())]
                count += 1
            else:
                code += alpha[alpha.index(message[i].upper()) - alpha.index(phrase[i].upper())]
        else:
            code += message[i]
    return code
print(vigenere_encode('barry is the spy', 'dog'))

reg_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def caesar_decode(code, offset):
    decode = ''
    for letter in code.upper():
        if letter in reg_alpha:
            decode += reg_alpha[((reg_alpha.index(letter) - 26) + offset)]
        else:
            decode += letter
    return decode
print(caesar_decode('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!', 10))


def caesar_encode(code, offset):
    encryption = ''
    for letter in code:
        if letter in reg_alpha:
            encryption += reg_alpha[reg_alpha.index(letter) - offset]
        else:
            encryption += letter
    return encryption
print(caesar_encode('HEY THERE! THIS IS AN EXAMPLE OF A CAESAR CIPHER. WERE YOU ABLE TO DECODE IT? I HOPE SO! SEND ME A MESSAGE BACK WITH THE SAME OFFSET!', 10))