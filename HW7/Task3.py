__author__ = 'fengchen'


from sklearn.svm import SVC
import copy
print 'Captain America, Non-Stop, 300, Thor, The Wolf of Wall Street, Frozen'
def main():
    data = [[1,1,0,0,1,0],
            [0,1,1,0,0,0],
            [1,0,0,0,0,1],
            [1,1,0,1,0,0],
            [1,0,0,0,1,1],
            [0,1,1,0,1,0]]
    pred = copy.deepcopy(data)
    n_users = len(pred)
    n_movies = len(pred[0])
    for u in range(n_users):
        for m in range(n_movies):
            if pred[u][m] == 0: # If it equals 1, this movie will not be recommended since the user has watched the movie already.
                Y = []
                X = []
                for i in range(u) + range(u+1, n_users):
                    X.append(data[i][:m] + data[i][m+1:])
                    Y.append(data[i][m])
                sv = SVC(probability=True)
                sv.fit(X,Y)
                val = sv.predict_proba([data[u][:m] + data[u][m+1:]])
                pred[u][m] = round(val[0][1],2)
    for vals in pred:
        print vals




if __name__ == '__main__':
    main()