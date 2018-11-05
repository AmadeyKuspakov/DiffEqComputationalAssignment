import numpy as np
from abc import ABC, abstractmethod

class InitData():

    # Class that contains initial data for easy access

    x0, y0, xf, n = None, None, None, None

    def __init__(self, x0, y0, xf, n):
        self.x0 = x0
        self.y0 = y0
        self.xf = xf
        self.n = n 

    def getInitData(self):
        return self.x0, self.y0, self.xf, self.n

    def getXInterval(self):
        return self.x0, self.xf

    def getInitX(self):
        return self.x0
    
    def getInitY(self):
        return self.y0

    def getIntervalNumber(self):
        return self.n

    def __str__(self):
        return "Initial Data is: x0=" + str(self.x0) + ", y0=" + str(self.y0) + ", xf=" + str(self.xf) + ", n=" + str(self.n)

class ComputationalDifferentialEquation(ABC):

    # Class contains methods that can be used in both exact and approximate computations

    def deltaX(self):
        # Defining step for a function
        x0, xf = initData.getXInterval()
        n = initData.getIntervalNumber()
        return (xf - x0)/(n-1)

    def __allocateArraysForCalculations(self):
        # This method allocates 2 array of x and y of n elements; 
        # array X contains a lot of numbers in which all of them are separated by step; 
        # array Y contains only 0s at the time
        n = initData.getIntervalNumber()
        x0, xf = initData.getXInterval()
        x = np.linspace(np.floor(x0),np.ceil(xf),n)
        y = np.zeros([n])
        return x, y

    def get_allocated_xyn(self):
        # This method returns 2 arrays for x and y and also a number of steps which is N
        x, y = self.__allocateArraysForCalculations()
        n = initData.getIntervalNumber()
        x[0] = initData.getXInterval()[0]
        y[0] = initData.getInitY()
        return x, y, n

    @abstractmethod
    def getFunction(self, x, y):
        pass

    @abstractmethod
    def compute(self):
        pass

class ApproximateSolution(ComputationalDifferentialEquation):

    # All classes that inherit from this class will be computed with this initial function

    def getFunction(self, x, y):
        return np.e**(-np.sin(x)) - y*np.cos(x)


class EulersMethod(ApproximateSolution):

    def compute(self):
        x, y, n = self.get_allocated_xyn()
        for i in range(1, n):
            y[i] = self.deltaX()*self.getFunction(x[i-1], y[i-1]) + y[i-1]
        return x, y

class ImprovedEulersMethod(ApproximateSolution):

    def __getSecondFunctionForImprovedEulersMethod(self, x, y):
        xForSecondFunction = x + self.deltaX()
        yForSecondFunction = y + self.deltaX() * self.getFunction(x, y)
        return xForSecondFunction, yForSecondFunction

    def __getSumOfTwoFunctionsDividedByTwo(self, x, y):
        x_secondFunctionForImprovedEulersMethod, y_secondFunctionForImprovedEulersMethod = self.__getSecondFunctionForImprovedEulersMethod(x, y)
        y1 = self.getFunction(x, y)
        y2 = self.getFunction(x_secondFunctionForImprovedEulersMethod, y_secondFunctionForImprovedEulersMethod)
        return (y1 + y2)/2

    def compute(self):
        x, y, n = self.get_allocated_xyn()
        for i in range(1, n):
            y[i] = self.deltaX()*self.__getSumOfTwoFunctionsDividedByTwo(x[i-1], y[i-1]) + y[i-1]
        return x, y

class RungeKutta(ApproximateSolution):

    def __k1(self, x, y):
        return self.deltaX() * self.getFunction(x, y)

    def __k2(self, x, y):
        newX = x + 0.5 * self.deltaX()
        newY = y + 0.5 * self.__k1(x, y)
        return self.deltaX() * self.getFunction(newX, newY)

    def __k3(self, x, y):
        newX = x + 0.5 * self.deltaX()
        newY = y + 0.5 * self.__k2(x, y)
        return self.deltaX() * self.getFunction(newX, newY)

    def __k4(self, x, y):
        newX = x + self.deltaX()
        newY = y + self.__k3(x, y)
        return self.deltaX() * self.getFunction(newX, newY)
    
    def __getSumOfKsDividedBySix(self, x, y):
        return (self.__k1(x, y) + 2*(self.__k2(x, y)) + 2*(self.__k3(x, y)) + self.__k4(x, y)) / 6 

    def compute(self):
        x, y, n = self.get_allocated_xyn()
        for i in range(1, n):
            x[i] = x[i-1] + self.deltaX()
            y[i] = y[i-1] + self.__getSumOfKsDividedBySix(x[i-1], y[i-1])
        return x, y

class ExactSolution(ComputationalDifferentialEquation):

    # This class is for plotting graph of exact solution

    def constant(self):
        x, y = initData.getInitX(), initData.getInitY()
        return (y - (np.e**(-np.sin(x))*x))/(np.e**(-np.sin(x)))

    def getFunction(self, x, y=None):
        c = self.constant()
        return np.e**(-np.sin(x)) * (x + c)

    def compute(self):
        x, y, n = self.get_allocated_xyn()
        for i in range(1, n):
            y[i] = self.getFunction(x[i-1])
        return x, y

class Error():

    def __init__(self):
        self.xExact, self.yExact = ExactSolution().compute()

    def getEulersMethodError(self):
        x, y = EulersMethod().compute()
        return x, np.absolute(y - self.yExact)

    def getImprovedEulersMethodError(self):
        x, y = ImprovedEulersMethod().compute()
        return x, np.absolute(y - self.yExact)
        
    def getRungeKuttaMethodError(self):
        x, y = RungeKutta().compute()
        return x, np.absolute(y - self.yExact)



initData = InitData(0, 1, 9.3, 101)

def setInitData(x0, y0, xf, n):
    global initData
    initData = InitData(x0, y0, xf, n)

def getInitData():
    global initData
    return str(initData)

def getEulersMethodSolution():
    return EulersMethod().compute()

def getImprovedEulersMethod():
    return ImprovedEulersMethod().compute()

def getRungeKuttaMethodSolution():
    return RungeKutta().compute()

def getExactSolution():
    return ExactSolution().compute()

def getEulersMethodError():
    return Error().getEulersMethodError()

def getImprovedEulersMethodError():
    return Error().getImprovedEulersMethodError()

def getRungeKuttaMethodError():
    return Error().getRungeKuttaMethodError()
    