def reads_file(file_name):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    file_name.
    """
    
    string = ''
    wordlist = []
    for line in file_name:
        if line != '':
            wordlist.append(line[:-1])

    return wordlist

file_1 = open(input('Please input the name of the first file: '), 'r')
string_file_1 = reads_file(file_1)
file_1.close()

file_2 = open(input('Please input the name of the second file: '), 'r')
string_file_2 = reads_file(file_2)
file_2.close()
common_strings = []

for string in string_file_1:
    if (string in string_file_2) and (string not in common_strings):
        common_strings.append(string)

print(common_strings)