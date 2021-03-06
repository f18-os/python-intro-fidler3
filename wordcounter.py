import re
import string
import sys

frequency = {}
txtinput =  sys.argv[1]
txtoutput =  sys.argv[2]

textreader = open(txtinput, 'r')
text = textreader.read()
text.translate(None, string.punctuation)
text.strip()
regex = r'\w+'
matches = re.findall(regex, text)
for word in matches:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequencylist = frequency.keys()
frequencylist.sort()
out = open(txtoutput, 'w')

for words in frequencylist:
    a = words+ ' ' + str(frequency[words]) + '\n'
    out.writelines(a)
out.close()