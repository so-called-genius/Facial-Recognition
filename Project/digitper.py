import os
import math
import pprint
import random
import numpy as np


class Perceptron:
    def __init__(self):
        # labels is vector of 1 * n 
        self.labels = []
        # data is vector of n * m ：n is number of data，m is number of traits
        self.data = []
        # testlabels is vector of 1 * N
        self.testlabels = []
        # testdata is vector of N * M：N is number of test data，M is number of traits
        self.testdata = []
        # initializing data
        self.initdata()
        # initializing learning rate, 1 on webpage
        self.l_rate = 0.01
        self.part = 0.1
        self.n, self.m = self.data.shape

        self.N, self.M = self.testdata.shape
        self.totClass = 10
        # w is matrix of m * totClass ：m is number of traits，lastly print out totClass number of prediction mark
        # since sample size of labels is 10
        # so totClass is 10
        self.w = np.zeros((self.m, self.totClass))
        #self.b = np.zeros(self.totClass)
        self.correct = 0
        self.total = self.N
        # self.numSimples = x.shape[0]
        # self.numFeatures = x.shape[1]

    def initdata(self):
        f1 = open("trainingimages")
        f2 = open("traininglabels")
        f3 = open("testimages")
        f4 = open("testlabels")
        labels = []
        Data = []
        for line in f2:
            labels.append(line[0])

        cnt = 0
        tmp = []
        for line in f1:
            cnt = cnt + 1
            for i in line:
                if i == ' ':
                    tmp.append(0)
                else:
                    tmp.append(1)
            if cnt == 28:
                Data.append(tmp)
                cnt = 0
                tmp = []
        testlabels = []
        testData = []
        for line in f4:
            testlabels.append(line[0])
        cnt = 0
        tmp = []
        for line in f3:
            cnt = cnt + 1
            for i in line:
                if i == ' ':
                    tmp.append(0)
                else:
                    tmp.append(1)

            if cnt == 28:
                testData.append(np.array(tmp))
                tmp = []
                cnt = 0
        self.labels = np.array(labels)
        self.data = np.array(Data)
        self.testlabels = np.array(testlabels)
        self.testdata = np.array(testData)
        return

    def train(self, part=0.1):
        self.part = part
        self.w = np.zeros((self.m, self.totClass))
        listnum = [i for i in range(0, self.n)]
        # print(listnum)
        random.shuffle(listnum)
        # print(listnum)
        for i in range(int(self.n * self.part)):
            pos = listnum[i]
            score = np.dot(self.data[pos], self.w)
            idx = np.argmax(score)
                # current training gets first class，but real value is others，which need update
                # acoording to function's calculation
                # w to first class's weight is higher
                # w to other clas's weigh is lower
            ttmp = [[-1]] * self.totClass
            if not idx == int(self.labels[pos]):
                # update
                ttmp[int(self.labels[pos])] = [1]
            add = ttmp * self.data[pos].transpose() * self.l_rate
            self.w = self.w + add.transpose()
        return

    def test(self):
        self.correct = 0
        score = np.dot(self.testdata, self.w)
        idx = np.argmax(score, axis=1)
        for i in range(self.N):
            if idx[i] == int(self.testlabels[i]):
                self.correct = self.correct + 1
        return self.correct/self.total


if __name__ == '__main__':
    p = Perceptron()
    p.train(0.4)
    print(p.test())

