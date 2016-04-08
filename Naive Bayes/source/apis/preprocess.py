__author__ = 'Muru'

import re
from nltk.corpus import stopwords
from stemming.porter2 import stem
from nltk.corpus import wordnet
import fileprocess

class preprocess():

    global abbrfile
    #Set the path to abbreviation file
    abbrfile = 'G:/CS583/project2/DmTest/data/abbr.txt'

    #start process_tweet
    def processTweet(self,tweet):

        fobj2 = fileprocess.fileprocess()
        abbr_dict = fobj2.abbr_extract(abbrfile)

        #Replace www.* or https?://* with space
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)

        #Convert username from @username to AT_USER
        tweet = re.sub('@[^\s]+','',tweet)

        #Replacing abbreviations and emoticons with respective words
        tweet = self.replace_abbr(tweet,abbr_dict)

        #Remove punctuations
        punct_remove = re.compile(r"[\"'\[\],.:;()\-&!]")
        tweet = re.sub(punct_remove, '', tweet)


        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)

        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)


        #Convert camel-case words to space delimited words
        tweet = self.camelcase(tweet)

        #Remove non-letters
        tweet = re.sub("[^a-zA-Z]", " ", tweet)

        #Convert to lower case
        tweet = tweet.lower()

        #Trim the tweet
        tweet = tweet.strip('\'"')

        #Removing <e> and <a> tags
        tweet = re.sub(r'(<e>|</e>|<a>|</a>|\n)', '', tweet)

        #Removing repeating letters in word
        tweet = self.replaceRepeatingLetter(tweet)

        #Removing stop words
        words = tweet.split()
        stops = set(stopwords.words("english"))
        meaningful_words = [w for w in words if w not in stops]
        meaningful_words_edit = []
        for word in meaningful_words:
            #Check if word is an English word and do Stemming
            word = self.extract_englishword(word)
            if word != '':
                meaningful_words_edit.append(word)
            else:
                continue
        tweet = (" ".join(meaningful_words_edit))
        return tweet
        #end

    #Function to remove words that are not caught in previous steps
    def remove_smallwords(self,word):
        if(len(word)>2 and (word not in ('no','ok'))):
            return word
        else:
            return ''

    #Function to do Stemming for English words
    def extract_englishword(self,word):
        #Removing words which are less than three letters except 'no', 'ok'
        word = self.remove_smallwords(word)
        if word !='':
            #Check if it is an English word else remove that word from tweet
            if not wordnet.synsets(word):
                return ''
            else:
                #Perform Stemming
                word = stem(word)
                return word
        else:
            return ''

    #Function to replace abbreviation with respective word
    def replace_abbr(self,s,abbr_dict):
        for word in s:
            if word.lower() in abbr_dict.keys():
                s = [abbr_dict[word.lower()] if word.lower() in abbr_dict.keys() else word for word in s]
        return s

    #Function to separate camel case words with space
    def camelcase(self,word):
        return re.sub("([a-z])([A-Z])","\g<1> \g<2>",word)

    def replaceRepeatingLetter(self,s):
        #Check for more than two repetitions of a character
        # and replace with the repeating letters with that character itself
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)
