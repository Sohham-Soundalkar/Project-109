import plotly.figure_factory as pf
import pandas as pd
import csv
import plotly.graph_objects as pg
import statistics as st
import random

df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()

mean = sum(data)/len(data)
print('Mean: ', mean)

median = st.median(data)
print('Median: ', median)

mode = st.mode(data)
print('Mode: ', mode)

standardDeviation = st.stdev(data)
print('SD: ', standardDeviation)

first_sd_start, first_sd_end = mean-standardDeviation, mean+standardDeviation
second_sd_start, second_sd_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
third_sd_start, third_sd_end = mean-(3*standardDeviation), mean+(3*standardDeviation)

graph = pf.create_distplot([data],['results'],show_hist=False)
graph.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.17],mode='lines', name ='mean'))
graph.add_trace(pg.Scatter(x=[first_sd_start,first_sd_start], y=[0,0.17],mode='lines', name = 'SD1'))
graph.add_trace(pg.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode='lines', name = 'SD1'))
graph.add_trace(pg.Scatter(x=[second_sd_start,second_sd_start], y=[0,0.17],mode='lines', name = 'SD2'))
graph.add_trace(pg.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode='lines', name = 'SD2'))
graph.add_trace(pg.Scatter(x=[third_sd_start,third_sd_start], y=[0,0.17],mode='lines', name = 'SD3'))
graph.add_trace(pg.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17],mode='lines', name = 'SD3'))
graph.show()

#printing the findings of how much data lies within each standard deviation
sd1 = [result for result in data if result > first_sd_start and result < first_sd_end]
sd2 = [result for result in data if result > second_sd_start and result < second_sd_end]
sd3 = [result for result in data if result > third_sd_start and result < third_sd_end]

print('{}% of data lies within first sd'.format(len(sd1)*100.0/len(data)))
print('{}% of data lies within second sd'.format(len(sd2)*100.0/len(data)))
print('{}% of data lies within third sd'.format(len(sd3)*100.0/len(data)))