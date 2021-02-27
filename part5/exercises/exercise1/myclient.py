import sys
#from pathlib import Path
#sys.path.append(Path(__file__).parent)
#import mymod

name = input('Pass filename : ')
expectedChars = int(input('Pass expected chars number : '))
expectedLines = int(input('Pass expected lines number : '))

if __name__ == '__main__':
    mymod.test(name, expectedChars, expectedLines)

