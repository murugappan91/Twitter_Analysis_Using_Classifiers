__author__ = 'Muru'

import fileprocess
import nltk.classify
from sklearn import cross_validation
import collections
import random

class nbclassifier():

    def classify_tweets(self,file_train,candidate_train,file_test,candidate_test):
        fp_obj = fileprocess.fileprocess()
        tweets_train = fp_obj.readfile(file_train,candidate_train,'train')
        tweets_test = fp_obj.readfile(file_test,candidate_test,'test')


        training_set = nltk.classify.apply_features(self.extract_features,tweets_train)

        test_set = nltk.classify.apply_features(self.extract_features,tweets_test)


        NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)

        for i, (feats, label) in enumerate(test_set):
            refsets[label].add(i)
            observed = NBClassifier.classify(feats)
            testsets[observed].add(i)

        pp = nltk.metrics.precision(refsets[1.0], testsets[1.0])
        pr = nltk.metrics.recall(refsets[1.0], testsets[1.0])
        fp = nltk.metrics.f_measure(refsets[1.0], testsets[1.0])

        np = nltk.metrics.precision(refsets[-1.0], testsets[-1.0])
        nr = nltk.metrics.recall(refsets[-1.0], testsets[-1.0])
        fn = nltk.metrics.f_measure(refsets[-1.0], testsets[-1.0])

        # print "Neutral: "
        # nup = nltk.metrics.precision(refsets[0.0], testsets[0.0])

        # print 'Neutral Precision:', nup
        # nur = nltk.metrics.recall(refsets[0.0], testsets[0.0])
        #
        # print 'Neutral Recall:', nur
        # fnur = nltk.metrics.f_measure(refsets[0.0], testsets[0.0])
        #
        # print 'Neutral F-measure:', fnur

        temp = nltk.classify.accuracy(NBClassifier,test_set)
        print 'Accuracy: %.2f' % (temp*100.0),'%'

        print '#########'
        print 'Positive Precision: %.2f' % (pp*100.0),"%"
        print 'Positive Recall: %.2f' % (pr*100.0),"%"
        print 'Positive Fscore: %.2f' % (fp*100.0),"%"
        print '#########'
        print 'Negative Precision: %.2f' % (np*100.0),"%"
        print 'Negative Recall: %.2f' % (nr*100.0),"%"
        print 'Negative Fscore: %.2f' % (fn*100.0),"%"


    def extract_features(self,tweet):
        return dict([(word, True) for word in tweet])
