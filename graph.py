from matplotlib import pyplot as plt
import matplotlib as mpl

functionColorDeterminant = 0
errorColorDeterminant = 0


fig, (ax1, ax2) = plt.subplots(2,sharex=True)
def addFunctionPlot(x,y, label):
    global ax1, functionColorDeterminant
    color = "C" + str(functionColorDeterminant)
    ax1.plot(x, y, color, label=label)
    functionColorDeterminant = functionColorDeterminant + 1

def addFunctionErrorPlot(x, y, label):
    global ax2, errorColorDeterminant
    color = "C" + str(errorColorDeterminant)
    ax2.plot(x, y, color, label=label)
    errorColorDeterminant = errorColorDeterminant + 1

def clearPlot():
    global functionColorDeterminant, errorColorDeterminant
    ax1.clear()
    ax2.clear()
    functionColorDeterminant = 0
    errorColorDeterminant = 0

def showPlot():
    global ax1, ax2
    ax1.xlabel = "X"
    ax1.ylabel = "Y"
    ax2.xlabel = "X"
    ax2.ylabel = "Y"
    ax1.set_title("Plot of functions")
    ax2.set_title("Plot of errors")
    ax1.legend()
    ax2.legend()
    plt.ion()
    plt.show()