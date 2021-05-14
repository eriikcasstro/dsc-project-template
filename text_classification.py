## Natural Language processing libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk import word_tokenize, FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
## Machine Learning Libraries
from sklearn.metrics import roc_curve, auc, confusion_matrix, accuracy_score, f1_score, \
precision_score, recall_score, roc_auc_score, classification_report, plot_confusion_matrix, \
precision_score, accuracy_score, f1_score
from sklearn.datasets import fetch_20newsgroups
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV,train_test_split,cross_val_score
random_state = 0
import time
import pandas as pd
import matplotlib.pyplot as plt



nltk.download('punkt')
lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'[a-zA-Z0-9]+')
tfidf = TfidfVectorizer()



def clean_pics(df, words_list):
    for  index, caption in enumerate(df['Caption']):
        for word in words_list:
            if word in caption:
                df.drop(index, inplace = True)
                df.reset_index(drop = True, inplace = True)
    return df


def del_mentions(df):
    for index,num_of_hashtags in enumerate(df['num_of_mentions']):
        if num_of_hashtags > 1:
            df.drop(index, inplace = True)
    return df

def get_stopwords():
    stopwords_list = stopwords.words('english')
    stopwords_list += list(string.punctuation)
    return stopwords_list

def tokenize_all_captions(df):
    tokenized_list = []
    for i, caption in enumerate(df['Caption']):
        tokenized_caption = tokenizer.tokenize(caption)
        tokenized_list.extend(tokenized_caption)
    return tokenized_list

def filter_list(tokenized_list, stopwords_list):
    filtered_captions=[]
    for w in tokenized_list:
        if w.lower() not in stopwords_list:
            filtered_captions.append(w.lower())
    return filtered_captions

def lemmatize_caption(list):
    # creating a list with all lemmatized outputs
    lemmatized_output = []

    for listy in list:
        lemmed = ' '.join([lemmatizer.lemmatize(w) for w in listy])
        lemmatized_output.append(lemmed)
    return lemmatized_output

def process_caption(caption):
    tokenized_caption = tokenizer.tokenize(caption)
    return tokenized_caption


def vectorized_captions(text_list,df_captions):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(text_list)
    vectorized_captions = []
    for i, caption in enumerate(df_captions['Caption']):
        v = vectorizer.transform([caption])
        vectorized_captions.append(v)

    df_vect_captions = pd.DataFrame({'vectorized_captions': vectorized_captions})
    return df_vect_captions



def create_vectorized_captions(caption):
    tokenized_caption = process_caption(caption)
    tfidf_lem = tfidf.fit_transform(tokenized_caption)
    return tfidf_lem





### Machine Learning


# Define function to batch classify

def batch_clf(X_train, y_train, X_test, y_test, clf_dict):
    '''
    Fits a dictionary of classifiers, makes predictions and returns metrics

    Args:
        X_train: {array-like, sparse matrix} of shape (n_samples, n_features) train input values
        y_train: array-like of shape (n_samples,) train target values
        X_test: {array-like, sparse matrix} of shape (m_samples, m_features) test input values
        y_test: array-like of shape (m_samples,) test target values
        clf_dict: dictionary with key name of classifier and value classifier instance
    Returns:
        Results dataframe
    '''
    # Create empty DataFrame to store results
    times = []
    train_acc_scores = []
    test_acc_scores = []
    train_f1_scores = []
    test_f1_scores = []
    train_precision_scores = []
    test_precision_scores = []
    train_recall_scores = []
    test_recall_scores = []
    train_roc_data = []
    test_roc_data = []
    test_profit_scores = []

    # Loop through dictionary items
    for key, clf in clf_dict.items():
        start_time =time.time()

        # Fit classifier
        clf_fitted = clf.fit(X_train,y_train)

        # Get Predictions
        train_preds = clf_fitted.predict(X_train)
        test_preds = clf_fitted.predict(X_test)


        #Get F1 Scores
        train_f1 = f1_score(y_train, train_preds)
        train_f1_scores.append(round(train_f1,2))
        test_f1 = f1_score(y_test, test_preds)
        test_f1_scores.append(round(test_f1,2))


        # Get Precision Scores
        train_precision = precision_score(y_train, train_preds)
        train_precision_scores.append(round(train_precision,2))
        test_precision = precision_score(y_test, test_preds)
        test_precision_scores.append(round(test_precision,2))


        # Get Recall Scores
        train_recall = recall_score(y_train, train_preds)
        train_recall_scores.append(round(train_recall,2))
        test_recall = recall_score(y_test, test_preds)
        test_recall_scores.append(round(test_recall,2))



        #Get accuracy scores
        train_acc = accuracy_score(y_train, train_preds)
        train_acc_scores.append(round(train_acc,2))
        test_acc = accuracy_score(y_test, test_preds)
        test_acc_scores.append(round(test_acc,2))

        # Get Probability Predictions
        train_hat = clf_fitted.predict_proba(X_train)
        train_proba = train_hat[:,1]
        fpr_train, tpr_train, thresholds_train = roc_curve(y_train, train_proba)
        train_roc_data.append([fpr_train, tpr_train, thresholds_train])

        test_hat = clf_fitted.predict_proba(X_test)
        test_proba = test_hat[:,1]
        fpr_test, tpr_test, thresholds_test = roc_curve(y_test, test_proba)
        test_roc_data.append([fpr_test, tpr_test, thresholds_test])

        end_time = time.time()
        time_elapsed = end_time - start_time
        times.append(round(time_elapsed,2))


    # Create results dataframe
    results = pd.DataFrame({'Model': list(clf_dict.keys()),
                            'Time': times,
                            'Train Accuracy': train_acc_scores,
                            'Test Accuracy': test_acc_scores,
                            'Train F1': train_f1_scores,
                            'Test F1': test_f1_scores,
                            'Train Precision' : train_precision_scores,
                            'Test Precision' : test_precision_scores,
                            'Train Recall': train_recall_scores,
                            'Test Recall': test_recall_scores
                           })
    #plot_conf_matrix(clf,X_train, y_train,X_test, y_test,class_names)
    # Plot side by side ROC curve
    fig, axes = plt.subplots(1,2, figsize = (13,6))

    for i in range(len(train_roc_data)):
        axes[0].plot(train_roc_data[i][0], train_roc_data[i][1], lw=4, \
                 label= f'{list(clf_dict.keys())[i]}')

    for i in range(len(test_roc_data)):
        axes[1].plot(test_roc_data[i][0], test_roc_data[i][1], lw=4, \
                 label= f'{list(clf_dict.keys())[i]}')

    for ax in axes:
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.legend(loc='lower right')
    axes[0].set_title('Receiver operating characteristic (ROC) Curve \n Training Set')
    axes[1].set_title('Receiver operating characteristic (ROC) Curve \n Test Set')
    plt.show()

    return results
