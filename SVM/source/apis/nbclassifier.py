__author__ = 'Muru'
import fileprocess
import nltk
import nltk.classify
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import collections
from sklearn.feature_extraction.text import TfidfTransformer

class nbclassifier():

    def classify_tweets(self,file_train,candidate_train,file_test,candidate_test):
        fp_obj = fileprocess.fileprocess()
        tweets_train,sentiments_train = fp_obj.readfile(file_train,candidate_train,'train')


        tweets_test, sentiments_test = fp_obj.readfile(file_test,candidate_test,'test')

        classifierSVM = svm.SVC(kernel='linear')
        v = CountVectorizer()
        train_vec = v.fit_transform(tweets_train)

        #$$$$ Implementing TF-IDF
        tf_transformer = TfidfTransformer(use_idf=False).fit(train_vec)
        train_tf = tf_transformer.transform(train_vec)

        classifierSVM.fit(train_tf,sentiments_train)
        test_vec = v.transform(tweets_test)
        test_tfidf = tf_transformer.transform(test_vec)
        op =  classifierSVM.predict(test_tfidf)
        #$$$$$ Changes end

        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)
        observed = classifierSVM.predict(test_vec)
        print ""
        for i in range(len(sentiments_test)):
            refsets[sentiments_test[i]].add(i)
            testsets[observed[i]].add(i)


        # print "Positive: "
        pp = nltk.metrics.precision(refsets[1.0], testsets[1.0])
        # print ' pos precision:', pp

        pr = nltk.metrics.recall(refsets[1.0], testsets[1.0])
        # print ' pos recall:', pr

        fp = nltk.metrics.f_measure(refsets[1.0], testsets[1.0])
        # print ' pos F-measure:', fp

        # print "Negative : "
        np = nltk.metrics.precision(refsets[-1.0], testsets[-1.0])
        # print ' neg precision:', np
        nr = nltk.metrics.recall(refsets[-1.0], testsets[-1.0])
        # print ' neg recall:', nr
        fn = nltk.metrics.f_measure(refsets[-1.0], testsets[-1.0])
        # print ' neg F-measure:', fn

        # print "Neutral: "
        nup = nltk.metrics.precision(refsets[0.0], testsets[0.0])
        # print ' neu precision:', nup
        nur = nltk.metrics.recall(refsets[0.0], testsets[0.0])
        # print ' neu recall:', nur
        fnu = nltk.metrics.f_measure(refsets[0.0], testsets[0.0])
        # print ' neu F-measure:',fnu

        temp = accuracy_score(op,sentiments_test)
        print 'Accuracy: %.2f' % (temp*100.0),'%'

        print '#########'
        print 'Positive Precision: %.2f' % (pp*100.0),"%"
        print 'Positive Recall: %.2f' % (pr*100.0),"%"
        print 'Positive Fscore: %.2f' % (fp*100.0),"%"
        print '#########'
        print 'Negative Precision: %.2f' % (np*100.0),"%"
        print 'Negative Recall: %.2f' % (nr*100.0),"%"
        print 'Negative Fscore: %.2f' % (fn*100.0),"%"
        print ""
        print ""
        # print '#########'
        # print 'Neutral Precision: %.2f' % (nup*100.0),"%"
        # print 'Neutral Recall: %.2f' % (nur*100.0),"%"
        # print 'Neutral Fscore: %.2f' % (fnu*100.0),"%"