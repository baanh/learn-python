'''
Created on 1/23/2019 @author: TBABAIAN
 
Starting code for hw2. Place the rest of the code below the comment line 
'''
def fromFile(file):
    file = open(file, 'r')
    line = file.read() 
    return line 

txtfile = input("Please enter the name of the file containing the text: ")
textOrig = fromFile(txtfile)
print('Contents of file',txtfile)
print (textOrig)

'''
Solution created on 2/10/2019 @author: Luke Nguyen

The program takes a file_name input, a keyword input, and a line_length input.
It then prints out a sentence in the given text that contains the keyword.
It also prints out a text schema with periods as characters with the keyword, 
the schema spans line_length characters per line.
'''
textLower = textOrig.lower()
textLowerNoPunc = textLower.replace(".", " ").replace("!", " ").replace(",", " ").replace("?", " ") \
    .replace(";", " ").replace(":", " ").replace("-", " ").replace("\"", " ").replace("\'", " ").replace("\n", " ")

word = input("Enter the keyword:")
word = word.lower()

# Get the word in original form
if (textLowerNoPunc.startswith(word + " ")): # if the text starts with the keyword, the word's position is 0
    wordOrigPos = 0
else: # if not, look for " word " in the text
    wordOrigPos = textLowerNoPunc.find(" " + word + " ") + 1
    if wordOrigPos == 0: # if the finding result is -1, the word does not exist, exit the program
        print("\'" + word + "\' does not appear in the text")
        exit()
    
wordOrig = textOrig[wordOrigPos:wordOrigPos+len(word)]

length = int(input("Enter the line length:"))
print("Outputting the sentence followed by the text schema with", length, "characters per line:")
print("*****")

# Capitalize the keyword in the text origin
textOrigCap = textOrig[:wordOrigPos] + wordOrig.upper() + textOrig[wordOrigPos+len(wordOrig):]

sentence = ""
startPos = 0
endPos = 0

# Extract textSplit1 and textSplit2
textSplits = [1, 2]
textSplits[0] = textOrig[:wordOrigPos]
textSplits[1] = textOrig[wordOrigPos + len(wordOrig):]

# Find the sentence start position
if textSplits[0].rfind(".") == -1 and textSplits[0].rfind("!") == -1 and textSplits[0].rfind("?") == -1: # key word is in the 1st sentence
    startPos = 0
else: # key word is not in the 1st sentence
    startPos = max(textSplits[0].rfind("."), textSplits[0].rfind("!"), textSplits[0].rfind("?")) + 2

# Find the sentence end position
if textSplits[1].find(".") != -1 and textSplits[1].find("!") != -1 and textSplits[1].find("?") != -1: # if ! . and ? exist in the text
    endPos = min(textSplits[1].find("."), textSplits[1].find("!"), textSplits[1].find("?"))
elif textSplits[1].find(".") != -1 and textSplits[1].find("!") != -1:
    endPos = min(textSplits[1].find("."), textSplits[1].find("!"))
elif textSplits[1].find(".") != -1 and textSplits[1].find("?") != -1:
    endPos = min(textSplits[1].find("."), textSplits[1].find("?"))
elif textSplits[1].find("!") != -1 and textSplits[1].find("?") != -1:
    endPos = min(textSplits[1].find("!"), textSplits[1].find("?"))
elif textSplits[1].find(".") != -1: # if only . exists in the text, find the first existence
    endPos = textSplits[1].find(".")
elif textSplits[1].find("!") != -1: # if only ! exists in the text, find the first existence
    endPos = textSplits[1].find("!")
else:
    endPos = textSplits[1].find("?")

# Get the sentence from the text origin
sentence = textOrigCap[startPos:len(textSplits[0]) + len(word) + endPos + 1]

# Replace line breaks in sentence with spaces
sentence = sentence.replace("\n", " ")

# Create text schema
lastLine = (len(textOrig) % length) * "."
textSchema = ('.' * length + '\n') * (len(textOrig) // length) + lastLine

# Identify which line number of the text schema the keyword will be in
lineNum = wordOrigPos // length

# The line number is equal the number of additional line breaks
newWordOrigPos = wordOrigPos + lineNum

# Replace periods with the keyword in the text schema
if wordOrigPos // length == (wordOrigPos + len(wordOrig) - 1) // length: # word spans one line
    textSchema = textSchema[:newWordOrigPos] + wordOrig.upper() + textSchema[newWordOrigPos+len(wordOrig):]
else: # word spans more than one line
    wordSplitPos = length * (lineNum + 1) - wordOrigPos
    textSchema = textSchema[:newWordOrigPos] + wordOrig.upper()[:wordSplitPos] + "\n" \
        + wordOrig.upper()[wordSplitPos:] + textSchema[newWordOrigPos+len(wordOrig)+1:]

# Print the output
print(sentence)
print(textSchema)