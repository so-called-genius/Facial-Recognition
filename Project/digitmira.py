import os
import math
#This is a comment
def ma(z):
    a=trainthedata(z)
    return a


def trainthedata(z):
    data = []
    f = open("trainingimages")
    f2 = open("traininglabels")
    f3 = open("testimages")
    f4 = open("testlabels")
    w0 = []
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    w5 = []
    w6 = []
    w7 = []
    w8 = []
    w9 = []

    for i in range(785):
        w0.append(0)
        w1.append(0)
        w2.append(0)
        w3.append(0)
        w4.append(0)
        w5.append(0)
        w6.append(0)
        w7.append(0)
        w8.append(0)
        w9.append(0)

    indexx = 0
    inde = 0
    for line in f2:
        if inde == len(z):
            indexx = indexx + 1
            break
        if indexx != z[inde]:
            indexx = indexx + 1
            for i in range(28):
                l = f.readline()
            continue
        inde = inde + 1
        indexx = indexx + 1
        
        label = line[0]
        fe = []
        for i in range(28):
            l = f.readline()
            for j in range(28):
                if l[j] == '#':
                    fe.append(1)
                else:
                    fe.append(0)

        s0 = 0
        for i in range(784):
            s0 = s0 + w0[i] * fe[i]
        s0=s0+w0[784]
        s1 = 0
        for i in range(784):
            s1 = s1 + w1[i] * fe[i]
        s1=s1+w1[784]
        s2 = 0
        for i in range(784):
            s2 = s2 + w2[i] * fe[i]
        s2=s2+w2[784]
        s3 = 0
        for i in range(784):
            s3 = s3 + w3[i] * fe[i]
        s3=s3+w3[784]
        s4 = 0
        for i in range(784):
            s4 = s4 + w4[i] * fe[i]
        s4=s4+w4[784]
        s5 = 0
        for i in range(784):
            s5 = s5 + w5[i] * fe[i]
        s5=s5+w5[784]
        s6 = 0
        for i in range(784):
            s6 = s6 + w6[i] * fe[i]
        s6=s6+w6[784]
        s7 = 0
        for i in range(784):
            s7 = s7 + w7[i] * fe[i]
        s7=s7+w7[784]
        s8 = 0
        for i in range(784):
            s8 = s8 + w8[i] * fe[i]
        s8=s8+w8[784]
        s9 = 0
        for i in range(784):
            s9 = s9 + w9[i] * fe[i]
        s9=s9+w9[784]
        s=-1000
        ind=-1
        t=[[s0,w0],[s1,w1],[s2,w2],[s3,w3],[s4,w4],[s5,w5],[s6,w6],[s7,w7],[s8,w8],[s9,w9]]
        for i in range(10):
            if t[i][0]>s:
                s=t[i][0]
                ind=i
        la=int(label)
        if(la!=ind):
            r=calr(t[ind][0],t[ind][1],t[la][0],t[la][1],fe)
            for i in range(784):
                t[ind][1][i] = t[ind][1][i] - r*fe[i]
            t[ind][1][784] = t[ind][1][784] - r
            for i in range(784):
                t[la][1][i] = t[la][1][i] + r*fe[i]
            t[la][1][784] = t[la][1][784] + r
        w0=t[0][1]
        w1=t[1][1]
        w2=t[2][1]
        w3=t[3][1]
        w4=t[4][1]
        w5=t[5][1]
        w6=t[6][1]
        w7=t[7][1]
        w8=t[8][1]
        w9=t[9][1]


    # Test the data
    correct = 0
    total = 0
    for li in f4:
        total=total+1
        fe = []

        # Read label into testlist
        for i in range(28):
            l = f3.readline()
            for j in range(28):
                if l[j] == '#':
                    fe.append(1)
                else:
                    fe.append(0)
        s0 = 0
        for i in range(784):
            s0 = s0 + w0[i] * fe[i]
        s0 = s0 + w0[784]
        s1 = 0
        for i in range(784):
            s1 = s1 + w1[i] * fe[i]
        s1 = s1 + w1[784]
        s2 = 0
        for i in range(784):
            s2 = s2 + w2[i] * fe[i]
        s2 = s2 + w2[784]
        s3 = 0
        for i in range(784):
            s3 = s3 + w3[i] * fe[i]
        s3 = s3 + w3[784]
        s4 = 0
        for i in range(784):
            s4 = s4 + w4[i] * fe[i]
        s4 = s4 + w4[784]
        s5 = 0
        for i in range(784):
            s5 = s5 + w5[i] * fe[i]
        s5 = s5 + w5[784]
        s6 = 0
        for i in range(784):
            s6 = s6 + w6[i] * fe[i]
        s6 = s6 + w6[784]
        s7 = 0
        for i in range(784):
            s7 = s7 + w7[i] * fe[i]
        s7 = s7 + w7[784]
        s8 = 0
        for i in range(784):
            s8 = s8 + w8[i] * fe[i]
        s8 = s8 + w8[784]
        s9 = 0
        for i in range(784):
            s9 = s9 + w9[i] * fe[i]
        s9 = s9 + w9[784]

        print(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9)
        m = max(s0,s1,s2,s3,s4,s5,s6,s7,s8,s9)
        print(li[0], end=' ')
        if m == s0:
            if li[0] == "0":
                correct = correct + 1
            print(0)
        elif m == s1:
            if li[0] == "1":
                correct = correct + 1
            print(1)
        elif m == s2:
            if li[0] == "2":
                correct = correct + 1
            print(2)
        elif m == s3:
            if li[0] == "3":
                correct = correct + 1
            print(3)
        elif m == s4:
            if li[0] == "4":
                correct = correct + 1
            print(4)
        elif m == s5:
            if li[0] == "5":
                correct = correct + 1
            print(5)
        elif m == s6:
            if li[0] == "6":
                correct = correct + 1
            print(6)
        elif m == s7:
            if li[0] == "7":
                correct = correct + 1
            print(7)
        elif m == s8:
            if li[0] == "8":
                correct = correct + 1
            print(8)
        elif m == s9:
            if li[0] == "9":
                correct = correct + 1
            print(9)

    print(correct)
    print(total)
    print(correct / total)
    return(correct/total)

def calr(w0,ww,t0,tt,ff):
    r=0
    while w0>=t0:
        w0=0
        t0=0
        r=r+0.01
        for i in range(784):
            w0=w0+(ww[i]-r*ff[i])*ff[i]
            t0=t0+(tt[i]+r*ff[i])*ff[i]
        w0=w0+ww[784]-r
        t0=t0+tt[784]+r
    return r



