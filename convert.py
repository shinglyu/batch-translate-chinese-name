import pinyin
import argparse


def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

def toPinyin(s, rearrange=False):
    s = s.strip()
    if isEnglish(s):
        return s

    chars = []
    if rearrange:
        firstname=s[1:]
        lastname=s[0]
        chars.append(pinyin.get(firstname, format="strip", delimiter="-").strip("-"))
        chars.append(pinyin.get(lastname, format="strip", delimiter="-"))
    else:
        chars+= pinyin.get(s, format="strip", delimiter=" ").split()
    return " ".join(map(lambda x: x.capitalize(), chars))


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filename', help='The input filename')
    parser.add_argument('--rearrange', '-r', help='Rearrange into <first-name> <last name> format', action='store_true')

    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.readlines()
    output = []
    for line in lines:
        output.append(toPinyin(line, args.rearrange).strip())

    for line in output:
        print(line)

if __name__ == "__main__":
    main()



