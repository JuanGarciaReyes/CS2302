import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='x_IAA3B1ypV01Q',
                     client_secret='vt_BW5GESY4n0yGCuUoaxkoKWug',
                     user_agent='champagnefruit'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

def process_comments(neg,pos,neu,comments):
    for i in comments:
        positive = get_text_positive_proba(i.body)
        neutral = get_text_neutral_proba(i.body)
        negative = get_text_negative_proba(i.body)
        if (positive > neutral and positive > negative):
            pos.append(i.body)
        elif(neutral >positive and neutral > negative):
            neu.append(i.body)
        elif(negative >positive and negative > neutral):
            neg.append(i.body)
        process_comments(neg,pos,neu,i.replies)
         

 
def main():
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    print(comments[0].body)
    print(comments[0].replies[0].body)

    neg = [] #et_text_negative_proba(comments[0].replies[0].body)
    pos = [] #get_text_positive_proba(comments[0].replies[0].body)
    neu = [] #get_text_neutral_proba(comments[0].replies[0].body)
    process_comments(neg,pos,neu,comments)
    print(neg)
    print(pos)
    print(neu)
main()
