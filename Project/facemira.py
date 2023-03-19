import os
import math
import pprint


def ma(z):
    a = trainthedata(z)
    return(a)


def trainthedata(z):
    data = []
    f = open("facedatatrain")
    f2 = open("facedatatrainlabels")
    f3 = open("facedatatest")
    f4 = open("facedatatestlabels")
    numline = [0, 0]
    w0 = []
    w1 = []

    
    for i in range(4201):
        w0.append(0)
        w1.append(0)
        
    indexx = 0
    ind = 0
    for line in f2:
        if ind == len(z):
            indexx = indexx + 1
            break
        if indexx != z[ind]:
            indexx = indexx + 1
            for i in range(70):
                l = f.readline()
            continue
        ind = ind + 1
        indexx = indexx + 1

        label = line[0]
        if label == '0':
            numline[0] = numline[0] + 1
        elif label == '1':
            numline[1] = numline[1] + 1

        fe = []
        for i in range(70):
            l = f.readline()
            for j in range(60):
                if l[j] == '#':
                    fe.append(1)
                else:
                    fe.append(0)

        s0 = 0
        for i in range(4200):
            s0 = s0 + w0[i] * fe[i]
        s0=s0+w0[4200]
        s1 = 0
        for i in range(4200):
            s1 = s1 + w1[i] * fe[i]
        s1=s1+w1[4200]

        if label == '0':

            while s0<s1+1:
                    for i in range(4200):
                        w0[i] = w0[i] + 0.001*fe[i]
                    w0[4200]=w0[4200]+0.001
                    for i in range(4200):
                        w1[i] = w1[i] - 0.001*fe[i]
                    w1[4200]=w1[4200]-0.001
                    s0 = 0
                    for i in range(4200):
                        s0 = s0 + w0[i] * fe[i]
                    s0 = s0 + w0[4200]
                    s1 = 0
                    for i in range(4200):
                        s1 = s1 + w1[i] * fe[i]
                    s1 = s1 + w1[4200]

        elif label == '1':
            while s0+1 > s1:
                for i in range(4200):
                    w0[i] = w0[i] - 0.001 * fe[i]
                w0[4200] = w0[4200] - 0.001
                for i in range(4200):
                    w1[i] = w1[i] + 0.001 * fe[i]
                w1[4200] = w1[4200] + 0.001
                s0 = 0
                for i in range(4200):
                    s0 = s0 + w0[i] * fe[i]
                s0 = s0 + w0[4200]
                s1 = 0
                for i in range(4200):
                    s1 = s1 + w1[i] * fe[i]
                s1 = s1 + w1[4200]

    # Test the data
    correct = 0
    total = 0
    k = 1
    for li in f4:
        total=total+1
        fe = []

        # Read label into testlist
        for i in range(70):
            l = f3.readline()
            for j in range(60):
                if l[j] == '#':
                    fe.append(1)
                else:
                    fe.append(0)
        s0 = 0
        for i in range(4200):
            s0 = s0 + w0[i] * fe[i]
        s0=s0+w0[4200]
        s1 = 0
        for i in range(4200):
            s1 = s1 + w1[i] * fe[i]
        s1=s1+w1[4200]

        print(s0, s1)
        m = max(s0, s1)
        print(li[0], end=' ')
        if m == s0:
            if li[0] == "0":
                correct = correct + 1
            print(0)
        elif m == s1:
            if li[0] == "1":
                correct = correct + 1
            print(1)

    print(correct)
    print(total)
    print(correct / total)
    return(correct/total)


