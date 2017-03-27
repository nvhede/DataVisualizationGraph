#TIme to take parsed info and turn it into visual data!

from collections import Counter
from parse import parse
import csv
import matplotlib.pyplot
import numpy as np

MY_FILE = "C:/Users/nvhed/Desktop/Coding/MySourceFiles/incident.csv.txt"
parsed_Data = parse (MY_FILE, ',')

def visualize_days (parsed_data):
    parsed_Data = parsed_data
    """Visualize data by day of week"""
    #returns a dict where it sums the total values for each key
    #here, keys - DayofWeek, values = # of incidents
    counter = Counter(item["DayOfWeek"] for item in parsed_Data)
    #tldr for item in data_file:
        # counter = Counter (item["DayofWeek"])
    #separate the values counted in counter and orders it correctly by labels:
    data_list = [
        counter ["Monday"],
        counter ["Tuesday"],
        counter ["Wednesday"],
        counter ["Thursday"],
        counter ["Friday"],
        counter ["Saturday"],
        counter ["Sunday"]
    ]
    #dicts are not immutable while tuples and lists are
    day_tuple = tuple (["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
    #with that y axis data, assign it a matplotlib plot instance
    matplotlib.pyplot.plot (data_list)
    #create the amount of ticks needed for our x axis and assign labels
    matplotlib.pyplot.xticks (range (len(day_tuple)), day_tuple)
    #save plot!
    matplotlib.pyplot.savefig ("Days.png")
    #close plot file
    matplotlib.pyplot.clf ()

def visualize_type (parsed_data):
    parsed_Data = parsed_data
    CategoryCount = Counter(item["Category"] for item in parsed_Data)
    #order doesn't matter here, so no need to make a list and convert it to a tuple
    xlabels = CategoryCount.keys ()
    yvalues = CategoryCount.values ()
    #set where the labels hit x axis; this helps place the ticks on the x axis
    xlocations = np.arange (len(xlabels)) + 0.5
    #width of each bar
    width = 0.5
    #assign our data to a bar plot
    matplotlib.pyplot.bar (xlocations, yvalues, width = width)
    #assign our x ticks and edit them
    matplotlib.pyplot.xticks (xlocations + width/2, xlabels, rotation = 90)
    #give room so labels aren't cut off in the graph
    matplotlib.pyplot.subplots_adjust (bottom = 0.4)
    #make overall graph larger, mess with certain functions, etc
    matplotlib.pyplot.rcParams ['figure.figsize'] = 12, 8
    matplotlib.pyplot.rcParams ['lines.linewidth'] = 2
    matplotlib.pyplot.rcParams ['lines.color'] = 'r'
    font = {'family' : 'Comc Sans MS',
            'weight' : 'bold',
            'size' : 10,
    }
    matplotlib.pyplot.rc ('font', **font)
    matplotlib.pyplot.savefig ('Graph2.png')
    matplotlib.pyplot.clf ()

def main ():
    visualize_days (parsed_Data)
    visualize_type (parsed_Data)
if __name__ == "__main__":
    main ()
