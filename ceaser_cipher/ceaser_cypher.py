def shift_char(char,shift):
    char_code = ord(char)
    if ord('A') <= char_code <= ord('Z'):
        shifted_code = char_code + shift
        if shifted_code > ord('Z'):
            wrap = shifted_code % ord('Z')
            shifted_code = ord('A') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    elif ord('a') <= char_code <= ord('z'):
        shifted_code = char_code + shift
        if shifted_code > ord('z'):
            wrap = shifted_code % ord('z')
            shifted_code = ord('a') + wrap
        shifted_char = chr(shifted_code)
        return shifted_char
    else:
        return char

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

if __name__ == '__main__':
    print(shift_char('H',26))
    print(shift_char('H',25))
    print(shift_char('H',24))
    print(shift_char('H',23))
    print(shift_char('h',26))
    print(shift_char('h',25))
    print(shift_char('h',24))
    print(shift_char('h',23))

