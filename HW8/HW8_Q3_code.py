
# coding: utf-8

# In[2]:
import ast

import numpy as np
import copy

# In[23]:

def get_all_sequences(m, n):
    i = 1
    S = []
    for j in range(n):
        S.append([j])
    while i < m:
        S1 = []
        for s in S:
            for j in range(n):
                s1 = copy.deepcopy(s)
                s1.append(j)
                S1.append(s1)
        S.extend(S1)
        i = i + 1
    S = [item for item in S if len(item) == m]
    return S


class markovmodel:
    #transmat: None
    def __init__(self, transmat = None, startprob = None):
        self.transmat = transmat
        self.startprob = startprob
    # It assumes the state number starts from 0
    def fit(self, X):
        ns = max([max(items) for items in X]) + 1
        self.transmat  = np.zeros([ns, ns])
        self.startprob = np.zeros([ns])
        for items in X:
            n = len(items)
            self.startprob[items[0]] += 1
            for i in range(n-1):
                self.transmat[items[i], items[i+1]] += 1
        self.startprob = self.startprob / sum(self.startprob)
        n = self.transmat.shape[0]
        d = np.sum(self.transmat, axis=1)
        for i in range(n):
            if d[i] == 0:
                self.transmat[i,:] = 1.0 / n
        d[d == 0] = 1
        self.transmat = self.transmat * np.transpose(np.outer(np.ones([ns,1]), 1./d))

#    def predict_most_probable_sequene(self, ):


    def predict(self, obs, steps):
        n = len(obs)
        if len(obs) > 0:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = obs[-1]
                for i in comb:
                    prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            print max_prob,max_seq
            return max_seq
        else:
            combs = get_all_sequences(steps, len(self.startprob))
            max_seq = []
            max_prob = -1
            for comb in combs:
                prob = 1.0
                prev = -1
                for i in comb:
                    if prev == -1:
                        prob = prob * self.startprob[i]
                    else:
                        prob = prob * self.transmat[prev, i]
                    prev = i
                if prob > max_prob:
                    max_seq = comb
                    max_prob = prob
            return max_seq


# In[1]:

label = {0: "Albany", 1: "New York City", 2: "Washington D.C.", 3: "Seattle", 4: "Philadelphia", 5: "Boston"}
file_list = []
while True:
    file = open('HW9_Q3_training.txt')

    for line in file:
        x= line.replace("New York City", "1")
        y = x.replace("Albany", "0")
        z = y.replace("Washington D.C.", "2")
        w = z.replace("Seattle", "3")
        v = w.replace("Philapedia", "4")
        b = v.replace("Boston", "5")
        n = b.replace("'", '').replace('"', '')
        m = n.replace('\n', '')
        file_list.append(ast.literal_eval(m))
    break
    #print file_list
file_list1 = []
    #print file_list1


# train a markov model
mm = markovmodel()
mm.fit(file_list)


# predict the next 5 states given the current sequence 1,2,2
while True:
    file = open('HW9_Q3_testing.txt')

    for line in file:
        x= line.replace("New York City", "1")
        y = x.replace("Albany", "0")
        z = y.replace("Washington D.C.", "2")
        w = z.replace("Seattle", "3")
        v = w.replace("Philapedia", "4")
        b = v.replace("Boston", "5")
        n = b.replace("'", '').replace('"', '')
        m = n.replace('\n', '')
        l = ast.literal_eval(m)
        pred = mm.predict(l, 5)
        predictions = str([label[s] for s in pred])
        file1 = open('HW8_Q3_predictions.txt','a')
        file1.write(predictions)
        file1.write('\n')
    break




