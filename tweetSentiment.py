from pattern.web import Twitter, plaintext
from pattern.web.locale import geocode

import csv
import indicoio


#enter your api key here
indicoio.config.api_key = ""


class tweetSentiment(object):


	def __init__(self, topic, tweetCount):
		self.topic = topic
		self.tweetCount = tweetCount
		self.t = Twitter(language='EN')
		self.i = None

	def fArray(self):
		'''full array including tweet and sentiment'''	
		fullArray = []

		for tweet in self.t.search(self.topic, start=self.i, count = self.tweetCount):
			fullArray.append([tweet.text,indicoio.sentiment(tweet.text)])
			self.i = tweet.id

		return fullArray

	def sArray(self):
		'''calculate sentiment '''
		sentimentArray = []

		for tweet in self.t.search(self.topic, start=self.i, count = self.tweetCount):
			sentimentArray.append(indicoio.sentiment(tweet.text))
			self.i = tweet.id

		return sentimentArray

	def average(self,numArray):
		'''average sentiment'''
		return sum(numArray)/len(numArray)

	def trending(self):
		'''trending sentiment'''

		trendArray = []

		for trend in Twitter().trends(cached=False):
			trendArray.append([trend,indicoio.sentiment(trend)])

		return trendArray


		 
def main():
	sentiment = tweetSentiment('wall street', 10)

	#array of tweets and sentiment
	fArr = sentiment.fArray()
	#array of only tweet sentiment
	sArr = sentiment.sArray()
	#array of trending and sentiment
	tArr = sentiment.trending()

	#print "Number of Tweets: " + str(len(sArr))
	#print "Subject Sentiment: "  + str(sentiment.average(tArr))

if __name__ == "__main__":
	main()


