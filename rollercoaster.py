import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood_rankings.head())
print(steel_rankings.head())

# write function to plot rankings over time for 1 roller coaster here:

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

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

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
  #print(years)
  # plot the line graph
  plt.plot(range(len(rankings2)),rankings2)
  plt.legend(coaster1, coaster2)
  ax = plt.subplot()
  ax.set_xticks(range(len(rankings2)))
  ax.set_xticklabels(years2)

  plt.show()

plt.clf()

# write function to plot top n rankings over time here:
def plot_top_n(dataset, n):











plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
