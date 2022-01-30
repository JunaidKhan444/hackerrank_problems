def split_and_join(line):
    splitted_line = line.split(" ")
    changed_line = "-".join(splitted_line)
    return changed_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
