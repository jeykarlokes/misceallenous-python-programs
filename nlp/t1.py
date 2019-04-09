from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer
filtered_sentence = []
fair_draft = []
example_sent = "Text summarization is the process of shortening a text document with software, in order to create a summary with the major points of the original document. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. Automatic data summarization is part of machine learning and data mining. In the scenario, I had developed a text summarization using python with nltk tool.i had removed the stopwords in the text. Stopwords means that it provides an unecessary meaning to the given sentences.and I had the statistics table of words it calculates how many times an each word is occurred in the paragraph based on that statistics assign the sores to the sentences depending upon the words contain and in the frequency table finally I created a list where it provides the summary of the every sentences with a certain score.by doing this we can able to reduce the  paragraph in to less number of sentences with that actual meaning of the sentences should not change ."
stop_words_set = set(stopwords.words('english'))
sentence_token = sent_tokenize(example_sent)
tokenization_of_sentences = word_tokenize(example_sent)
print(tokenization_of_sentences)
filtered_sentence = [w for w in tokenization_of_sentences if not w in stop_words_set]

for w in tokenization_of_sentences:
    if w not in stop_words_set:
        filtered_sentence.append(w)


ps = PorterStemmer()
for w in filtered_sentence:
    fair_draft.append(ps.stem(w))



print("the fair draft is ",fair_draft)

print("$"*20)
print("the filterd sentence is " ,filtered_sentence)
