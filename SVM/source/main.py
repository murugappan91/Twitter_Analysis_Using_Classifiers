__author__ = 'Muru'

from apis import nbclassifier, preprocess


if __name__ == '__main__':

    pre_obj = preprocess.preprocess()
    nbc_obj = nbclassifier.nbclassifier()
    print " Classifier name : SVM "
    #Set file path of training and test file
    train_file_path = '../data/training-Obama-Romney-tweets.xlsx'
    test_file_path = '../data/Project2_Testing.xlsx'


    #Set the training file sheet and test file sheet for candidate 1
#File 1
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


