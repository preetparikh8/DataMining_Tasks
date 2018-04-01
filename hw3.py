import twitter, sys, json

reload(sys)
sys.setdefaultencoding("utf-8")

myApi = twitter.Api(consumer_key='2cLzaxIlSWqBVbaRDXMU9xtWq', \
                   consumer_secret='DTGsPq93MLE5x1sRSlWXQ8dEmS0qdCuzWNbyNTSOtSRjfTHJcP', \
                   access_token_key='141564321-jCZlz8Ceh0Rr1mQjmBHbXgOLirG0c0Qi9YeoesEb', \
                   access_token_secret='hQog9J12vXN4tOH2a88Z5HR1FELdIZtwz2rYzRnHRgcVu')


def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet['id']
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
        print 'Tweet Text: ', tweet['text']
    except:
        pass


def rest_query_ex3():
    query = 'gun OR bomb OR burglary OR theft OR crime'
    geo = [40.7128, -74.0060, "10mi"]  # City of New York
    MAX_ID = None
   # for it in range(1):  # Retrieve up to 200 tweets
    tweets = myApi.GetSearch(query, geocode=geo, count=100, max_id=MAX_ID, result_type='recent')
    for raw_tweet in tweets:
        tweet = json.loads(str(raw_tweet))
        print_info(tweet)
        data = {"created_at": tweet['created_at'], "screen_name": tweet['user'], "text": tweet['text']}
        data1 = {"text": tweet['text']}
        with open("crimenyc.txt", 'a+') as files:
            files.write(json.dumps(str(data)))
            files.write("\n")
        with open("crimenyctweets.txt", 'a+') as files:
            files.write(json.dumps(str(data1)))
            files.write("\n")
        for i in range(5):
            uid = str(tweets[i].user.id)
            timeline=myApi.GetUserTimeline(uid)
            for r in timeline:
                with open("timeline.txt", 'a+') as time:
                    time.write(r.text)
                    time.write("\n")
                    time.write("\n")



def main():
    rest_query_ex3()
    pass


if __name__ == '__main__':
    main()


