# Made by: Aarav Agarwal, IBCP-XI
## Summative Assessment 2

### Overview

The task that I have decided to pick is Task 2: Analyzing Disney Hotstar's Trends. The purpose of this project is to analyze trends in the movie and TV show content (for example genres, running time, release years and more), understand the content strategies of this industry and identify insights inferred from the data. <br/>

### Requirements
The following libraries are required for the project to run:
1. matplotlib
2. seaborn
3. pandas

The dataset "hotstar.csv" is also added to the GitHub repository. 

### Data preprocessing 
To load the data, I used the command "pd.read_csv()" from the file hotstar.csv. To make sure that the data was in the correct format for the numeric columns (i.e running_time, seasons, episodes), I converted them to the proper data types using "pd.to_numeric()" and errors='coerce' to handle invalid values. Any missing values were handled by filling them with zeroes using ".fillna(0)". <br/>

### Methods used
For the statistical analysis, I used the "groupby()", "agg()" (aggregation) functions to get key inferences such as average seasons, episodes, running time, genre counts, etc. To visualize the data, I used libraries like matplotlib and seaborn. Graphs like bar charts, line charts, density plot and stacked bar charts were created to identify different patterns in content releases, genre distribution and industrial shifts. <br/>

### Significant findings 
1. The average movie runtime has increased gradually over the years, suggesting a trend towards longer experiences. However, in the recent years, there seems to be a bifurcation, some movies have become shorter to cater to digital and the on-the-go consumption, while others (for example franchise films) have become longer to justify cinematic experiences. 

2. A huge rise in releases is observed from the early 2000s, also correlating with the growth of streaming platforms. Peak years for production indicate substantial growth in the industry, with great increases during the 2010s due to digital transformation and significant increase in media consumption. Recent years show a slight decline due to the COVID-19 pandemic impacting the production. 

3. Genres like drama and comedy significantly dominate the market, but there is an increasing variety in genre combination, suggesting diversity in audience preferences.  

4. Emotionally engaging or educational content is preferred by the audiences based on the viewer ratings for Drama and Documentary genres. 

5. Movie runtimes typically clustered around 90-120 minutes, but in the recent years, they've seen an uptick in movies over 150 minutes, indicating a split between theatrical and digital first movies. 


![age_rating_comparison_tv_movies](https://github.com/user-attachments/assets/dfce6892-d4db-4751-94f0-5804576312f5)
![age_rating_distribution_by_genre](https://github.com/user-attachments/assets/6fa488fd-527f-4000-84e0-1c85c0a268bd)
![average_running_time_bar_chart](https://github.com/user-attachments/assets/2477c958-617a-4541-b6bc-840d2098962c)
![content_longevity](https://github.com/user-attachments/assets/d1546a81-74cd-4b5c-aaf8-25bdc5e55c73)
![content_types_over_time](https://github.com/user-attachments/assets/da478a32-cdbf-47b7-903f-1e336b0c90fb)
![genre_comparison_tv_movies](https://github.com/user-attachments/assets/aacd4bc4-9625-4672-9228-efd4a4435b94)
![genre_distribution](https://github.com/user-attachments/assets/703302ae-e5d4-4c32-8054-c7bdbd024455)
![movie_running_time_trends](https://github.com/user-attachments/assets/8aec0dbd-3a87-467e-b516-d8a6ad95081d)
![release_year_comparison_tv_movies](https://github.com/user-attachments/assets/4864e244-acfd-4828-99e5-60eb6e2a4930)
![release_year_trends_tv_movies](https://github.com/user-attachments/assets/7182dd9f-e633-4d0b-8999-600298fa513f)

### Citations <br/>
https://chatgpt.com/ <br/>
https://seaborn.pydata.org/tutorial/introduction.html <br/>
https://www.geeksforgeeks.org/python-seaborn-tutorial/ <br/>
https://matplotlib.org/stable/api/pyplot_summary.html <br/>
https://medium.com/@anaraquel.fiap/exploratory-data-analysis-with-python-disney-movies-ab2e35a77121 
https://medium.com/analytics-vidhya/portfolio-project-1-disney-movie-anaysis-12190297d1fe


