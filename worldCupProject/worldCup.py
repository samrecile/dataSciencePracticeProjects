# !python3 file working with csv data found on Kaggle about the world cup
# csv files: https://www.kaggle.com/abecklas/fifa-world-cup

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# load the csv files
matches = pd.read_csv('WorldCupMatches.csv')
goals = pd.read_csv('goals.csv')
# inspect data
print(goals.head())

# sum goals create new column with result
matches['Total Goals'] = matches['Home Team Goals'] + matches['Away Team Goals']
print(matches.head())

# sets figure size to 12 inches wide 7 tall
f, ax = plt.subplots(figsize=(12,7))
# barplpot with year in x goals in y
sns.barplot(data=matches, x="Year", y="Total Goals")
# whitegrid style
sns.set_style("whitegrid")
sns.set_context('poster', font_scale=.5)
ax.set_title('Goals Scored by Year')
plt.show()

plt.clf()

# sets notebook style
sns.set_context('notebook', font_scale=1.25)
# creates boxplot
ax2 = sns.boxplot(data=goals, x='year', y='goals')
ax.set_title('Goals by Year')
plt.show()
