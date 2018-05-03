
# coding: utf-8

# In[2]:

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
            #print max_prob,max_seq
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

label = {0: "New York City", 1: "Boston", 2: "Washington D.C.", 3: "Albany", 4: "Philadelphia"}
y = [[3, 2, 3, 1, 3],
     [3, 0, 1, 0, 3],
     [1, 3, 4, 1, 0],
     [3, 2, 1, 3, 2],
     [3, 4, 3, 2, 0],
     [3, 0, 3, 4, 1],
     [1, 3, 0, 4, 3],
     [1, 3, 2, 4, 1],
     [0, 4, 1, 4, 2],
     [4, 0, 4, 0, 4]]

# train a markov model
mm = markovmodel()
mm.fit(y)

print "Largest probability of 5 cities:"
# predict a sequence 5 states without a current sequence
pred = mm.predict([], 5)
print [label[s] for s in pred]


# predict the next 5 states given the current sequence 1,2,2
print "Sequence if the current city is Washington D.C:"
pred = mm.predict([2], 5)
print [label[s] for s in pred]
