from __future__ import absolute_import
from __future__ import print_function
import six


import rake
import operator
import io


stoppath = "data/stoplists/SmartStoplist.txt"


rake_object = rake.Rake(stoppath)
sample_file = io.open("data/docs/mp.txt", 'r',encoding="iso-8859-1")
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
