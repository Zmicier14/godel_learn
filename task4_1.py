from tkinter.filedialog import askopenfile

def reads_file(file_name):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    file_name.
    """

    i = 0
    string = ''
    wordlist = []
    for line in file_name:
        if line != '':
            wordlist.append(line[:-1])

    return wordlist

file_1 = askopenfile(mode='r', title='Select first file')
string_file_1 = reads_file(file_1)
file_1.close()

file_2 = askopenfile(mode='r', title='Select first file')
string_file_2 = reads_file(file_2)
file_2.close()
common_strings = []

for string in string_file_1:
    if (string in string_file_2) and (string not in common_strings):
        common_strings.append(string)

print(common_strings)