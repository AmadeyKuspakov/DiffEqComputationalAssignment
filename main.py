import diffeqssolver
import graph

while(True):
    print("Please provide initial value of the program:")
    print("x0:")
    x0 = input()
    print("y0:")
    y0 = input()
    print("xf:")
    xf = input()
    print("n:")
    n = input()

    diffeqssolver.setInitData(int(x0), int(y0), int(xf), int(n))

    x, y = diffeqssolver.getEulersMethodSolution()

    graph.addFunctionPlot(x, y, "Euler's method Solution")

    x, y = diffeqssolver.getImprovedEulersMethod()

    graph.addFunctionPlot(x, y, "Improved Euler's method Solution")

    x, y = diffeqssolver.getRungeKuttaMethodSolution()

    graph.addFunctionPlot(x, y, "Runge Kutta method Solution")

    x, y = diffeqssolver.getExactSolution()

    graph.addFunctionPlot(x, y, "Exact Solution")

    x, y = diffeqssolver.getEulersMethodError()

    graph.addFunctionErrorPlot(x, y, "Error of Euler's method")

    x, y = diffeqssolver.getImprovedEulersMethodError()

    graph.addFunctionErrorPlot(x, y, "Error of Improved Euler's method")

    x, y = diffeqssolver.getRungeKuttaMethodError()

    graph.addFunctionErrorPlot(x, y, "Error of Runge-Kutta method")

    graph.showPlot()

    print("Please enter Exit to stop execution of the program. Or press enter to continue.")
    str_input = input()
    if str(str_input) == "Exit":
        break
    graph.clearPlot()