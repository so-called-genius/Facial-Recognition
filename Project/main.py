import digitnaive
import facenaive
import digitper
import faceper
import digitmira
import facemira
import numpy as np
def main():
    print("Choose what you want to test")
    a = input("1: digitnaive,  2: facenaive,  3: digitper,  4: faceper,  5: digitmira  6: facemira (enter 1~6): ")

    arr = []
    suu = []
    if a == '1':
        b = int(input("Choose the percentage of train (enter 1~100): "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        f = open("traininglabels")
        total = 0
        for line in f:
            arr.append(total)
            total = total + 1
        f.close
        per = int(per*total)
        for i in range (k):
            z = np.random.choice(arr, size=per, replace=False)
            z.sort()
            print(len(z))
            suu.append(digitnaive.ma(z))
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)
        
    elif a == '2':
        b = int(input("Choose the percentage of train: "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        f = open("facedatatrainlabels")
        total = 0
        for line in f:
            arr.append(total)
            total = total + 1
        f.close
        per = int(per*total)
        for i in range (k):
            z = np.random.choice(arr, size=per, replace=False)
            z.sort()
            print(len(z))
            suu.append(facenaive.ma(z))
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)
        
    elif a == '3':
        b = int(input("Choose the percentage of train: "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        p = faceper.Perceptron()
        for i in range(k):
            p.train(per)
            print(p.test())
            suu.append(p.test())
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)

    elif a == '4':
        b = int(input("Choose the percentage of train: "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        p = faceper.Perceptron()
        for i in range(k):
            s = p.train(per)
            print(p.test())
            suu.append(p.test())
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)

    elif a == '5':
        b = int(input("Choose the percentage of train: "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        f = open("traininglabels")
        total = 0
        for line in f:
            arr.append(total)
            total = total + 1
        f.close
        per = int(per*total)
        for i in range (k):
            z = np.random.choice(arr, size=per, replace=False)
            z.sort()
            suu.append(digitmira.ma(z))
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)

    elif a == '6':
        b = int(input("Choose the percentage of train: "))
        k = int(input("Choose num of test (enter any number): "))
        per = b/100
        f = open("facedatatrainlabels")
        total = 0
        for line in f:
            arr.append(total)
            total = total + 1
        f.close
        per = int(per*total)
        for i in range (k):
            z = np.random.choice(arr, size=per, replace=False)
            z.sort()
            suu.append(facemira.ma(z))
        m = np.mean(suu)
        s = np.std(suu)
        print("The mean is: ", end='')
        print(m)
        print("The standard deviation is: ", end='')
        print(s)
        

    return






if __name__ == '__main__':
    main()
