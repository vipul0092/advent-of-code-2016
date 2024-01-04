def read_lines(path):
    file = open(path, "r")
    lines = file.read().split("\n")
    return lines
