import pandas as pd
from langdetect import detect #pip install langdetect
from textblob import TextBlob #pip install textblob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 

#function to detect language using langdetect
def detect_language(tweet):
    try:
        return detect(tweet)
    except:
        return 'Unknown'

def analyze_sentiment_english(tweet):
    #Turn tweet into textblob
    testimonial = TextBlob(tweet)
    #Get the polarity score of tweet
    score = testimonial.sentiment.polarity

    #Based on score return if its positive, negative or neutral
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    else:
        return "neutral"
    
def analyze_sentiment_other(tweet):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(tweet)
    compound_score = score['compound']
    if compound_score >= 0.05:
        return "positive"
    if compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"
    
def analyse_tweets(tweets):
    for index, row in tweets.iterrows():
        if row['Language'] == 'en':
            score = analyze_sentiment_english(str(row['Tweet']))
        else:
            score = analyze_sentiment_other(str(row['Tweet']))
    
    tweets.loc[index, 'Sentiment'] = score

    return tweets

def main():
    #Use for first time use: nltk.download('vader_lexicon')
    tweets = pd.read_excel("Week4/tweets.xlsx")
    #Add language column to the dataframe
    tweets['Language'] = tweets['Tweet'].apply(detect_language)
    #Add sentiment to tweet
    tweets = analyse_tweets(tweets)
    tweets = tweets[['Tweet', 'Language', 'Sentiment']]
    print(tweets)

main()