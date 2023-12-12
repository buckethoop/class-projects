nltk.download('punkt')
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

amazon_data = pd.read_csv('data.tsv', sep='\t', on_bad_lines='skip')

important_fields = ['star_rating', 'review_body']
amazon_data = amazon_data[important_fields]
amazon_data.dropna(subset=['star_rating'], inplace=True) #remove reviews with no star ratings

def classify_ratings(ratings):
    if(ratings in [1,2,3]):
        return 1
    else:
        return 2

amazon_data['Class'] = amazon_data['star_rating'].apply(classify_ratings)

data_class1 = amazon_data[amazon_data['Class'] == 1]
data_class2 = amazon_data[amazon_data['Class'] == 2]

review_size = 50000

class1_rand = data_class1.sample(n=review_size, random_state=4)
class2_rand = data_class2.sample(n=review_size, random_state=4)

amazon_data = pd.concat([class1_rand,class2_rand], axis=0)

contraction_dict = {
    "won't" : "will not",
    "couldn't" : "could not",
    "shouldn't" : "should not",
    "wouldn't" : "would not",
    "aren't" : "are not",
    "didn't" : "did not",
    "can't" : "can not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't" : "has not",
    "haven't" : "have not",
    "I'd" : "I would", #specifically picked this instead of I had
    "I'll" : "I will",
    "I'm" : "I am",
    "I've" : "I have",
    "isn't" : "is not",
    "let's" : "let us",
    "that's" : "that is",
    "there's": "there is",
    "they'd" : "they had",
    "they'll" : "they will",
    "weren't" : "were not",
    "what're" : "what are",
    "what's" : "what is",
    "where's" : "where is",
    "you'll" : "you will",
    "you're" : "you are",
    "it's" : "it is",
    "we're" : "we are",
    "y'all" : "you all",
    "it'll" : "it will",
    "could've" : "could have",
    "would've" : "would have",
    "should've" : "should have",
    "ain't" : "is not",
    "he'll" : "he will",
    "he's" : "he is",
    "she'll" : "she will",
    "she's" : "she is",
    "it'd" : "it would",
}

def review_avg(dataframe, column):
    dataframe['review_length'] = dataframe[column].apply(len)
    avg_length = dataframe['review_length'].mean()
    return avg_length

#generates a new column in the dataframe with cleaned reviews
def data_clean(dataframe):

    dataframe['clean_review'] = dataframe['review_body'].apply(lambda x: x.lower().strip()) #change to lowercase and remove extra spaces on beginning/end of entry
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: ' '.join([contraction_dict.get(contraction, contraction) for contraction in x.split()])) #expands contractions
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x)) #remove punctutation /does it also remove numbers?
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: BeautifulSoup(x,'html.parser').get_text()) #remove html
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: ' '.join([word for word in x.split() if len(word) >= 3]))
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: re.sub(r'http\S+|www\S+|https|S+','',x,flags=re.MULTILINE)) #remove urls
    dataframe['clean_review'] = dataframe['clean_review'].apply(lambda x: re.sub(' +', ' ', x)) #remove extra spaces

    return dataframe

amazon_data['review_body'] = amazon_data['review_body'].astype(str) #assure that all entries are in string format
cleaning_avg_length_before = review_avg(amazon_data,'review_body') #set the average length of the reviews before the data cleaning step
clean_data = data_clean(amazon_data)

cleaning_avg_length_after = review_avg(clean_data,'clean_review') #set the average length of the reviews after the data cleaning step

print(f"The average length of the reviews in terms of character length BEFORE & AFTER Data Cleaning: {cleaning_avg_length_before}, {cleaning_avg_length_after}")

#tokenize reviews and stop words
def rmv_stopwords(review):
    split_reviews = nltk.word_tokenize(review)
    tokens = [word for word in split_reviews if word not in stopwords.words('english')]

    return ' '.join(tokens)

preprocessing_avg_length_before = review_avg(amazon_data,'clean_review') #set the average length of the reviews before the data cleaning step

amazon_data['clean_review'] = amazon_data['clean_review'].apply(rmv_stopwords)

def lemmatize_review(review):
    return [WordNetLemmatizer().lemmatize(review) for token in review]

amazon_data['clean_review'] = amazon_data['clean_review'].apply(lemmatize_review)

preprocessing_avg_length_after = review_avg(amazon_data,'clean_review') #set the average length of the reviews after the data cleaning step

print(f"The average length of the reviews in terms of character length BEFORE & AFTER Preprocessing: {preprocessing_avg_length_before}, {preprocessing_avg_length_after}")

amazon_data['clean_review'] = amazon_data['clean_review'].apply(lambda x: ' '.join(x)) #assure that all entries are in string format

reviews = amazon_data['clean_review']
labels = amazon_data['Class']

#splitting data
rev_split_train, rev_split_test, labels_train, labels_test = train_test_split(reviews, labels, test_size=.2,random_state=0)


bow_vect = CountVectorizer(max_features=8000)
bow_feat = bow_vect.fit_transform(rev_split_train)
bow_test = bow_vect.transform(rev_split_test)

ss_bow = StandardScaler(with_mean=False)
bow_feat_ss = ss_bow.fit_transform(bow_feat)
bow_test_ss = ss_bow.transform(bow_test)

tfidf_vect = TfidfVectorizer(max_features=8000)
tfidf_feat = tfidf_vect.fit_transform(rev_split_train)
tfidf_test = tfidf_vect.transform(rev_split_test)

ss_tfidf = StandardScaler(with_mean=False)
tfidf_feat_ss = ss_tfidf.fit_transform(tfidf_feat)
tfidf_test_ss = ss_tfidf.transform(tfidf_test)

perceptron = Perceptron(max_iter=1000)
perceptron.fit(bow_feat_ss, labels_train)
bow_predict = perceptron.predict(bow_test_ss)

#evaluate bow
per_bow_precision = precision_score(labels_test,bow_predict)
per_bow_recall = recall_score(labels_test,bow_predict)
per_bow_f1 = f1_score(labels_test,bow_predict)

print(f"Precision: {per_bow_precision}, Recall: {per_bow_recall} , F1 score: {per_bow_f1} ")

perceptron = Perceptron(max_iter=1000)
perceptron.fit(tfidf_feat_ss, labels_train)
tfidf_predict = perceptron.predict(tfidf_test_ss)

#evaluate tf idf
per_tfidf_precision = precision_score(labels_test,tfidf_predict)
per_tfidf_recall = recall_score(labels_test,tfidf_predict)
per_tfidf_f1 = f1_score(labels_test,tfidf_predict)

print(f"Precision: {per_tfidf_precision}, Recall: {per_tfidf_recall}, F1 score: {per_tfidf_f1} ")

svm = LinearSVC(max_iter=100000)
svm.fit(bow_feat_ss, labels_train)
bow_predict = svm.predict(bow_test_ss)

#evaluate bow
svm_bow_precision = precision_score(labels_test,bow_predict)
svm_bow_recall = recall_score(labels_test,bow_predict)
svm_bow_f1 = f1_score(labels_test,bow_predict)

print(f"Precision: {svm_bow_precision}, Recall: {svm_bow_recall} , F1 score: {svm_bow_f1} ")

svm = LinearSVC(max_iter=100000)
svm.fit(tfidf_feat_ss, labels_train)
tfidf_predict = svm.predict(tfidf_test_ss)

#evaluate tf idf
svm_tfidf_precision = precision_score(labels_test,tfidf_predict)
svm_tfidf_recall = recall_score(labels_test,tfidf_predict)
svm_tfidf_f1 = f1_score(labels_test,tfidf_predict)

print(f"Precision: {svm_tfidf_precision}, Recall: {svm_tfidf_recall}, F1 score: {svm_tfidf_f1} ")

logistic = LogisticRegression(max_iter=3000)
logistic.fit(bow_feat_ss, labels_train)
bow_predict = logistic.predict(bow_test_ss)

#evaluate bow
log_bow_precision = precision_score(labels_test,bow_predict)
log_bow_recall = recall_score(labels_test,bow_predict)
log_bow_f1 = f1_score(labels_test,bow_predict)

print(f"Precision: {log_bow_precision}, Recall: {log_bow_recall} ,F1 score: {log_bow_f1} ")

logistic = LogisticRegression(max_iter=3000)
logistic.fit(tfidf_feat_ss, labels_train)
tfidf_predict = logistic.predict(tfidf_test_ss)

#evaluate tf idf
log_tfidf_precision = precision_score(labels_test,tfidf_predict)
log_tfidf_recall = recall_score(labels_test,tfidf_predict)
log_tfidf_f1 = f1_score(labels_test,tfidf_predict)

print(f"Precision: {log_tfidf_precision}, Recall: {log_tfidf_recall}, F1 score: {log_tfidf_f1} ")

naive = MultinomialNB()
naive.fit(bow_feat_ss, labels_train)
bow_predict = naive.predict(bow_test_ss)

#evaluate bow
naive_bow_precision = precision_score(labels_test,bow_predict)
naive_bow_recall = recall_score(labels_test,bow_predict)
naive_bow_f1 = f1_score(labels_test,bow_predict)

print(f"Precision: {naive_bow_precision} , Recall: {naive_bow_recall} , F1 score: {naive_bow_f1} ")

naive = MultinomialNB()
naive.fit(tfidf_feat_ss, labels_train)
tfidf_predict = naive.predict(tfidf_test_ss)

#evaluate tf idf
naive_tfidf_precision = precision_score(labels_test,tfidf_predict)
naive_tfidf_recall = recall_score(labels_test,tfidf_predict)
naive_tfidf_f1 = f1_score(labels_test,tfidf_predict)

print(f"Precision: {naive_tfidf_precision}, Recall: {naive_tfidf_recall} , F1 score: {naive_tfidf_f1} ")