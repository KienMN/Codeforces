def split(string):
    isDigits = False
    parts = []
    part = ""
    for i in range(0, len(string)):
        if isDigits:
            if ord(string[i]) <= 57 and ord(string[i]) >= 48:
                part += string[i]
            else:
                isDigits = not isDigits
                parts.append(part)
                part = string[i]

        else:
            if string[i] <= 'Z' and string[i] >= 'A':
                part += string[i]
            else:
                isDigits = not isDigits
                parts.append(part)
                part = string[i]
        if i == len(string) - 1:
            parts.append(part)
    return parts

def transform(parts):
    m = len(parts)
    res = ""
    if m <= 2:
        r = int(parts[1])
        c = 0
        col = list(parts[0])
        for i in range(0, len(col)):
            c += (ord(col[i]) - 64) * (26 ** (len(col) - 1 - i))
        res = "R" + str(r) + "C" + str(c)
    else:
        r = int(parts[1])
        c = int(parts[3])
        col = ""
        while c != 0:
            t = int(c / 26)
            remain = c % 26
            if remain != 0:
                col = chr(remain + 64) + col
            else:
                col = "Z" + col
                t -= 1
            c = t
        res = col + str(r)
    return res

n = int(input())
for i in range (0, n):
    inp = input()
    print(transform(split(inp)))
