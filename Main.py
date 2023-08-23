# Import the necessary library for data manipulation
import pandas as pd

# Load datasets from CSV files into pandas DataFrames
super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

# Display the first five rows of each DataFrame for a quick overview
display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())

# Display a summary of the TV dataset to inspect its columns and data types
tv.info()

print('\n')  # Print a newline for better readability

# Display a summary of the halftime musician dataset to inspect its columns and data types
halftime_musicians.info()

# Import necessary libraries for plotting
from matplotlib import pyplot as plt
# Ensure that plots are displayed inline in Jupyter notebooks
%matplotlib inline
# Set the plotting style to 'seaborn' for better aesthetics
plt.style.use('seaborn')

# Plot a histogram of combined points scored in Super Bowls
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display Super Bowls with the highest (more than 70) and lowest (less than 25) combined scores
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences in Super Bowls
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowl with the smallest point difference (most competitive game) and those with a difference of 35 or more (blowouts)
display(super_bowls[super_bowls['difference_pts'] == 1])
display(super_bowls[super_bowls['difference_pts'] >= 35])

# Merge the game and TV datasets, excluding Super Bowl I due to its unique broadcasting situation
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn for advanced plotting
import seaborn as sns
# Create a scatter plot with a linear regression model fit to see the relationship between point difference and household share
sns.regplot(x='difference_pts' , y='share_household', data=games_tv)

# Create a 3x1 subplot to visualize TV data trends over the years
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Adjust the spacing between subplots for better visualization
plt.tight_layout()

# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians.super_bowl <= 27]

# Count how many times each musician has performed during halftime and sort them in descending order
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians who have performed more than once during halftime shows
halftime_appearances[halftime_appearances['super_bowl'] > 1]

# Filter out marching bands and similar groups from the halftime musicians data
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram showing the distribution of number of songs performed by musicians during halftime shows
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.ylabel('Number of Musicians')
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.show()

# Sort the non-band musicians by the number of songs they performed and display the top 15
no_bands = no_bands.sort_values('num_songs', ascending=False)
display(no_bands.head(15))
