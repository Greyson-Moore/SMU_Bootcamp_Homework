PyWeather and PyVacation-
Greyson Moore-
Instructor Alexander Booth-
SMU Data Analytics-

Description: 
Contains two programs pyweather and pyvaction. Pyweather uses random longitudes and latitudes to pick 500+ cities around the globe.
It then calls the OpenWeather API to get current weather data for each city and organizes it in a dataframe. The program creates
several scatter plots and performs regressions on latitude vs. various weather conditions. Pyvacation reads in a csv from the
city weather data collected in pyweather. The program creates a humidity map based on humidy %. It then whittles down the dataframe to 
cities that meet certain 'ideal' conditions for vacation. the program uses the Google API to locate hotels within the ideal cities.
It overlays markers representing each hotel on the humidity map.

Images:
Contains screenshot of gmap humidity map

programs:
Contains pyvacation and pyweather

output_data:
Contains cities_weather.csv and .png images of scatter plots from pyweather

Analysis:
- Temperature is affected by latitude. The closer to zero the more likely a temperature is to be higher
- Cloudiness and wind speed are not correlated with latitude.
- Humidity is unaffected by latitude in both the Northern and Southern hemispheres