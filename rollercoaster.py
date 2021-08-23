import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood_rankings.head())
print(steel_rankings.head())

# function to plot rankings over time for 1 roller coaster here:

def plot_rankings(dataset, coaster):
    # fetch series of points scored by the coaster
  rankings = dataset['Points'][dataset.Name == coaster]
    # fetch years of those points scored
  years = dataset['Year of Rank'][dataset.Name == coaster]
  #print(years)
  # plot the line graph
  plt.plot(range(len(rankings)),rankings)
  ax = plt.subplot()
  ax.set_xticks(range(len(rankings)))
  ax.set_xticklabels(years)
  plt.title(coaster + ' Points Earned by Year')
  plt.xlabel('Year')
  plt.ylabel('Points')
  plt.show()

plot_rankings(wood_rankings, 'El Toro')

plt.clf()

# function to plot rankings over time for 2 roller coasters here:

def plot_two_rankings(dataset1, coaster1, dataset2, coaster2):
    # fetch series of points scored by coaster 1
  rankings = dataset1['Points'][dataset1.Name == coaster1]
    # fetch years of those points scored
  years = dataset1['Year of Rank'][dataset1.Name == coaster1]
  # print(years)
  # plot the line graph
  plt.plot(range(len(rankings)),rankings)
  ax = plt.subplot()
  ax.set_xticks(range(len(rankings)))
  ax.set_xticklabels(years)
  plt.title(coaster1 + ' Points Earned by Year')
  plt.xlabel('Year')
  plt.ylabel('Points')

  # fetch series of points scored by the coaster2
  rankings2 = dataset2['Points'][dataset2.Name == coaster2]
  # fetch years of those points scored
  years2 = dataset2['Year of Rank'][dataset2.Name == coaster2]
  # plot the line graph
  plt.plot(range(len(rankings2)),rankings2)
  plt.legend(coaster1, coaster2)
  ax = plt.subplot()
  ax.set_xticks(range(len(rankings2)))
  ax.set_xticklabels(years2)

  plt.show()

plot_two_rankings(wood_rankings, "El Toro", wood_rankings, "Boulder Dash")

plt.clf()

# function to plot top n rankings over time here:
def plot_top_n(dataset, n):
    # get points from the dataset
    points = dataset[dataset.Rank <= n]
    # get the names of the coasters from the new df
    names = points.Name[0:5]
    # get unique year values for x ticks
    year_range = points['Year of Rank'].unique()
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    # loop the length of names and plot each coaster one by one
    for x in range(n):
      name = names[x]
      value = points.Points[points.Name == name]
      plt.plot(range(len(value)), value, color=colors[x], label=name)
    ax = plt.subplot()
    ax.set_xticks(range(len(year_range)))
    ax.set_xticklabels(year_range)
    plt.legend(names)
    plt.title('Top 5 Coasters')
    plt.show()

plot_top_n(wood_rankings, 5)

plt.clf()

# load roller coaster data here:
overall = pd.read_csv('roller_coasters.csv')
print(overall.head())

# function to plot histogram of column values here:
#def hist_gen(df, colName):
    #data = df.colName
    #plt.hist(data)
    #plt.show()









plt.clf()

# write function to plot inversions by coaster at a park here:
def inver_bar(df, park):
    # get number of inversions
  coasters = df.num_inversions[df.park == park]
   # get ride names
  ride_names = df.name[df.park == park]
  # initialize ax so you can change x tick labels to park rides
  ax = plt.subplot()
  plt.bar(range(len(coasters)), coasters)
  ax.set_xticks(range(len(coasters)))
  # set xtick to park rides
  ax.set_xticklabels(ride_names, rotation=90)
  plt.title('Inversions by Ride at ' + park)
  plt.xlabel('Park')
  plt.ylabel('Inversions')
  plt.show()

inver_bar(roller_coasters, 'Parc Asterix')
plf.clf()

# function to plot pie chart of operating status here:
def open_vs_closed(df):
  num_open = df[df.status == 'status.operating']
  num_closed = df[df.status == 'status.closed.definitely']
  status = [len(num_open), len(num_closed)]
  cats = ['Operating', 'Closed']
  plt.pie(status, labels=cats, autopct='%d%%')
  plt.axis('equal')
  plt.title('Operating Roller Coasters')
  plt.show()

# Create pie chart of roller coasters
open_vs_closed(roller_coasters)
plt.clf()

# function to create scatter plot of any two numeric columns
def scatter_two_col(df, col1, col2):
  colData = df[col1]
  colData2 = df[col2]
  plt.scatter(colData, colData2)
  plt.show()

# plot scatter of speed vs height
scatter_two_col(roller_coasters, 'speed', 'height')
# plot of roller coaster height by speed
scatter_two_col(roller_coasters, 'height', 'speed')

plt.clf()
