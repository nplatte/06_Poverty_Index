## PA Poverty Index
The goal of this project is to do a basic data analysis of US Census Data. I went with a Chloropleth map of PA school districts as that seemed the most granular and accurate way of proceeding. To accomplish this, I used D3 map making on the front end and Echo Golang on the backend. Running this project will show a functional Chloropleth map of PA school districts shaded based on percentage of students in poverty for the year 2023. 

### Goals for the project
1. Right now the state and year are hard coded, I need to adjust this so that both state and year can be adjusted.
2. The coordinates D3 uses to draw the map and the Shape File provided by the US Census have two different methods for placing coordinates, to fix this, the server reverses the coordinates before drawing them on each render. A useful optimization would be fixing the coordinates on upload to the server and cutting that step out of the rendering process.
3. I should add sortable statistics for each school district. Right now you can see severity by visual refrence but you have no idea what the percentage of students in poverty actually is, nor what district.

### What Issues did I face?

1. The largest issue by far was learning D3's map maping process. It took a long time to find out the improper coordinate ordering in my shapefile. Once I found the issue and used the reverse function from the turf library, that was solved.
2. Once I dealt with that issue, I had to deal with an optimization issue where I was drawing dozens of maps on top of each other. This started crashing my browser whenever I loaded the webpage. The solution to this has to do with how the coordinated were appended to the geopath.
