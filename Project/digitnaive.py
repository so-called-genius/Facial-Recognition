import os
import math
import pprint


def ma(z):
    a = trainthedata(z)
    return(a)


def trainthedata(z):
    data = []
    f = open("trainingimages")
    f2 = open("traininglabels")
    f3 = open("testimages")
    f4 = open("testlabels")
    numline = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n0 = {}
    n1 = {}
    n2 = {}
    n3 = {}
    n4 = {}
    n5 = {}
    n6 = {}
    n7 = {}
    n8 = {}
    n9 = {}
    indexx = 0
    ind = 0

    for line in f2:
        if ind == len(z):
            indexx = indexx + 1
            break
        if indexx != z[ind]:
            indexx = indexx + 1
            for i in range(28):
                l = f.readline()
            continue
        ind = ind + 1
        indexx = indexx + 1
        
        label = line[0]
        if label == '0':
            numline[0] = numline[0] + 1
        elif label == '1':
            numline[1] = numline[1] + 1
        elif label == '2':
            numline[2] = numline[2] + 1
        elif label == '3':
            numline[3] = numline[3] + 1
        elif label == '4':
            numline[4] = numline[4] + 1
        elif label == '5':
            numline[5] = numline[5] + 1
        elif label == '6':
            numline[6] = numline[6] + 1
        elif label == '7':
            numline[7] = numline[7] + 1
        elif label == '8':
            numline[8] = numline[8] + 1
        elif label == '9':
            numline[9] = numline[9] + 1

        for i in range(28):
            l = f.readline()
            for j in range(28):
                if l[j] == '#':
                    if label == '0':
                        if 28 * i + j in n0:
                            n0[28 * i + j] = n0[28 * i + j] + 1
                        else:
                            n0[28 * i + j] = 1
                    elif label == '1':
                        if 28 * i + j in n1:
                            n1[28 * i + j] = n1[28 * i + j] + 1
                        else:
                            n1[28 * i + j] = 1
                    elif label == '2':
                        if 28 * i + j in n2:
                            n2[28 * i + j] = n2[28 * i + j] + 1
                        else:
                            n2[28 * i + j] = 1
                    elif label == '3':
                        if 28 * i + j in n3:
                            n3[28 * i + j] = n3[28 * i + j] + 1
                        else:
                            n3[28 * i + j] = 1
                    elif label == '4':
                        if 28 * i + j in n4:
                            n4[28 * i + j] = n4[28 * i + j] + 1
                        else:
                            n4[28 * i + j] = 1
                    elif label == '5':
                        if 28 * i + j in n5:
                            n5[28 * i + j] = n5[28 * i + j] + 1
                        else:
                            n5[28 * i + j] = 1
                    elif label == '6':
                        if 28 * i + j in n6:
                            n6[28 * i + j] = n6[28 * i + j] + 1
                        else:
                            n6[28 * i + j] = 1
                    elif label == '7':
                        if 28 * i + j in n7:
                            n7[28 * i + j] = n7[28 * i + j] + 1
                        else:
                            n7[28 * i + j] = 1
                    elif label == '8':
                        if 28 * i + j in n8:
                            n8[28 * i + j] = n8[28 * i + j] + 1
                        else:
                            n8[28 * i + j] = 1
                    elif label == '9':
                        if 28 * i + j in n9:
                            n9[28 * i + j] = n9[28 * i + j] + 1
                        else:
                            n9[28 * i + j] = 1
    correct = 0
    total = 0
    k = 0.01
    for li in f4:
        total = total + 1
        testlist = []
        for i in range(28):
            l = f3.readline()
            for j in range(28):
                if l[j] == '#':
                    testlist.append(28 * i + j)

        p0 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n0:
                        p0 = p0 * (n0[28 * i + j] + k) / (numline[0] + k)
                    else:
                        p0 = p0 * k / (numline[0] + k)

        p1 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n1:
                        p1 = p1 * (n1[28 * i + j] + k) / (numline[1] + k)
                    else:
                        p1 = p1 * k / (numline[0] + k)

        p2 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n2:
                        p2 = p2 * (n2[28 * i + j] + k) / (numline[2] + k)
                    else:
                        p2 = p2 * k / (numline[0] + k)
        p3 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n3:
                        p3 = p3 * (n3[28 * i + j] + k) / (numline[3] + k)
                    else:
                        p3 = p3 * k / (numline[0] + k)
        p4 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n4:
                        p4 = p4 * (n4[28 * i + j] + k) / (numline[4] + k)
                    else:
                        p4 = p4 * k / (numline[0] + k)
        p5 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n5:
                        p5 = p5 * (n5[28 * i + j] + k) / (numline[5] + k)
                    else:
                        p5 = p5 * k / (numline[0] + k)
        p6 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n6:
                        p6 = p6 * (n6[28 * i + j] + k) / (numline[6] + k)
                    else:
                        p6 = p6 * k / (numline[0] + k)
        p7 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n7:
                        p7 = p7 * (n7[28 * i + j] + k) / (numline[7] + k)
                    else:
                        p7 = p7 * k / (numline[0] + k)
        p8 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n8:
                        p8 = p8 * (n8[28 * i + j] + k) / (numline[8] + k)
                    else:
                        p8 = p8 * k / (numline[0] + k)
        p9 = 1
        for i in range(28):
            for j in range(28):
                if 28 * i + j in testlist:
                    if 28 * i + j in n9:
                        p9 = p9 * (n9[28 * i + j] + k) / (numline[9] + k)
                    else:
                        p9 = p9 * k / (numline[0] + k)
        p0 = p0 * numline[0]
        p1 = p1 * numline[1]
        p2 = p2 * numline[2]
        p3 = p3 * numline[3]
        p4 = p4 * numline[4]
        p5 = p5 * numline[5]
        p6 = p6 * numline[6]
        p7 = p7 * numline[7]
        p8 = p8 * numline[8]
        p9 = p9 * numline[9]
        print(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
        m = max(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print(li[0], end='')
        if m == p0:
            if li[0] == "0":
                correct = correct + 1
            print(0)
        elif m == p1:
            if li[0] == "1":
                correct = correct + 1
            print(1)
        elif m == p2:
            if li[0] == "2":
                correct = correct + 1
            print(2)
        elif m == p3:
            if li[0] == "3":
                correct = correct + 1
            print(3)
        elif m == p4:
            if li[0] == "4":
                correct = correct + 1
            print(4)
        elif m == p5:
            if li[0] == "5":
                correct = correct + 1
            print(5)
        elif m == p6:
            if li[0] == "6":
                correct = correct + 1
            print(6)
        elif m == p7:
            if li[0] == "7":
                correct = correct + 1
            print(7)
        elif m == p8:
            if li[0] == "8":
                correct = correct + 1
            print(8)
        elif m == p9:
            if li[0] == "9":
                correct = correct + 1
            print(9)
    print(correct)
    print(total)
    print(correct / total)
    return(correct/total)



