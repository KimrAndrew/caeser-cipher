def shift_char(char,shift):
    char_code = ord(char)
    if ord('A') <= char_code <= ord('Z'):
        shifted_code = char_code + shift
        if shifted_code > ord('Z'):
            #wrap = shifted_code % ord('Z')
            wrap = shifted_code % ord('Z')
            shifted_code = ord('A') + wrap
        if shifted_code < ord('A'):
            wrap = 1 + (ord('A') % shifted_code) * -1
            #print('SHIFT:',shifted_code)
            #print('WRAP:',wrap)
            shifted_code = ord('Z') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    elif ord('a') <= char_code <= ord('z'):
        shifted_code = char_code + shift
        if shifted_code > ord('z'):
            wrap = shifted_code % ord('z')
            shifted_code = ord('a') + wrap
        if shifted_code < ord('a'):
            wrap = 1 + (ord('a') % shifted_code) * -1
            shifted_code = ord('z') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    else:
        return char


def encrypt(plain,shift):
    encrypted = ''
    for char in plain:
        encrypted += shift_char(char,shift)
    return encrypted

    # for char in plain:
        
    #     # assigned to None if  not upper
    #     encrypted_char = _shift(char,shift,(ord('A'),ord('B')))

    #     # assigned to None if not lower after checking if upper
    #     if not encrypted_char:
    #         encrypted_char = _shift(char,shift,(ord('a'),ord('b')))

    #     # if neither, do nothing - return char as is
    #     if not encrypted_char:
    #         encrypted_char = char

    #     encrypted += encrypted_char
    
    # return encrypted 

def decrypt(encrypted,shift):
    return encrypt(encrypted, -shift)

def crack(encrypted):
    cracked = []
    for shift in range(26):
        cracked.append(decrypt(encrypted,shift))
    return cracked

if __name__ == '__main__':
    print(shift_char('H',26))
    #print(shift_char('H',25))
    #print(shift_char('H',24))
    print(shift_char('H',23))
    #print(shift_char('h',26))
    #print(shift_char('h',25))
    #print(shift_char('h',24))
    #print(shift_char('h',23))
    #print(encrypt('Hello_World!!',3))
    #print(decrypt('KHOOR_ZRUOG!!',3))
    #print(crack('KHOOR_ZRUOG!!'))
    print(crack('HELLO_WORLD!!!'))
    print(crack('hello_world!!!'))

