import sys,string
from pathlib import Path

def countLines(name):
    count = 0
    for i in open(Path(__file__).parent / name).readlines(): count += 1
    return count

def countChars(name):
    count = 0
    for i in open(Path(__file__).parent / name).read():      
        if i.isalpha(): count += 1
    return count

# 23 chars
# 4 lines
def test(name,expectedChars,expectedLines):
    lines = countLines(name)
    chars = countChars(name)
    if lines == expectedLines: print('Lines ok!')
    else: print('Lines error! value got : {0}'.format(lines))
    if chars == expectedChars: print('Chars ok!')
    else: print('Chars error! value got : {0}'.format(chars))
