# LAB 2: GEOPROCESSING USING ArcPy

Our organization has moved onto a plot of land in a given zip code and we have safety concerns with existing bike paths that exist.  We would like to visualize the bike paths within this zip code area as well as display 500-meter buffers around facilities.  This visualization can help us in identifying bike paths that may pose safety concerns and aid in decisions to re-route these paths. In order to perform this analysis, we must complete a series of geoprocessing steps within the arcpy module.

##  Input shapefiles

We were given shapefiles for regional bike paths (*bike_route.shp*), parks (*parks.shp*), and facilities (*facilities.shp*) as well as a shapefile for our zip code (*zip.shp*).

##  The Code

The script within this repo, *Lab2.py*, performs the following operation:

1.  A clip analysis is performed with the arcpy module using parks.shp as the input feature and zip.shp as the clip feature.  The output which is all parks within our zipcode is saved as *parks_Clip.shp* in a Results folder in a local drive.
2.  After importing the environments from arcpy, the workspace environment folder is set.
3.  A buffer analysis is performed with *facilities.shp* as the input feature and 500 meters as the distance parameter.  The output is saved to the Results folder.
4.  A second buffer analysis that overwrites the previous buffer is performed.  The same inputs are used except that the dissolve option is selected.
5.  Variables for a second clip analysis are assigned.  *bike_routes.shp* is assigned to in_features, *zip.shp* is assigned to clip_features, a new filepath name, *bike_Clip.shp*, is assigned to out_features, and xy_tolerance is assigned to "".
6.  A clip is performed with the variables assigned in Step 5.  The output is a shapefile of all bike routes within our zip code.

##  Output

The following is the map displaying outputs of using this geoprocessing script.  The facilities buffer, clipped parks and bike routes, and zip code boundary are displayed:

![Map](/Lab2.jpg)
