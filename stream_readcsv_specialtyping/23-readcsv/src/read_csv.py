#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def getcommand(file):
    def lenSort(Index, L):
        lenList = sorted(map(lambda x:len(x[Index]), L))
        return lenList[-1]

    def printline(line, width0, width1):
        print(line[0].ljust(width0), line[1].ljust(width1), '{0:.2f}'.format(line[2]))

    num = int(input())
    for i in range(num):
        ins = input().split(' ')
        if ins[0] == 'INSERT':
            f = open(file, 'a')
            f.write('\n'+ins[1])
            f.close()
        elif ins[0] == 'SHOWALL':
            f = open(file)
            L = [['Name','Title','Salary']]
            while True:
                line = f.readline()

                if len(line) == 0:
                    break
                
                lineL = line.strip().split(',')
                lineL[2] = float(lineL[2])
                L.append(lineL)

            f.close()
            width0 = lenSort(0, L)
            width1 = lenSort(1, L)
            lineSorted = sorted(L[1:], key=lambda x: x[2])

            print('Name'.ljust(width0), 'Title'.ljust(width1), 'Salary')
            for l in lineSorted:
                printline(l, width0, width1)

            Len = len(lineSorted)
            if Len != 0:
                average = sum(map(lambda x: x[2], lineSorted)) / Len
                print('AVG:{0:.2f}'.format(average))