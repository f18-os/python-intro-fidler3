import re
import string
import sys
from collections import OrderedDict

frequency = {}
txtinput =  sys.argv[1]
txtoutput =  sys.argv[2]

textreader = open(txtinput, 'r')
text = textreader.read().lower()
text.translate(string.punctuation)
text.strip()
regex = r'\w+'
matches = re.findall(regex, text)
for word in matches:
    count = frequency.get(word,0)
    frequency[word] = count + 1
print(frequency)

frequencylist = OrderedDict(sorted(frequency.items()))
#frequencylist.sort()
out = open(txtoutput, 'w')

for words in frequencylist:
    a = words+ ' ' + str(frequency[words]) + '\n'
    out.writelines(a)
out.close()
