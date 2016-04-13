__author__ = 'Muru'
#
# Main function which process file data from excel sheet, preprocess and cleanse data
# perform requested classification based on NLTK libraries and Sci-Kit libraries avaiable in Python
#
from apis import fileprocess, nbclassifier, preprocess
import nltk.classify
from sklearn import cross_validation
import collections
import random

if __name__ == '__main__':

    fp_obj = fileprocess.fileprocess()
    pre_obj = preprocess.preprocess()
    nbc_obj = nbclassifier.nbclassifier()

    print " Classifier name: Naive Bayes Classifier "
    #Set file path of training and test file
    train_file_path = '../data/training-Obama-Romney-tweets.xlsx'
    test_file_path = '../data/Project2_Testing.xlsx'

    #Set the training file sheet and test file sheet for candidate 1
    sheet_train = 'Romney'
    sheet_test = 'romney-test'

    candidate_train = sheet_train
    candidate_test = sheet_test

    print "Training candidate - ", candidate_train, " : ","Testing candidate - ",candidate_test

    #Classify tweets and print result
    nbc_obj.classify_tweets(train_file_path,candidate_train,test_file_path,candidate_test)

    #Set the training file sheet and test file sheet for candidate 1
    sheet_train = 'Obama'
    sheet_test = 'obama-test'
    candidate_train = sheet_train
    candidate_test = sheet_test

    print "Training candidate - ", candidate_train, " : ","Testing candidate - ",candidate_test

    #Classify tweets and print result
    nbc_obj.classify_tweets(train_file_path,candidate_train,test_file_path,candidate_test)
