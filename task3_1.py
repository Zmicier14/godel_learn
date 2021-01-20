def reverse_string(str):
    ''' (str) -> str
    Returns reversed string str.

    >>> reverse_string('I hate Lukashenko')
    'Lukashnko hate I'
    >>> reverse_string('Python is pretty interesting language')
    'language interesting pretty is Python
    '''

    word = ''
    words = []
 #   reverse_str = ''

    i = 0

    for char in str:
        if char not in ' ':
            word = word + char
        if (char in ' ') or (i == len(str) - 1):
            words.append(word)
            word = ''
        i += 1

 #'''   j = len(words)

 #   while j > 0:
#        reverse_string = reverse_str 
#'''
    words.reverse()
    return words

print(reverse_string('I hate Lukashenko'))