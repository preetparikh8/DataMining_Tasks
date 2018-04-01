import json
import datetime
import os
from pattern.en import sentiment


def task1():
    print "hello world"

if __name__=='__main__':
    task1()

def task2():
    list=[1,2,3,4,5]
    print list

if __name__=='__main__':
    task2()

def task3():
    fo = open("task3.data", "r")
    for line in fo:
            list = line.split(" ")
    print "items1 = [%s]" % (','.join(list[0:5]))
    print "items2 = [%s]" % (','.join(list[5:10]))

if __name__=='__main__':
    task3()

def task4():
    data={'School':'Ualbany','address':'1400 Washington Avenue, Albany, NY 12222','phone':'(518)442-3300'}
    print "School :" , data['School']
    print "Address :", data['address']
    print "Phone :", data['phone']

if __name__=='__main__':
    task4()

def task5():
    data = {'School': 'Ualbany', 'address': '1400 Washington Avenue, Albany, NY 12222', 'phone': '(518)442-3300'}
    with open('task5.json', 'wb') as pp:
        json.dump(data, pp)
    json_data=open('task5.json').read()
    data1=json.loads(json_data)
    print "School :", data1['School']
    print "Address :", data1['address']
    print "Phone :", data1['phone']


if __name__=='__main__':
    task5()


def task6():
    data = {'School': 'Ualbany', 'address': '1400 Washington Avenue, Albany, NY 12222', 'phone': '(518)442-3300', 'list': '[1,2,3,4,5]'}
    with open('task6.data', 'wb') as pp:
        json.dump(data, pp)
    json_data = open('task6.data').read()
    data1 = json.loads(json_data)
    print "School :", data1['School']
    print "Address :", data1['address']
    print "Phone :", data1['phone']
    print "List :", data1['list']

if __name__=='__main__':
    task6()

def task7():
    tweet = []
    tweets_file = open("CrimeReport.txt", "r").readlines()
    for line in tweets_file:
            tweet = json.loads(line)
            print tweet.keys()
            print "ID :", tweet['id']


if __name__=='__main__':
    task7()

def task8():
    tweets = []
    tweets_file = open("CrimeReport.txt", "r").readlines()
    for line in tweets_file:
        tweet = json.loads(line)
        tweets.append(tweet)
        sorted_tweets=sorted(tweets,key=lambda item:datetime.datetime.strptime(item['created_at'], '%a %b %d %H:%M:%S +0000 %Y' ))

    for tweet in sorted_tweets[-10:]:
        f = open('task8.data', 'a')
        f.write(json.dumps(tweet) + '\n ')
    f.close()

if __name__=='__main__':
    task8()


def task9():
    tweets = []
    tweets_file = open("CrimeReport.txt", "r").readlines()
    for line in tweets_file:
        tweet = json.loads(line)
        tweets.append(tweet)
        string_time = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        hours = string_time.strftime("%b %d %Y %H")
        output_path = 'C:/Users/PreetP/PycharmProjects/Homework/task9-output'
        file_name=os.path.join(output_path, hours + ".txt")
        f=open(file_name,'a')
        f.write(json.dumps(tweet) + '\n ')
    f.close()


if __name__=='__main__':
    task9()


def task10():
    tweets = []
    tweets_file = open("CrimeReport.txt", "r").readlines()
    print "Sentiment of each tweet text:"
    for line in tweets_file:
        tweet = json.loads(line)
        #tweets.append(tweet)
        tweets= tweet['text']
        score=sentiment(tweets).assessments
        print format(score)
        score1=sentiment(tweets)
        print format(score1)


if __name__=='__main__':
    task10()



