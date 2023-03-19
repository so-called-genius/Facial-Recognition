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
    n0 = {}
    n1 = {}

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


        for i in range(70):
            l = f.readline()
            for j in range(60):
                if l[j] == '#':
                    if label == '0':
                        if 70 * i + j in n0:
                            n0[70 * i + j] = n0[70 * i + j] + 1
                        else:
                            n0[70 * i + j] = 1
                    elif label == '1':
                        if 70 * i + j in n1:
                            n1[70 * i + j] = n1[70 * i + j] + 1
                        else:
                            n1[70 * i + j] = 1

    #Test the data
    correct = 0
    total = 0
    k = 60
    for li in f4:
        total = total + 1
        testlist = []

        #Read label into testlist
        for i in range(70):
            l = f3.readline()
            for j in range(60):
                if l[j] == '#':
                    testlist.append(70 * i + j)

        p0 = 1
        for i in range(70):
            for j in range(60):
                if 70 * i + j in testlist:
                    if 70 * i + j in n0:
                        p0 = p0 * (n0[70 * i + j] + k) / (numline[0] + k)
                    else:
                        p0 = p0 * k / (numline[0] + k)

        p1 = 1
        for i in range(70):
            for j in range(60):
                if 70 * i + j in testlist:
                    if 70 * i + j in n1:
                        p1 = p1 * (n1[70 * i + j] + k) / (numline[1] + k)
                    else:
                        p1 = p1 * k / (numline[1] + k)



        p0 = p0 * numline[0]
        p1 = p1 * numline[1]

        print(p0, p1)
        m = max(p0, p1)
        print(li[0], end='')
        if m == p0:
            if li[0] == "0":
                correct = correct + 1
            print(0)
        elif m == p1:
            if li[0] == "1":
                correct = correct + 1
            print(1)


    print(correct)
    print(total)
    print(correct / total)
    return(correct/total)



