# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:51:37 2019

@author: Ryanz
"""
#import matplotlib.pyplot as plt
import csv
import os
redP = []
redN = []
blueP =[]
blueN = []
orangeP = []
orangeN = []
greenBP = []
greenBN = []
greenCP = []
greenCN = []
greenDP = []
greenDN = []
greenEP = []
greenEN = []
listOfCSV = []
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.csv'):
            listOfCSV.append(filename)
for i in range(len(listOfCSV)):
    with open(listOfCSV[i], newline='') as csvfile:
        read = csv.reader(csvfile)
        rateDate = []
        for row in read:
           # print(', '.join(row))
            #print(row)
            if row[0] == 'Red':
                rateDate.append(float(row[9])/float(row[10]))
                rateDate.append(row[6])
                redP.append(rateDate)
                rateDate = []
            
print(redP)
