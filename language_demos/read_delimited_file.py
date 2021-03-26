
def read_delimited_lines(file_handle, delimiter='|',
                         omit_delimiter=False, read_size=4):

    delimited_line = ""
    data = file_handle.read(read_size)

    while data:

        delimiter_index = data.find(delimiter)

        if delimiter_index < 0:
            delimited_line += data
        else:
            delimited_line += data[:delimiter_index
                                   if omit_delimiter else delimiter_index + 1]
            yield delimited_line.strip()
            delimited_line = data[delimiter_index + 1:]

        data = file_handle.read(read_size)

    if len(delimited_line) > 0:
        yield delimited_line


with open("lorem.txt") as colors_file:

    for line in read_delimited_lines(colors_file, "."):
        print(line)
