from numpy import *
import csv

#calculate average nationwide change in unemployment from this time last year to this year by week
week1 = 0
week2 = 0
week3 = 0
week4 = 0
week5 = 0
week6 = 0
week7 = 0
with open('unemployment.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        week1+=float(line[0])
        week2+=float(line[1])
        week3+=float(line[2])
        week4+=float(line[3])
        week5+=float(line[4])
        week6+=float(line[5])
        week7+=float(line[6])
week1 /= 52
week2 /= 52
week3 /= 52
week4 /= 52
week5 /= 52
week6 /= 52
week7 /= 52

unemployment=[week1,week2,week3,week4,week5,week6,week7]


#plot percent of poll surveyees who approve of Trump's response to COVID-19 against time (in weeks)
from scipy.interpolate import *
week=[]
approval=[]
unemployment_mag=[]
week1_approval = 0
week2_approval = 0
week3_approval = 0
week4_approval = 0
week5_approval = 0
week6_approval = 0
week7_approval = 0
week1_size = 0
week2_size = 0
week3_size = 0
week4_size = 0
week5_size = 0
week6_size = 0
week7_size = 0

with open('covid_approval_toplines.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        week.append(int(line[0]))
        approval.append(float(line[8]))
        if (int(line[0]) == 1):
            unemployment_mag.append(1)
            week1_approval += float(line[8])
            week1_size += 1
        elif (int(line[0]) == 2):
            unemployment_mag.append(2)
            week2_approval += float(line[8])
            week2_size += 1
        elif (int(line[0]) == 3):
            unemployment_mag.append(3)
            week3_approval += float(line[8])
            week3_size += 1
        elif (int(line[0]) == 4):
            unemployment_mag.append(4)
            week4_approval += float(line[8])
            week4_size += 1
        elif (int(line[0]) == 5):
            unemployment_mag.append(5)
            week5_approval += float(line[8])
            week5_size += 1
        elif (int(line[0]) == 6):
            unemployment_mag.append(6)
            week6_approval += float(line[8])
            week6_size += 1
        elif (int(line[0]) == 7):
            unemployment_mag.append(7)
            week7_approval += float(line[8])
            week7_size += 1

week1_approval /= week1_size
week2_approval /= week2_size
week3_approval /= week3_size
week4_approval /= week4_size
week5_approval /= week5_size
week6_approval /= week6_size
week7_approval /= week7_size
week_shortened = list(dict.fromkeys(week))
approval_shortened = [week1_approval, week2_approval, week3_approval, week4_approval, week5_approval, week6_approval, week7_approval]

import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_title("Unemployment rate and Trump approval rating over time")
ax1.set_xlabel("week (3/21~5/8)")
ax1.set_ylabel("% of people who approve of Trump's COVID-19 policies", color=color)
ax1.plot(week_shortened, approval_shortened, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("weekly % change in new unemployment claims compared with last year", color=color)
ax2.plot(week_shortened, unemployment, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
