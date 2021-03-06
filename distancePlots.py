'''
Dataset Used:
1.
The CSIC 2010 HTTP Dataset in CSV Format (for Weka Analysis) (2010) dataset is from a web penetration testing testbed for anomaly detection training.

2.
ADFA-IDS - Collected by Gideon Creech and Jiankun Hu of the Australian Defense Force Academy, ADFA IDS is an intrusion detection system dataset made publicly available in 2013, intended as representative of modern attack structure and methodology to replace the older datasets KDD and UNM. ADFA IDS includes independent datasets for Linux and Windows environments.
'''

import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
from math import sqrt
import pickle
import datetime

'''
-----------------------
Data cleanup Phase

Assigning numerical values for categorical fields

Method:
GET: 0
POST: 1
PUT: 2

Label:
anom: 0
norm:1

Protocol
HTTP/1.1: 0
----------------------
'''
def dataCleanup(data):
    
    for i in range(len(data['method'].values)):
        if data['method'].values[i] == "GET":
            data['method'].values[i] = 0
        elif data['method'].values[i] == "POST":
            data['method'].values[i] = 1
        elif data['method'].values[i] == "PUT":
            data['method'].values[i] = 2
        else:
            data['method'].values[i] = -1

    for i in range(len(data['label'].values)):
        if data['label'].values[i] == "anom":
            data['label'].values[i] = 0
        elif data['label'].values[i] == "norm":
            data['label'].values[i] = 1
        else:
            data['label'].values[i] = -1

    for i in range(len(data['protocol'].values)):
        if data['protocol'].values[i] == "HTTP/1.1":
            data['protocol'].values[i] = 0
        else:
            data['protocol'].values[i] = -1

    for i in range(len(data['pragma'].values)):
        if data['pragma'].values[i] == "no-cache":
            data['pragma'].values[i] = 0
        else:
            data['pragma'].values[i] = -1

    for i in range(len(data['cacheControl'].values)):
        if data['cacheControl'].values[i] == "no-cache":
            data['cacheControl'].values[i] = 0
        else:
            data['cacheControl'].values[i] = -1


    for i in range(len(data['connection'].values)):
        if data['connection'].values[i] == "close":
            data['connection'].values[i] = 0
        if data['connection'].values[i] == "keep-alive":
            data['connection'].values[i] = 1
        else:
            data['connection'].values[i] = -1

    for i in range(len(data['contentLength'].values)):
        if data['contentLength'].values[i] == "null":
            data['contentLength'].values[i] = -100
        else:
            data['contentLength'].values[i] = int(data['contentLength'].values[i])
        
    for i in range(len(data['contentType'].values)):
        if data['contentType'].values[i] == "null":
            data['contentType'].values[i] = 0
        else:
            data['contentType'].values[i] = -1



def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = len(list(set(list1).union(list2)))
    return float(intersection / union)

def levenshtein(seq1, seq2):  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    #print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def getDissimilarityDist(d, centroid):
    '''
    For some inputs, we take categorical differences
    For other inputs (concatenated or fields with options), we find jaccard difference = len(intersection)/len(union)
    For cookie, since closely similar cookie strings may have some relationship, we use levenshtein distance
    '''
    #method
    distMethod = abs(d[1]-centroid[1])
    #print("Method:",distMethod)
    
    #url
    url1 = d[2].split('/')
    url2 = centroid[2].split('/')
    distUrl = 1 - jaccard_similarity(url1,url2)
    #print("Url:",distUrl)

    #protocol
    distProtocol = abs(d[3]-centroid[3])
    #print("Protocol:",distProtocol)
    
    #userAgent
    ua1 = d[4].split('/')
    ua2 = centroid[4].split('/')
    distUserAgent = 1 - jaccard_similarity(ua1,ua2)
    #print("UA:",distUserAgent)
        
    #pragma
    distPragma = abs(d[5]-centroid[5])
    #print("Pragma:",distPragma)
    
    #cacheControl
    distCache = abs(d[6]-centroid[6])
    #print("Cache:",distCache)

    #accept
    accept1 = d[7].split(',')
    accept2 = centroid[7].split(',')
    distAccept = 1-jaccard_similarity(accept1,accept2)

    #print("Accept:",distAccept)
    #print(accept1, accept2)

    #acceptEncoding
    en1 = d[8].split(',')
    en2 = centroid[8].split(',')
    distAcceptEnc = 1 - jaccard_similarity(en1,en2)
    #print("Accept Enc:",distAcceptEnc)
    #print(en1, en2)
    
    #acceptCharset
    char1 = d[9].split(',')
    char2 = centroid[9].split(',')
    distAcceptChar = 1 - jaccard_similarity(char1,char2)
    #print("Accept Charset:",distAcceptChar)
    #print(char1, char2)
    
    #acceptLang
    lang1 = d[10].split(',')
    lang2 = centroid[10].split(',')
    distAcceptLang = 1 - jaccard_similarity(lang1,lang2)
    #print("Accept Lang:",distAcceptLang)
    
    #host
    host1 = d[11].split('.')
    host2 = centroid[11].split('.')
    distHost = 1 - jaccard_similarity(char1,char2)
    #print("Host:", distHost)
    
    #connection
    distConnect = abs(d[12] - centroid[12])
    #print("Connection:",distConnect)
    
    #contentLength
    distContLen = abs(d[13] - centroid[13])
    #print("Content Length:",distContLen)
    
    #contentType
    distContType = abs(d[14] - centroid[14])
    #print("Content Type:",distContType)
    
    #cookie
    cookie1 = d[15]
    cookie2 = centroid[15]
    distCookie = levenshtein(cookie1,cookie2)
    #print("Cookie:",distCookie)
    
    #payload
    pay1 = str(d[16]).split(',')
    pay2 = str(centroid[16]).split(',')
    distPayload = 1 - jaccard_similarity(pay1,pay2)
    #print("Payload:",distPayload)

    '''
    once we have differences input-wise

    We calculate euclidian distance as:
    
    dist(X,Y) = sqrt(summation( (xi-yi)^2) ))
                sqrt((x1-y2)^2 + (x2-y2)^2 + ...)

    We have added scaling factors:
    cookie sf = 0.01

    Yet to Implement: Normalise all inputs relative to average to eliminate bias

    '''

    distance = sqrt(pow(distMethod,2) + pow(distUrl,2) + pow(distProtocol,2) + pow(distUserAgent,2) + pow(distPragma,2) + pow(distCache,2) + pow(distAcceptEnc,2) + pow(distAcceptChar,2) + pow(distAcceptLang,2) + pow(distHost
        , 2) + pow(distConnect,2) + pow(distContType,2) + pow(distContLen*0.001,2) + pow(distCookie*0.01,2) + pow(distPayload,2)) 
    #print(distance)
    return (distance)

def validateModel():
    data = pd.read_csv('validationData.csv')
    dataCleanup(data)
    file2 = open(r'myLearnedData.pkl', 'rb')
    c1 = pickle.load(file2)
    c2 = pickle.load(file2)
    c3 = pickle.load(file2)
    c4 = pickle.load(file2)
    file2.close()
    correctCounts = 0
    wrongCounts = 0
    totalCounts = 0
    #True False Positive Negative: Positive means classified as anomalous
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    prettyPrintLine("Validating Model")
    for entry in data.values:
        print(entry, c1)
        #input()
        dist1 = getDissimilarityDist(entry, c1)
        dist2 = getDissimilarityDist(entry, c2)
        dist3 = getDissimilarityDist(entry, c3)
        dist4 = getDissimilarityDist(entry, c4)

        if dist1<dist2 and dist1<dist3 and dist1<dist4:
            if entry[17] == c1[17]:
                correctCounts = correctCounts+1
                tp = tp+1
            else:
                wrongCounts = wrongCounts+1
                fp = fp+1
            totalCounts = totalCounts+1
        elif dist2<dist3 and dist2<dist4:
            if entry[17] == c2[17]:
                correctCounts = correctCounts+1
                tp = tp+1
            else:
                wrongCounts = wrongCounts+1
                fp = fp+1
            totalCounts = totalCounts+1
        elif dist3<dist4:
            if entry[17] == c3[17]:
                correctCounts = correctCounts+1
                tn = tn+1
            else:
                wrongCounts = wrongCounts+1
                fn = fn+1
            totalCounts = totalCounts+1
        else:
            if entry[17] == c4[17]:
                correctCounts = correctCounts+1
                tn = tn+1
            else:
                wrongCounts = wrongCounts+1
                fn = fn+1
            totalCounts = totalCounts+1
    #print("Correct Classifications=",correctCounts)
    #print("Wrong Classifications =",wrongCounts)
    #print("Total Classifications=",totalCounts)

    now = datetime.datetime.now()
    afile = open(r'run_Results_Log.pkl', 'wb')
    
    pickle.dump(now.strftime("%Y-%m-%d %H:%M"), afile)
    pickle.dump(correctCounts, afile)
    pickle.dump(wrongCounts, afile)
    pickle.dump(totalCounts, afile)
    pickle.dump(tp, afile)
    pickle.dump(fp, afile)
    pickle.dump(tn, afile)
    pickle.dump(fn, afile)
    afile.close()

    
def prettyPrintLine(string):
    print('----------------------------------------------------------')
    print(string)
    print('----------------------------------------------------------\n')

def startTraining():
    data = pd.read_csv("ultraSmallData.csv")
    dataCleanup(data)
    prettyPrintLine("K Means")
    prettyPrintLine("Training started...")
    f1 = data['method'].values
    f2 = data['label'].values
    X = np.array(list(zip(f1, f2)))
    numOfDataEntries = len(data.values)

    initCentroid1 = random.randint(0, numOfDataEntries//4-100)
    initCentroid2 = random.randint(numOfDataEntries//4, numOfDataEntries//2-100)
    initCentroid3 = random.randint(numOfDataEntries//2, 3*numOfDataEntries//4-100)
    initCentroid4 = random.randint(3*numOfDataEntries//4, numOfDataEntries)

    ##print(data.values[initCentroid1])
    ##print(data.values[initCentroid2])
    ##print(data.values[initCentroid3])
    ##print(data.values[initCentroid4])
    ##print(data.values[initCentroid5])

    clusters = [[],[],[],[]]
    clusters[0].append(data.values[initCentroid1])
    clusters[1].append(data.values[initCentroid2])
    clusters[2].append(data.values[initCentroid3])
    clusters[3].append(data.values[initCentroid4])

    clustersConcise = [[],[],[],[]]
    clustersConcise[0].append(data.values[initCentroid1])
    clustersConcise[1].append(data.values[initCentroid2])
    clustersConcise[2].append(data.values[initCentroid3])
    clustersConcise[3].append(data.values[initCentroid4])

    #print(initCentroid1, initCentroid2, initCentroid3, initCentroid4)
    count = 0
    for entry in data.values:
        count = count+1
        if(count%10 < 7):
            continue
        #print(count)
        dist1 = getDissimilarityDist(entry, data.values[initCentroid1])
        #print("\n")
        dist2 = getDissimilarityDist(entry, data.values[initCentroid2])
        #print("\n")
        dist3 = getDissimilarityDist(entry, data.values[initCentroid3])
        #print("\n")
        dist4 = getDissimilarityDist(entry, data.values[initCentroid4])
        #print("\n")
        #print(dist1, dist2, dist3, dist4)
        if dist1<dist2 and dist1<dist3 and dist1<dist4:
            clusters[0].append(entry)
            clustersConcise[0].append(entry[17])
        elif dist2<dist3 and dist2<dist4:
            clusters[1].append(entry)
            clustersConcise[1].append(entry[17])
        elif dist3<dist4:
            clusters[2].append(entry)
            clustersConcise[2].append(entry[17])
        else:
            clusters[3].append(entry)
            clustersConcise[3].append(entry[17])

        #to recompute means
        for i in range(4):
            new_centers = np.array(X.mean(0))

    print("\nCentroids\n")
    print(data.values[initCentroid1], data.values[initCentroid2], data.values[initCentroid3], data.values[initCentroid4])
    print("Cluster 1: Labels classified")
    print(clustersConcise[0])
    print("\n\n")
    print("Cluster 2: Labels classified")
    print(clustersConcise[1])
    print("\n\n")
    print("Cluster 3: Labels classified")
    print(clustersConcise[2])
    print("\n\n")
    print("Cluster 4: Labels classified")
    print(clustersConcise[3])

    afile = open(r'myLearnedData.pkl', 'wb')
    pickle.dump(data.values[initCentroid1], afile)
    pickle.dump(data.values[initCentroid2], afile)
    pickle.dump(data.values[initCentroid3], afile)
    pickle.dump(data.values[initCentroid4], afile)
    #pickle.dump(clusters, afile)
    afile.close()