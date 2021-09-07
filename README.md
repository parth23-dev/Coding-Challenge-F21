# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## My Approach To Solving The Problem & Results

At first, I was not too familiar with Sentiment Analysiis or just natural language processing in general so I began by doing some research. I first read the Wikipedia Article that was linked and I then went on to read an article about [Emotion and Sentiment Analysis](https://www.kdnuggets.com/2018/08/emotion-sentiment-analysis-practitioners-guide-nlp-5.html) on KD Nuggets that went more in depth about the different types of Sentiment Analsysis. Through my research I learned that there are two types of Sentiment Analsysis, Supervised Machine Learning approaches and Lecxicon based approaches. I ended up going with the Lexicon based approach which uses pre built dictionaries to evaluate the sentiment of the text rather than the Supervised Machine Learning which requires pre-labeled text. There are many popular lexicon's but I ended up going with Textblob lexicon through their Textblob Library as it had one of the most coprehensive dictionary and was updated regularly.

<br>

After running my program, I was able to get both an overall polarity and subjectivity score as part of my sentiment analysis. Here were those results:

**The overall sentiment of the text file is: 
Sentiment(polarity=0.21014141414141416, subjectivity=0.5934949494949496)**

The polarity score tells how positive or how negative the text is, where positive 1.0 is the most positive, and negative 1.0 is the most negative. In this case, the sentiment analysis found the entire text file to have a score of 0.21014141414141416 which tells us that the text ls overall more positive than negative (greater than 0) but not super positive as it was only ~ .2 / 1.0 which would be approximately 20% positive. There is also another part of sentiment analysis, the subjectivity score. The subjecttivity score tells us how opinionated or how factual the text is so 0.0 means the text is very factual while positive 1.0 means the text is very opinionated. My sentiment analsysis found that this text was more opionated than it was factual because 0.5 would be the split between half factual and half opionated but with a subjectivity score of 0.5934949494949496, this text leans toward the more opionated side of the analysis.

<br>

I also ended up running an individual sentence analysis on the text file given and I was able to find the most polar score and sentence, the least polar score and sentence, the most subjective score and sentence, and the least subjective score and sentence.


Here are my results:

**The sentence with the lowest polarity has a polarity score of: -0.35**

**The sentence with the lowest polarity is: And I said, `Well, Dr. Johnson also said, dear boy,that "He is no wise man that will quit a certainty for an uncertainty.**

<br>

**The sentence with the highest polarity has a polarity score of: 0.625**

**The sentence with the highest polarity: Power, Isaid, And you, quoting Dr. Johnson, said `Knowledge is more thanequivalent to force!'**

<br>

**The sentence with the lowest subjectivity has a subjectivity score of: 0.0**

**The sentence with the lowest subjectivity: "Stop blushing.**

<br>

**The sentence with the highest subjectivity has a subjectivity score of: 1.0**

**The sentence with the highest subjectivity: and 'A dwarf on a giant's shoulders of thefurthest of the two!'**

One things that I found really interesting through the individual sentence scores is that with the subjectivity scores hit the highest and lowest subjective scores possible with their most and least subjective sentences while the polarity scores were not even close to hitting the highest and lowest scores possible in their least and most subjective sentences.

<br>

Overall, I felt like the sentiment analysis was pretty spot on as before I started the analysis I read over the text article and it definately seemed to have more positive connotations than negative ones so seeing the overall score being positive aligned with what I thought earlier. Also, unlike the polar score, the sentiment score was hard to judge on first glance of the text file as it was difficult to guage how opionated/factual each sentence was but after reading the most and least subjective sentneces through my indiviodual sentence analysis and going back through the text file, the subjectivity score started making more sense to me as well. After using Sentiment Analsysis for the first time, I can definately see how this can be a super powerful tool and can have real world application. I think that using the Machine Learning approach with labeled text could also be super interesting and could maybe even yield more accurate results, so I definately have to give it a try at some point. I really enjoyed learning more about NLP and hope to keep doing so throughout the semester!

<br>

**Libraries Used:** [TextBlob](https://textblob.readthedocs.io/en/dev/)
<br>
**Langauge Used:** Python


