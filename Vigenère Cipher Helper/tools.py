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
    """
    This function generates a series of circular shifts of the English alphabet. 
    Starting with the initial alphabet sequence ['a', 'b', 'c', ... 'z'], 
    it creates a list of shifted sequences where each subsequent sequence is obtained
    by moving each letter one position to the right and wrapping around from 'z' to 'a'.
    The result is a collection of alphabet sequences with each letter shifted to the 
    next position, preserving the cyclic nature of the English alphabet.
    This generator is useful for various applications involving encryption, encoding,
    or creating alphabet-related patterns and sequences.    

    shifts = 1:
    
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    shifts = 3:

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
    ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b']
    
    """

    start_char = 'a'
    end_char = 'z'

    result = []
    for iteration in range(shifts):
        a = [i for i in char_range(start_char,end_char)]
        result.append(a)
        start_char = chr(ord(start_char) + 1)
        if end_char == 'z':
            end_char = 'a'
        else:
            end_char = chr(ord(end_char) + 1)
    return result