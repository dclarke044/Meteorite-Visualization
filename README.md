# Meteorite Landing Visualizations

## Project Objective
Our team decided to visualize meteorite landings. We will use a dataset from NASA to analyze location, type, class, and size of meteorites that have been found around the world. The 

Link to Data Set: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh

Link to GitHub: https://github.com/EMENGH/Project-2

Prototype/Inspirations: https://github.com/EMENGH/Project-2/blob/master/proto_HTML.xlsx

Link to Vega-Lite (The new JS Library): https://vega.github.io/vega-lite/

### Methods Used
* Data Cleaning
* Data Visualization

### Technologies
* Python
* Pandas
* Jupyter
* Javascript
* D3
* HTML
* CSS
* Vega-Lite
* Leaflet
* Plotly
* DataTables
* Flask
* PostGres

## Project Description

In the data cleaning process we ran into some issues with the size of the dataset. We decided to eliminate all meteorites with numbers in the name. Those were just smaller pieces of broken meteorites that were already represented in the data. Also, their sizes were too small to include in some of the visualizations that we were preparing.

We also needed to find a way to combine the classes into larger representative groups. We grouped them into 7 large categories to better visualize the differences between the classes and added these main categories to a new column in out dataframe.
