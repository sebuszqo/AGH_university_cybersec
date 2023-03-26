import argparse
import re

# how to use?
# for example:
# python3 skrypt.py my_function:function,function1:fun1  file.py ; cat file.py

# to use help
# python3 skrypt.py -h

# writing to file
def writeToFile(towrite):
    f = open("file.py", "w")
    for i in range(len(towrite)):
        f.write(towrite[i])
    f.close()

# reading files 
def readFile():
    with open(str(args.File[0])) as f:
        lines = [line for line in f]
    return lines

# reading file line by line and changing what user want to change by using regex
# then appending to array and writing to a file
def changefile(string):
    lines = readFile()
    towrite = []
    # print(len(lines))
    for i in range(len(lines)):
        towrite.append(re.sub(f'{string[0]}[()]+',f'{string[1]}()',lines[i]))
    writeToFile(towrite)
    # cutting array of functions to change
    return string[2:]



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process function names')
    parser.add_argument('Names', metavar='names', type=str,
                        help='list of function names')
    parser.add_argument('File', metavar='file', nargs='+',
                        help='python script name')

    args = parser.parse_args()

    # splitng functions to change by using regex 
    string = re.split(r':|,', args.Names)

   
    for i in range(int(len(string) // 2)):
        string = changefile(string)




# --------- Some code that was a try code ---------
# lines = readFile()
# towrite = []
# for i in range(len(lines)):
#     towrite.append(re.sub(f'{string[0]}[()]+',f'{string[1]}()',lines[i]))
# writeToFile()

# lines = readFile()
# towrite = []
# for i in range(len(lines)):
#     towrite.append(re.sub(f'{string[2]}[()]+',f'{string[3]}()',lines[i]))
# writeToFile()

# splitted = args.Names.split(',')
# firstfun = splitted[0].split(':')
# secondfun = splitted[1].split(':')

