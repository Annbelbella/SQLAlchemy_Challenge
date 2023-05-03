# SQLAlchemy_Challenge

This challenge was about climate analysis in Honolulu, Hawaii to aid planning of a long holiday vacation there. 

## Part 1: Analyze and Explore the Climate Data
In this section, i used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, i used SQLAlchemy ORM queries, Pandas, and Matplotlib. 

The following questions were answered ;

### Precipitation Analysis.
- Find the most recent date in the dataset.
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
-Select only the "date" and "prcp" values.
- Load the query results into a Pandas DataFrame. Explicitly set the column names.
- Sort the DataFrame values by "date".
- Use Pandas to print the summary statistics for the precipitation data.
- Plot the results by using the DataFrame plot method, as the following image shows:

![image](https://user-images.githubusercontent.com/124645643/235828737-a909b298-551b-4c8a-abe3-634ea3016c1c.png)

### Station Analysis
- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:List the stations and observation counts in descending order.
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Which station id has the greatest number of observations?
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
- Filter by the station that has the greatest number of observations.
- Query the previous 12 months of TOBS data for that station.
- Plot the results as a histogram with bins=12, as the following image shows:
- List the stations and observation counts in descending order.

![image](https://user-images.githubusercontent.com/124645643/235830094-057ffd0d-54eb-41d9-ad87-d366ff76ccfa.png)

## Part 2: Design Your Climate App
In this section, I  designed a Flask API based on queries and below are the routes that i created;

![image](https://user-images.githubusercontent.com/124645643/235829830-40ffc90f-5612-443e-9236-7509c5c60a8a.png)

### References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910.
