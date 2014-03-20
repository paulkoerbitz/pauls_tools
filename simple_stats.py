#!/usr/bin/env python
from numpy import sqrt

def mean(coll):
    return sum(coll) / float(len(coll))

def variance(coll):
    sum = 0.0
    sum_sq = 0.0
    for item in coll:
        sum += item
        sum_sq += item*item
    n = float(len(coll))
    return (sum_sq - sum*sum / n) / n

def std(coll):
    return sqrt(variance(coll))

def quantile(q):
    def quant(coll):
        n = len(coll)
        float_i = q * (n-1)
        trunc_i = int(float_i)
        sorted_coll = sorted(coll)
        if trunc_i == float_i:
            return sorted_coll[trunc_i]
        else:
            return 0.5*(sorted_coll[trunc_i] + sorted_coll[trunc_i + 1])
    return quant

def acf(coll, lag=1):
    m = mean(coll)
    sum = 0.0
    n = len(coll)
    for i in range(n-lag):
        sum += (coll[i]-m)*(coll[i+lag]-m)
    return sum / ((n-lag)*variance(coll))

median = quantile(0.5)

def compute_stats(coll, stat_fs):
    return [f(coll) for f in stat_fs]
