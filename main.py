MORSE_CODE_DICT = {'A': ':Dolt::DeltaAirLines:', 'B': ':DeltaAirLines::Dolt::Dolt::Dolt:',
                   'C': ':DeltaAirLines::Dolt::DeltaAirLines::Dolt:', 'D': ':DeltaAirLines::Dolt::Dolt:', 'E': ':Dolt:',
                   'F': ':Dolt::Dolt::DeltaAirLines::Dolt:', 'G': ':DeltaAirLines::DeltaAirLines::Dolt:',
                   'H': ':Dolt::Dolt::Dolt::Dolt:', 'I': ':Dolt::Dolt:',
                   'J': 'Dolt::DeltaAirLines::DeltaAirLines::DeltaAirLines:',
                   'K': ':DeltaAirLines:Dolt::DeltaAirLines:', 'L': ':Dolt::DeltaAirLines::Dolt::Dolt:',
                   'M': ':DeltaAirLines::DeltaAirLines:', 'N': ':DeltaAirLines::Dolt:',
                   'O': ':DeltaAirLines::DeltaAirLines::DeltaAirLines:',
                   'P': ':Dolt::DeltaAirLines::DeltaAirLines::Dolt:',
                   'Q': ':DeltaAirLines::DeltaAirLines::Dolt::DeltaAirLines:', 'R': ':Dolt::DeltaAirLines::Dolt:',
                   'S': ':Dolt::Dolt::Dolt:', 'T': ':DeltaAirLines:',
                   'U': ':Dolt::Dolt::DeltaAirLines:', 'V': ':Dolt::Dolt::Dolt::DeltaAirLines:',
                   'W': ':Dolt::DeltaAirLines::DeltaAirLines:', 'X': ':DeltaAirLines::Dolt::Dolt::DeltaAirLines:',
                   'Y': ':DeltaAirLines::Dolt::DeltaAirLines::DeltaAirLines:',
                   'Z': ':DeltaAirLines::DeltaAirLines::Dolt::Dolt:',
                   '1': ':Dolt::DeltaAirLines::DeltaAirLines::DeltaAirLines::DeltaAirLines:',
                   '2': ':Dolt::Dolt::DeltaAirLines::DeltaAirLines::DeltaAirLines:',
                   '3': ':Dolt::Dolt::Dolt::DeltaAirLines::DeltaAirLines:',
                   '4': ':Dolt::Dolt::Dolt::Dolt::DeltaAirLines:',
                   '5': ':Dolt::Dolt::Dolt::Dolt::Dolt:', '6': ':DeltaAirLines::Dolt::Dolt::Dolt::Dolt:',
                   '7': ':DeltaAirLines::DeltaAirLines::Dolt::Dolt::Dolt:',
                   '8': ':DeltaAirLines::DeltaAirLines::DeltaAirLines::Dolt::Dolt:',
                   '9': ':DeltaAirLines::DeltaAirLines::DeltaAirLines::DeltaAirLines::Dolt:',
                   '0': ':DeltaAirLines::DeltaAirLines::DeltaAirLines::DeltaAirLines::DeltaAirLines:',
                   ',': ':DeltaAirLines::DeltaAirLines::Dolt::Dolt::DeltaAirLines::DeltaAirLines:',
                   '.': ':Dolt::DeltaAirLines::Dolt::DeltaAirLines::Dolt::DeltaAirLines:',
                   '?': ':Dolt::Dolt::DeltaAirLines::DeltaAirLines::Dolt::Dolt:',
                   '/': ':DeltaAirLines::Dolt::Dolt::DeltaAirLines::Dolt:',
                   '-': ':DeltaAirLines::Dolt::Dolt::Dolt::Dolt::DeltaAirLines:',
                   '(': ':DeltaAirLines::Dolt::DeltaAirLines::DeltaAirLines::Dolt:',
                   ')': ':DeltaAirLines::Dolt::DeltaAirLines::DeltaAirLines::Dolt::DeltaAirLines:'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter

        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher


def main():
    message = input("Encrypt: ")
    result = encrypt(message.upper())
    print(result)

    message = input("Decrypt: ")
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
