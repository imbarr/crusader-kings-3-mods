import re
regex = re.compile(".*province = (\d+).*")

with open("input.txt") as input:
    result = []

    for line in input.readlines():
        m = regex.match(line)
        if m:
            num = m.group(1)
            result.append(num + " = { winter_severity_bias = 0.45}\n")

    with open("output.txt", "w") as output:
        output.writelines(result)