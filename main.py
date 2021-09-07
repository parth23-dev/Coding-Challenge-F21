import nltk.tokenize
from textblob import TextBlob

# Reading the text file into a string
with open('input.txt', 'r') as file:
    fileText = file.read().replace('\n', '')

# Performing Sentiment Analysis on the entire text file
fileBlob = TextBlob(fileText)
print("The overall sentiment of the text file is: ")
print(fileBlob.sentiment)
print("\n")

# Splitting up the text file string into individual sentences
sentenceList = nltk.tokenize.sent_tokenize(fileText)
sentenceSentiment = []

# Performing Sentiment Analysis on each sentence in the file
i = 0
while i < len(sentenceList):
    sentenceBlob = TextBlob(sentenceList[i])
    sentenceSentiment.append(sentenceBlob.sentiment)
    i = i + 1

# Setting up the initial conditions for comparisons of each sentence
j = 1
lowPolarity = sentenceSentiment[0].polarity
highPolarity = sentenceSentiment[0].polarity
lowSubjectivity = sentenceSentiment[0].subjectivity
highSubjectivity = sentenceSentiment[0].subjectivity

lowPolarityIndex, highPolarityIndex, lowSubjectivityIndex, highSubjectivityIndex = 0, 0, 0, 0

# Going through each sentence's sentiment scores to find the highest and lowest polarity & subjectivity scores
while j < len(sentenceList):
    if(sentenceSentiment[j].polarity < lowPolarity):
        lowPolarity = sentenceSentiment[j].polarity
        lowPolarityIndex = j

    if(sentenceSentiment[j].polarity > highPolarity):
        highPolarity = sentenceSentiment[j].polarity
        highPolarityIndex = j

    if (sentenceSentiment[j].subjectivity < lowSubjectivity):
        lowSubjectivity = sentenceSentiment[j].subjectivity
        lowSubjectivityIndex = j

    if (sentenceSentiment[j].subjectivity > highSubjectivity):
        highSubjectivity = sentenceSentiment[j].subjectivity
        highSubjectivityIndex = j

    j = j + 1

# Outputting the results to the user
print(f"The sentence with the lowest polarity has a polarity score of: {lowPolarity}")
print("The sentence with the lowest polarity is: " + sentenceList[lowPolarityIndex])
print("\n")
print(f"The sentence with the highest polarity has a polarity score of: {highPolarity}")
print("The sentence with the highest polarity: " + sentenceList[highPolarityIndex])
print("\n")
print(f"The sentence with the lowest subjectivity has a subjectivity score of: {lowSubjectivity}")
print("The sentence with the lowest subjectivity: " + sentenceList[lowSubjectivityIndex])
print("\n")
print(f"The sentence with the highest subjectivity has a subjectivity score of: {highSubjectivity}")
print("The sentence with the highest subjectivity: " + sentenceList[highSubjectivityIndex])






