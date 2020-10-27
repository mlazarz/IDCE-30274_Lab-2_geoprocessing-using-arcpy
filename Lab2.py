# Author:  Mitchell Lazarz
# Python 2.7, Lab2.py
# Creation Date:  26 October 2020
# Description:  This code performs a clip on parks and bike routes within a zip code as well as creates a 500-meter buffer around facilities.  
# The output can be used to inform the UN of safety concerns with bike routes within the buffer of facility locations.

# Add parks.shp and zip.shp to contents of .mxd manually
# A clip is performed with parks as the input feature, zip as the clip feature, and the output saved as parks_Clip to a local results folder.
arcpy.Clip_analysis("parks", "zip", "C:\\CLARK\\PythonProgramming\\CompProg_Lab2\\Results\\parks_Clip.shp")

# The geoprocessing environments are imported.
from arcpy import env

# The geoprocessing workspace path is set on local drive.
env.workspace="C:\\CLARK\\PythonProgramming\\CompProg_Lab2"

# Add facilities.shp to contents of .mxd manually
# A 500 meter buffer is performed with facilities as the input feature.  The output is saved to the results folder.
arcpy.Buffer_analysis("facilities","\\Results\\facilities_buffer.shp","500 METERS")

# The previous buffer is modified and performed with adding a dissolve option.
arcpy.Buffer_analysis("facilities","\\Results\\facilities_buffer.shp","500 METERS","","","ALL")

# Input parameters for a clip analysis are assigned to variables.
in_features="\\Data_Lab_2_Geoprocessing_Python\\bike_routes.shp"  # Bike routes shapefile is the input feature.
clip_features="\\Data_Lab_2_Geoprocessing_Python\\zip.shp"        # Zip code shapefile is the clip feature.
out_features="\\Results\\bike_Clip.shp"                           # Output feature is saved as bike_Clip to Results folder.
xy_tolerance=""                                                   # XY tolerance is set to ""

# The clip is performed using the previously defined variables.
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)

