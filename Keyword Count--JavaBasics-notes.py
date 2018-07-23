###""Created on Mon Jul 23 02:25:52 2018
import PyPDF2
import csv
from collections import OrderedDict, Counter
from nltk.corpus import stopwords
##reading the pdf file as binary !!
pdfobject = open('JavaBasics-notes.pdf', 'rb')
##loading file through PyPF2 module
pdfReader = PyPDF2.PdfFileReader(pdfobject)
string = ''

##iterating through pdf pages and appending the text to predefined variable(string)
for i in range(pdfReader.numPages):
    pageobject = pdfReader.getPage(i)
    string+=(pageobject.extractText())
pdfobject.close()

## removing the headers,footer, numbers, puntuactions, etc-> keeping only words
list_replace=["jGuru.com.","All Rights Reserved.","Java Basics©","'","1996-2003"]
for wrd in list_replace:
    string=string.replace(wrd," ")
to_replace='"©@|\/,;!:`~#$%^&*({}><?)[]1234567890.,-_='
for char in to_replace:
    string=string.replace(char," ")

## removing spaces, splitting the text and convertiing it into a list of its words
text=string.split()
text=" ".join(text)
words=text.split()

##removing stop words
stop_words = stopwords.words('english')
stop_words.append("The")
stop_words=set(stop_words)
filtered_words=[]


###defining example keyword list
examplekeywords=["array","Java","class","C++","Basics"]
examplekeywordcount={"array":0,"Java":0,"class":0,"C++":0,"Basics":0}
for i in range(len(filtered_words)):
    for element in examplekeywords:
        if filtered_words[i]==element:
            examplekeywordcount[element]+=1
keywordcount=OrderedDict(sorted(examplekeywordcount.items(), key=lambda x: x[1]))
with open('Example_Keywords_Count.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in keywordcount.items():
        writer.writerow([key, value])
## 20 Most common words in text        
for w in words:
    if w not in stop_words:
        filtered_words.append(w)
dict_of_all_words=dict()
for w in filtered_words:
    if w in dict_of_all_words:
        dict_of_all_words[w]=dict_of_all_words[w]+1
    else:
        dict_of_all_words[w]=1
most_common_words=dict(Counter(dict_of_all_words).most_common(20))
CommonWords=OrderedDict(sorted(most_common_words.items(), key=lambda x: x[1]))
with open('20_Most_Common_Words.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in CommonWords.items():
        writer.writerow([key, value])        