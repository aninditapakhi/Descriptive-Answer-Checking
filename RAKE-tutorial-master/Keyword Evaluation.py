from __future__ import absolute_import
from __future__ import print_function
import six
import language_check

import rake
import operator
import io

sample_file = io.open("data/docs/mp2.txt", 'r',encoding="iso-8859-1")
n=0
for line in sample_file:
    words=line.split()
n=len(words)
if(n>=200):
    marks1=10
else:
    marks1=5
print("Marks obtained for word length",marks1,"/10")
a=marks1


stoppath = "data/stoplists/SmartStoplist.txt"

rake_object = rake.Rake(stoppath)
sample_file = io.open("data/docs/mp2.txt", 'r',encoding="iso-8859-1")
text = sample_file.read()

sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)

stopwords = rake.load_stop_words(stoppath)
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern, stopwords)
print("Phrases:", phraseList)

wordscores = rake.calculate_word_scores(phraseList)

keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    print("Keyword: ", keyword[0], ", score: ", keyword[1])
print(text)
keyw=dict(rake_object.run(text))
print(keyw)

f1=io.open("data/docs/mpques1.txt", 'r',encoding="iso-8859-1")
text1=f1.read()
l=text1.split("\n\n")
kw=l[2].split("\n")
print("keyword in original file:",kw)

c=0
for i in keyw:
    for j in kw:
        if(i==j):
            c=c+1
print("count:",c)

total=len(kw)
percentage=(c/total)*100
if(percentage>=90):
    marks2=20
    print("Marks obtained for keyword:",marks2,"/20")

elif(percentage>=80 or percentage<90):
    marks2=18
    print("Marks obtained for keyword:",marks2,"/20")

elif(percentage>=70 or percentage<80):
    marks2=16
    print("Marks obtained for keyword:",marks2,"/20")

elif(percentage>=60 or percentage<80):
    marks2=14
    print("Marks obtained for keyword:",marks2,"/20")

elif(percentage>=50 or percentage<60):
    marks2=12
    print("Marks obtained for keyword:",marks2,"/20")

else:
    marks2=10
    print("Score:",marks2,"/20")

b=marks2



tool=language_check.LanguageTool('en-US')
#input=open("mp.txt","r")
count=0
text=str(sample_file.read())
txtlen=len(text.split())
setxt = set(text.split())
setlen = len(setxt)
matches=tool.check(text)
#print("Error:",matches)
print("No. of Errors:",len(matches))
noOfError=len(matches)
if noOfError<=5:
    marks3=10
elif noOfError<=10:
    marks3=8
elif noOfError<=15:
    marks3=5
else:
    marks3=3

if setlen>(txtlen/2):
    marks3+=10
else:
    marks3+=5
print("Marks obtained after parsing:",marks3,"/20")
mes2 = Message(root, text="Marks obtained after parsing:"+ str(marks3)+"/20")
c=marks3
mes2.grid()
print("Marks obtained out of 50 is:",a+b+c,"/50")
