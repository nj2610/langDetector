import os
import csv
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))


langList = ['bash', 'c', 'cpp', 'csharp', 'css', 'go', 'java', 'js', 'php', 'python', 'ruby', 'scala', 'sql']

basePath = 'path to data'

csvFile = open('trainDataAllNew.csv','w', newline='')
wr = csv.writer(csvFile)
wr.writerow(['code', 'lang'])

for lang in langList:
    fullPath = basePath + '\\' + str(lang)
    fileList = os.listdir(fullPath)

    for files in fileList:
        try:
            filePath = fullPath + '\\' + files
            print(files)
            f= open(filePath, 'r')
            codes = f.read()
            word_tokens = word_tokenize(codes) 
            filtered_sentence = [] 
  
            for w in word_tokens: 
                if w not in stop_words: 
                    filtered_sentence.append(w) 

            filteredString = " ".join(filtered_sentence)
            words = re.findall(r'\w+', filteredString)
            word_counts = Counter(words)
            topWords = word_counts.most_common(20)
            string = ''
            for tup in topWords:
                string += tup[0]
                string += ' '
            string = string.strip('\n')
            string= string.encode('utf-8')
            string = string.decode('utf-8')
            row = [string, lang]
            wr.writerow(row)
        except:
            pass

