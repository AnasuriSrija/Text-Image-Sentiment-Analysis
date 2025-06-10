from textblob import TextBlob
import re

def sentiment(s):

    # s = "My experience so far has been fantastic"
    reg = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", s).split())
        # set sentiment
    analysis = TextBlob(reg)
    #print(analysis.sentiment.polarity)

    if analysis.sentiment.polarity > 0:
        print('positive')
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        print('neutral')
        return 'neutral'
    else:
        print('negative')
        return 'negative'

if __name__ == "__main__":
    sentiment("This sucks")
