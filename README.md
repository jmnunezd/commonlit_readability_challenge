# commonlit_readability_challenge
My Attempt on this Kaggle competition, I'm using that dataset for my Udacity ND


### Domain Background
“Can machine learning identify the appropriate reading level of a passage of text, and help inspire learning? Reading is an essential skill for academic success. When students have access to engaging passages offering the right level of challenge, they naturally develop reading skills.”
- Quoting Kaggle CommonLit Readability competition.

The main idea here is to take leverage on the NLP knowledge the Nanodegree have gave me and find a way to tackle this real world problem. My thoughts right now are centered on using classic indicators of read complexity and some novelty ML techniques to give better predictions. 


### Problem Statement

“Currently, most educational texts are matched to readers using traditional readability methods or commercially available formulas. However, each has its issues. Tools like Flesch-Kincaid Grade Level are based on weak proxies of text decoding (i.e., characters or syllables per word) and syntactic complexity (i.e., number or words per sentence). As a result, they lack construct and theoretical validity. At the same time, commercially available formulas, such as Lexile, can be cost-prohibitive, lack suitable validation studies, and suffer from transparency issues when the formula's features aren't publicly available.”
- Quoting Kaggle CommonLit Readability competition.

I see a lot of potential with the idea, imagine yourself for a moment, if you could know beforehand buying a book the complexity of the text that lurks inside, that may encourage you to find books that fit your comfort level. I could easily imagine every book in a shelve with an stamp like the “best seller” one but stating the complexity. Then buying books for kids will be easier as well as for foreign people to pick books written in other languages also for older people with cognitive problems, the possibilities are endless.

Since the current indexes for text complexity aren’t perfect, nor accurate with real people opinions, there may be a way to improve current result with the help of NLP and ML. Finally making a humble contribution to cause greater than myself as finding a free, open-source complexity index is a reward on itself.


### Datasets and Inputs

The dataset that Kaggle provided takes this form:

<INSERT IMAGE>

It has 6 columns, and 2834 rows. The columns are: id, url_legal, license, excerpt, target and standard_error. The id is just the excerpt identifier, both url_legal and license contains info about the excerpt license of use. The excerpt is the actual text you want to find out the complexity, the target columns is the average reading ease according to a panel of teachers, and the standard_error is the error of such average. Please notice the target variable is a continuous number, this means this is regression problem.

They also include a test dataset, but this ones doesn’t have neither the target nor the standard_error. So, we must train the model solely using the excerpt text. 

In addition to the above dataset I made some research and found an open source repository which contains some info regarding the frequency of English words, specifically for the top 50.000 more frequent words. My idea is to use this auxiliar dataset as well to determine the “rarity” of the words in the excerpt. The link to this repo is here: https://github.com/hermitdave/FrequencyWords.


### Solution Statement

The solution is to create a model that accurately predicts the complexity of a text and it needs to be better than classic indexes (with a lesser RMSE). Then host the model into a web application that let’s people know the complexity of an excerpt in a matter of seconds. So not only accuracy maters but time as well.


### Benchmark Model

I will use two models as benchmark, first a basic linear regression between the Flesch-Kincaid test index and the target variable, this is the most popular complexity index so performing better that it, its an accomplishment in on itself. This model will give us an idea of how good are classic indicators at estimating the real complexity of a excerpt.

Secondly I’ll use other Kaggle contestant RMSE to compare against mine.


### Evaluation Metrics

The benchmark for the model will be the root mean square error (RMSE) using the predictions of the model and the real values as inputs to the formula.

<INSERT IMAGE>


### Project Design

Right now I haven’t design a full solution, I’m still exploring ideas to tackle this complicated problem and so far I see 3 possible candidates:

* Perform some feature engineer process on the excerpt to describe it better, and use such quantitative characteristic as input for a traditional regression model as a support vector regressor. We can create variables from the excerpt such as the Flesch-Kincaid test index, calculate the average number of words per sentence, the average rarity of the words in the excerpt (using the auxiliar dataset), counting the number of unique words in the text, you name it. Then use those descriptive number to train a support vector regression as usual.

* Train a LSTM in the pure style of the sentiment analysis mini-project we did in the first part of the NanoDegree. This implies creating a word dictionary and then transform every excerpt into a vector using such vocabulary. Then feed this vectors to the net and hope it will learn the complexity from it. Also notice that in the mini project we did a classification with only 2 possible outcomes: positive or negative review. In this case we have a continuous variable as output, so we may change the last layer of the net to predict a number instead of a class.

* Use a state of the art pre-trained model such as Google’s Transformer BERT to accomplish the regression task. A lot of participants are suggesting this is the approach that provides the best results and as a Machine Learning Engineer student I should be able to learn new concepts and apply them. so probably I’ll try this as my last resort if I don’t get nice result for my other two alternatives.

Also bear in mind that 2834 records to train a net is a quite low number of examples, so I’m considering to perform some form of data augmentation process, maybe duplicating the original excerpts and replacing some words with synonymous words. I still need to research more on how to do this correctly.


#### License
[MIT](https://choosealicense.com/licenses/mit/)