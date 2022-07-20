import re

regex = re.compile("(\d+).*")

with open("input.txt") as input:
    lines = input.readlines()
    result = []

    for line in lines:
        match = regex.match(line)
        if not match:
            result.append(line)
            continue
        orig = int(match.group(1))
        line = line.replace(str(orig), str(orig - 1))
        result.append(line)

    with open("output.txt", "w") as output:
        output.writelines(result)