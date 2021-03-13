import sys
def open_read_file(name_file):
    """ (file open for reading) -> str

    Return a string of all content from open file name_file.
    """
    file_open = open(name_file, 'r')
    file_content = file_open.read()
    file_open.close()

    return file_content

content_file = []    
for i in range(1, len(sys.argv) - 1):
    content_file.append(open_read_file(sys.argv[i]))

file_write = open(sys.argv[-1], 'w')
i = 0
for i in range(len(content_file)):
    if i < (len(content_file) - 1):
        file_write.write(content_file[i])
        file_write.write('\n')
    else:
        file_write.write(content_file[i])
file_write.close()