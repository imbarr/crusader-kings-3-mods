import re

regex1 = re.compile("\t4769\\.1\\.1 = \\{")
regex2 = re.compile("\t\tbirth = (\d+)")

with open("input.txt") as input:
    lines = input.readlines()
    result = []

    hold = None
    for line in lines:
        if regex1.match(line):
            hold = line
        else:
            match2 = regex2.match(line)
            if match2:
                age = int(match2.group(1))
                born = 354 - age
                hold = hold.replace("4769", str(born))
                result.append(hold)
                result.append("\t\tbirth = yes\n")
            else:
                result.append(line)

    with open("output.txt", "w") as output:
        output.writelines(result)
