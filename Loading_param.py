def Load(filename="Parameters.txt"):
    d = {}
    FILE = open(filename)
    for line in FILE:
        name, value = line.split(":")
        d[name] = value.strip()
    return d


