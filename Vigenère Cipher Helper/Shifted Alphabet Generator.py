def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    
    if(ord(c2) + 1 > ord(c1)):
        for c in range(ord(c1), ord(c2)+1):
            yield chr(c)
    
    else:
        for c in range(ord(c1), ord('z') + 1):
            yield chr(c)
        for c in range(ord('a'),ord(c2) + 1):
            yield chr(c)

def shifted_alphabet_gen(shifts):
    start_char = 'a'
    end_char = 'z'

    result = []
    for count in range(shifts):
        #a = [start_char]
        #a.append([i for i in char_range('a','z')])
        a = [i for i in char_range(start_char,end_char)]
        result.append(a)
        start_char = chr(ord(start_char) + 1)
        if end_char == 'z':
            end_char = 'a'
        else:
            end_char = chr(ord(end_char) + 1)
    return result