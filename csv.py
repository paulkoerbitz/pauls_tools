from __future__ import absolute_import
import csv as Csv
import numpy as np
import matplotlib.pyplot as pp
import warnings
from paulsTools import plot

class excelSkipBlank(Csv.excel):
    skipinitialspace = True

def listDictFromCsv(filename):
    Csv.register_dialect('excelSkipBlank',excelSkipBlank)
    dr = Csv.DictReader(open(filename),dialect='excelSkipBlank')
    valDict = {}
    for name in dr.fieldnames:
        valDict[name] = []
    for row in dr:
        for k,v in row.iteritems():
            valDict[k].append(float(v))
    return valDict

def arrayDictFromCsv(filename):
    valDict = listDictFromCsv(filename)
    for k in valDict.keys():
        valDict[k] = np.array(valDict[k])
    return valDict

def multihistFromCsv(filename, nBins=100, saveTo=None):
    Dict = listDictFromCsv(filename)

    def histplot(data,nbins=nBins):
        pp.hist(data,bins=nbins,edgecolor='none')

    plot.multiplotFromListDict(Dict,histplot,None,saveTo)


def linesToDict(listOfStrings):
    valDict = {}
    for line in listOfStrings:
        key,nums = line.split(':')[0:1]
        valDict[key] = []
        for num in nums.split(','):
            valDict[key].append(float(num))
    return valDict
