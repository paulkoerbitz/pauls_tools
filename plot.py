import matplotlib.pyplot as pp
import numpy as np
import types

def multiplotFromListDict(ListDict, plotFunc=pp.plot, fig=None, saveTo=None,
        listOfKeyTitleTuplesToPlot=None,**kwargs):

    sizes = (110,120,130,220,230,230,330,240,330)

    if listOfKeyTitleTuplesToPlot is None:
        listOfKeyTitleTuplesToPlot = [ (k,k) for k in ListDict.keys()]

    nItems = len(listOfKeyTitleTuplesToPlot)
    
    if nItems > 9:
        warnings.warn("Warning: Only <=9 histograms can be plotted,"\
                "plotting first 9 entries in the dictionary")
        nItems = 9
    subplotPrefix = sizes[nItems-1]

    if fig is None:
        fig = pp.figure()

    if listOfKeyTitleTuplesToPlot is None:
        listOfKeyTitleTuplesToPlot = [(k,k) for k in ListDict.keys()]

    for i,k in enumerate(listOfKeyTitleTuplesToPlot):
        pp.subplot(subplotPrefix+i+1)
        plotFunc(np.array(ListDict[k[0]]),**kwargs)
        pp.title(k[1])

    if saveTo:
        pp.savefig(saveTo)
    else:
        pp.show()

def multiseriesPlotFromListDict(ListDict, plotFunc=pp.plot, fig=None,
        saveTo=None, xList=None, title=None, xlab=None, ylab=None, 
        listOfKeyLabelTuplesToPlot=None,show_legend=True,lkwargs=None):

    if fig is None:
        fig = pp.figure()

    if xList:
        if type(xList) is types.StringType:
            xVals = np.array(ListDict[xVals])
        else:
            xVals = np.array(xList)
    else:
        xVals = None

    if lkwargs is None:
        lkwargs = [{}]*len(ListDict)

    if listOfKeyLabelTuplesToPlot is None:
        listOfKeyLabelTuplesToPlot = [(k,k) for k in ListDict.keys()]

    for (key,label),kwargs in zip(listOfKeyLabelTuplesToPlot,lkwargs):
        if xVals is not None:
            plotFunc(xVals,np.array(ListDict[key]),label=label,**kwargs)
        else:
            plotFunc(np.array(ListDict[key]),label=label,**kwargs)
    if show_legend:
        pp.legend(loc='best')

    if title:
        pp.title(title)
    if xlab:
        pp.xlabel(xlab)
    if ylab:
        pp.ylabel(ylab)
    if saveTo:
        pp.savefig(saveTo)
    else:
        pp.show()
