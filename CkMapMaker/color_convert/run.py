import re

def convert_color(hex):
    return str(int(hex[0:2], 16)) + ';' + str(int(hex[2:4], 16)) + ';' + str(int(hex[4:6], 16))

startid = 9
regex = re.compile('.*?;(.*?);(.*?);x;')

with open("input.txt") as file:
    output = []
    for line in file.readlines():
        match = regex.match(line)
        if match is None:
            raise Exception("Match failed")
        id = startid
        startid += 1
        color_hex = match.group(1)
        color = convert_color(color_hex)
        name = match.group(2)
        output.append(str(id) + ';' + color + ';' + name + ';x;\n')

with open("output.txt", "w") as out_file:
    out_file.writelines(output)
