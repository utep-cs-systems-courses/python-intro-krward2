import sys        # command line arguments
import string     # string manipulation and formatting
import os         # checking if file exists

if len(sys.argv) != 3:
    print("Correct usage is: python wordCount.py input.txt output.txt")
    exit()

input = sys.argv[1]
output = sys.argv[2]

if not os.path.exists(input):
    print("Input text file path is not valid.")
    exit()

wordCounter = dict()

with open(input,"r") as inputFile:
    for line in inputFile:
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        for word in line.split():
            if word in wordCounter:
                wordCounter[word] += 1
            else:
                wordCounter[word] = 1

sortedDict = sorted(wordCounter.items(), key = lambda x: x[1], reverse = True)

with open(output, "w") as outputFile:
    for i in sortedDict:
        outputFile.write(i[0] + " " + str(i[1]) + "\n")
