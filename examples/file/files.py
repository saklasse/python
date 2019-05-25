import sys
sys.path.append("../../code")
from file.csvFile import openFile
from graph.graph import plotXyScatter, show, plotLine

if __name__ == '__main__':
    sampleContents = openFile("sample.csv")
    xyScatterContents = openFile("xyScatter.csv")
    plotXyScatter(xyScatterContents, "Scatter Plot")
    plotLine(xyScatterContents, "Line Plot")
    show()