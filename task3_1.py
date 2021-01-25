def reverse_string(string):
    ''' (str) -> str
    Returns reversed string str.

    >>> reverse_string('I hate Lukashenko')
    'Lukashnko hate I'
    >>> reverse_string('Python is pretty interesting language')
    'language interesting pretty is Python
    '''

    words = string.split()
    words.reverse()
    reverse_str = ' '.join(words)

    return reverse_str

print(reverse_string(input('Please input the string:')))