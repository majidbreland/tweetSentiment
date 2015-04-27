from pattern.web import Twitter, plaintext
from pattern.web.locale import geocode

import indicoio

indicoio.config.api_key = ""

class tweetSentiment(object):

	def __init__(self, topic, tweetCount):
		self.topic = topic
		self.tweetCount = tweetCount

	def calculate(self):
		t = Twitter(language='EN')
		i = None
		sentimentArray = []

		for tweet in t.search(self.topic, start=i, count = self.tweetCount):
			sentimentArray.append(indicoio.sentiment(tweet.text))
			i = tweet.id

		return sentimentArray

	def average(self,sentimentArray):
		b = sentimentArray

		return sum(b)/len(b)
		 
def main():
	sentiment = tweetSentiment('facebook', 10)

	sArr = sentiment.calculate()

	print "Number of Tweets: " + str(len(sArr))
	print "Subject Sentiment: "  + str(sentiment.average(sArr))

if __name__ == "__main__":
	main()


