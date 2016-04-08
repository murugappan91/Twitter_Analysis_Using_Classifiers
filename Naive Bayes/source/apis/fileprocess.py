__author__ = 'Muru'

import xlrd
import preprocess
import random

class fileprocess():

    #Function to read input file
    def readfile(self,filename,candidate,file_toprocess):
        tweets = []
        prepro_obj = preprocess.preprocess()
        tweets_sentis = self.randomize_tweet(filename,candidate,file_toprocess)
        for tweet_senti in tweets_sentis:
                tweet = tweet_senti[0]
                sentiment = tweet_senti[1]
                processed_tweet = prepro_obj.processTweet(tweet)
                processed_tweet = str(processed_tweet).split()

                if processed_tweet != '' and sentiment != '':
                    tweets.append((processed_tweet,sentiment))

                else:
                    continue
        return tweets

    #Function to read tweets and shuffle them to avoid skewness in the data
    def randomize_tweet(self,filename,candidate,file_status):
        #print "reading tweets for ", file_status
        workbook = xlrd.open_workbook(filename, on_demand=True)
        worksheet = workbook.sheet_by_name(candidate)
        tweet_sent = []
        #Get no. of cells
        no_cells = worksheet.ncols - 1
        print "No. of cells in ", file_status," data :", no_cells
        no_rows = worksheet.nrows - 1

        if file_status == 'train':
            class_column = 4
            tweet_column = 3
        else:
            class_column = 6
            tweet_column = 3

        print "No of rows: ", no_rows
        cur_row = 0
        while cur_row <= no_rows:
            if cur_row == 0 or cur_row ==1:
                cur_row += 1
                continue
            elif worksheet.cell_value(cur_row, 4) in (0, 1, -1):
                tweet = worksheet.cell_value(cur_row, tweet_column)
                sentiment = worksheet.cell_value(cur_row, class_column)
                tweet_sent.append((tweet,sentiment))
                cur_row +=1
            else:
                #skipping mixed and NA class instances
                cur_row += 1
                continue

        if file_status == 'train' or 'test':
          #setting fixed shuffle
            random.seed(999)
            random.shuffle(tweet_sent)
        print "***Tweet read***"
        return tweet_sent

    #Function to extract abbreviation and its respective word from given input file
    def abbr_extract(self,filename):
        abbr_dict = dict()
        f = open(filename)
        lines = f.readlines()
        f.close()
        for i in lines:
            tmp = i.split('$')
            abbr_dict[tmp[0]] = tmp[1]

        return abbr_dict
