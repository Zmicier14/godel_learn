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
    reverse_str = ''

    i = 0

    for char in str:
        if char not in ' ':
            word = word + char
        if (char in ' ') or (i == len(str) - 1):
            words.append(word)
            word = ''
        i += 1

    words.reverse()

    j = 0
    while j < len(words):
        if j < len(words) - 1:
            reverse_str = reverse_str + words[j] + ' '
        else:
            reverse_str = reverse_str + words[j]
        j += 1

    return reverse_str

print(reverse_string(input('Please input the string:')))
#print(f"{reverse_string('I hate Lukashenko')}.")