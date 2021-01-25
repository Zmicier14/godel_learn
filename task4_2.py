import sys
def open_read_file(name_file):
    file_open = open(name_file, 'r')
    file_content = file_open.read()
    file_open.close()

    return file_content

content_file = []    
for i in range(1, len(sys.argv) - 1):
    content_file.append(open_read_file(sys.argv[i]))

    

print(content_file)
