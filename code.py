import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the CSV file
data = pd.read_csv('hotstar.csv') # <- note: please copy paste the path to the dataset for the project to work

#making sure that columns are properly formatted 
data['running_time'] = pd.to_numeric(data['running_time'], errors='coerce').fillna(0)
data['seasons'] = pd.to_numeric(data['seasons'], errors='coerce').fillna(0)
data['episodes'] = pd.to_numeric(data['episodes'], errors='coerce').fillna(0)


# -------------------------------------------------------------------------------


#1. Visualize Genre Distribution
genre_counts = data['genre'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(
    x=genre_counts.index[:10], 
    y=genre_counts.values[:10], 
    palette="viridis")

plt.title("Most common Genres", fontsize=14)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Count", fontsize=12) 
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

#saving the graph to a file
plt.savefig('genre_distribution.png')
plt.show()


# -------------------------------------------------------------------------------


#2. Content Longevity
#filtering usable tv show data
tv_show_data = data[(data['type'].str.lower() == 'tv') & (data['seasons'] > 0) & (data['episodes'] > 0)]

#aggregating data for analysis
tv_show_aggregated = tv_show_data.groupby('year').agg(
    avg_seasons=('seasons', 'mean'),
    avg_episodes=('episodes', 'mean')
).reset_index()

#plotting trends in average seasons and episodes over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=tv_show_aggregated, x='year', y='avg_seasons', label='Average Seasons', color='blue', marker='o')
sns.lineplot(data=tv_show_aggregated, x='year', y='avg_episodes', label='Average Episodes', color='green', marker='s')

#improving the plot
plt.title("Trends in TV Show Longevity Over the Years", fontsize=16)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Average Count", fontsize=12)
plt.legend(title="Metric", fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

#saving the graph to a file
plt.savefig('content_longevity.png')
plt.show()


# -------------------------------------------------------------------------------


#the seasonal graph is not possible since there is no season column in the CSV file


# -------------------------------------------------------------------------------


#4. Analyse Content Types Over Time
#grouping data by year and type
content_type_over_time = data.groupby(['year', 'type']).size().unstack(fill_value=0)

#getting proportions
content_type_over_time_normalized = content_type_over_time.div(content_type_over_time.sum(axis=1), axis=0)

#stacked bar plot of the proportions
content_type_over_time_normalized.plot(
    kind='bar', 
    stacked=True, 
    figsize=(12, 6), 
    colormap='coolwarm', 
    alpha=0.8
)

plt.title("Content Types Over Time (Proportions)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Proportion", fontsize=12)
plt.legend(title="Type", fontsize=10)
plt.tight_layout()

#saving graph to a file
plt.savefig('content_types_over_time.png')
plt.show()


# -------------------------------------------------------------------------------


#5. Distribution of content-type by running time and genre
#calculating average running time by genre type and running time
avg_running_time = data.groupby(['genre', 'type'])['running_time'].mean().reset_index()

plt.figure(figsize=(14, 8))

#creating a bar plot with genres on the x axis and running time on y axis
sns.barplot(
    data=avg_running_time,
    x='genre',
    y='running_time',
    hue='type',
    palette='Set2'
)

#improving plot
plt.title("Average Running Time by Genre and Content Type", fontsize=16)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Average Running Time (minutes)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend(title="Content Type", fontsize=10, loc='upper right')
plt.tight_layout()

#saving graph
plt.savefig('average_running_time_bar_chart.png')
plt.show()


# -------------------------------------------------------------------------------


#6. Analyse Age-Rating Distribution
#pivoting data to count age ratings for each genre
age_rating_distribution = data.pivot_table(
    index='genre', 
    columns='age_rating', 
    aggfunc='size', 
    fill_value=0
)

#sorting genres by total count of age ratings
age_rating_distribution = age_rating_distribution.loc[age_rating_distribution.sum(axis=1).sort_values(ascending=False).index]

#plotting a stacked bar chart
age_rating_distribution.plot(
    kind='bar', 
    stacked=True, 
    figsize=(14, 8), 
    colormap='viridis', 
    alpha=0.9
)

#plotting aesthetics
plt.title("Age Rating Distribution Across Genres", fontsize=16)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, fontsize=10)

plt.legend(
    title="Age Rating", 
    fontsize=10, 
    loc='center left', 
    bbox_to_anchor=(1.02, 0.5) 
)

plt.tight_layout()

#saving graph
plt.savefig('age_rating_distribution_by_genre.png')
plt.show()


# -------------------------------------------------------------------------------


# 7. Compare TV shows and Movies
#seperating data into tv shows and movies
tv_shows = data[data['type'].str.lower() == 'tv']
movies = data[data['type'].str.lower() == 'movie']

#visualizing genre distribution for tv shows and movies
plt.figure(figsize=(12, 6))

#genre count for tv shows and movies
tv_genre_counts = tv_shows['genre'].value_counts()
movie_genre_counts = movies['genre'].value_counts()

#plotting bar plot for genre comparison
genre_comparison = pd.DataFrame({
    'TV Shows': tv_genre_counts,
    'Movies': movie_genre_counts
}).fillna(0)

genre_comparison.plot(kind='bar', figsize=(14, 8), colormap='coolwarm')

plt.title("Genre Distribution Comparison between TV Shows and Movies", fontsize=14)
plt.xlabel("Genre", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

#saving graph
plt.savefig('genre_comparison_tv_movies.png')
plt.show()

#visualizing release year distribution for tv shows and movies
plt.figure(figsize=(12, 6))

#release year distributions
sns.kdeplot(tv_shows['year'], label='TV Shows', shade=True, color='blue')
sns.kdeplot(movies['year'], label='Movies', shade=True, color='red')

plt.title("Release Year Distribution Comparison between TV Shows and Movies", fontsize=14)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend(title="Content Type", fontsize=10)
plt.tight_layout()

#saving graph
plt.savefig('release_year_comparison_tv_movies.png')
plt.show()

#visualizing age rating distribution for tv shows and movies
plt.figure(figsize=(12, 6))

#age rating count for tv shows and movies
tv_age_rating_counts = tv_shows['age_rating'].value_counts()
movie_age_rating_counts = movies['age_rating'].value_counts()

#plotting bar plot for age rating comparison
age_rating_comparison = pd.DataFrame({
    'TV Shows': tv_age_rating_counts,
    'Movies': movie_age_rating_counts
}).fillna(0)

age_rating_comparison.plot(kind='bar', figsize=(14, 8), colormap='coolwarm')

plt.title("Age Rating Distribution Comparison between TV Shows and Movies", fontsize=14)
plt.xlabel("Age Rating", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

#saving graph
plt.savefig('age_rating_comparison_tv_movies.png')
plt.show()


# -------------------------------------------------------------------------------


# 9. Explore content length trends
#filtering dataset for movies
movies_data = data[data['type'].str.lower() == 'movie']

#confirming that all running time data is numeric 
movies_data['running_time'] = pd.to_numeric(movies_data['running_time'], errors='coerce')

#grouping by year and calculating average running time
movies_avg_running_time = movies_data.groupby('year')['running_time'].mean().reset_index()

#plot the trend in average running time over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=movies_avg_running_time, x='year', y='running_time', marker='o', color='red')

#set plot labels and title
plt.title("Average Movie Running Time Over the Years", fontsize=16)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Average Running Time (minutes)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

#saving graph
plt.savefig('movie_running_time_trends.png')
plt.show()


# -------------------------------------------------------------------------------


#10. Chart Release Year Trends
#grouping data by year and type to count releases
release_trends = data.groupby(['year', 'type']).size().unstack(fill_value=0)

#plotting a stacked bar chart to compare tv shows and movies released each year
release_trends.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='coolwarm', alpha=0.8)

#set plot labels and title
plt.title("Release Year Trends: TV Shows vs Movies", fontsize=16)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Number of Releases", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend(title="Content Type", fontsize=10)
plt.tight_layout()

#saving graph
plt.savefig('release_year_trends_tv_movies.png')
plt.show()


# --------------------------END OF CODE--------------------------------
