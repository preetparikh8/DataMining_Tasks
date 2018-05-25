import pickle
import json
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')


with open("Model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)

id=[]
tweets=[]
for line in open('test_tweets.txt').readlines():
    tweet = json.loads(line)
    emb_id = tweet['embersId']
    test_tweets = tweet['text']
    id.append(emb_id)
    tweets.append(test_tweets)

vocab=dict()
with open('Vocab.txt') as f:
    vocab=eval(f.read())

X = []
for text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    X.append(x)
y = pickle_model.predict(X)

data={}
with open("predictions.txt", 'a+') as file:
    file.write("{")
    for line in range(len(tweets)):
        for line1 in id:
            if (y[line]==0):
                pred="false"
            else:
                pred="true"
        print id[line],pred
        data = {id[line], pred}
        file.write('"' + id[line] + '" :')
        file.write(pred)
        file.write(",")
        file.write("\n")
    file.write("}")

