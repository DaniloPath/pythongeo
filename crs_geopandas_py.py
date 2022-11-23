# -*- coding: utf-8 -*-
"""CRS_Geopandas.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qZOKdjadjqeRwuDDERCSKYE9djv_8Mcp
"""

!pip install geopandas

import geopandas as gpd

# Read the file
fp = "/content/drive/MyDrive/Colab/L2_data/Europe_borders.shp"
data = gpd.read_file(fp)

#Check the coordenare reference system

data.crs

#Check value in our geometry

data['geometry'].head()

#Let’s re-project our data into EPSG 3035 using epsg -parameter:

#Let´s make a backup copy of our data
data_wgs83 = data.copy()

#Reproject the data
data = data.to_crs(epsg=3035)

#Check the new geometry values
data['geometry'].head()

data_wgs83.crs

# Explore our data visually
import matplotlib.pyplot as plt

#Make subplots that are next to each outher
fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2,figsize=(12,12))

#Plot the data in WGS84 CRS
data_wgs83.plot(ax=ax1, facecolor='gray')
#Add title
ax1.set_title("WGS84")

#Plot the one with ETRS-LAEA projection
data.plot(ax=ax2, facecolor='blue')
#Add title
ax2.set_title("ETRS Lambert Azimuthal Egual Area Projection")

#Set aspect ratio as 1
ax1.set_aspect(aspect=1)
ax2.set_aspect(aspect=1)

#Remove empty white space around the plot
plt.tight_layout()

#Save our projected layer into a Shapefile so that we can use it later

#Output filepath
outfp = "/content/drive/MyDrive/Colab/L2_data/Europe_borders_epsg3035.shp"
#Save to disk
data.to_file(outfp)

#Reproject the data to wgs84 geograph
data_wgs84 = data.to_crs(epsg=4326)

#Import CRS class from pyproj
from pyproj import CRS

#PROJ dictionary
crs_dict = data_wgs84.crs
#pyproj CRS object
crs_object = CRS(data_wgs84.crs)
#EPSG code (here, the input crs information is a bit vague so we need to lower the confidence threshold 25%)
crs_epsg = CRS(data_wgs84.crs).to_epsg(min_confidence=25)
#PROJ string
crs_proj4 = CRS(data_wgs84.crs).to_proj4()
#Wll-Known Text (WKT)
crs_wkt = CRS(data_wgs84.crs).to_wkt()

#Show the datas
print("PROJ dictionary:\n", crs_dict)
print("\nCRS object:\n", crs_object)
print("\nEPSG code: \n", crs_epsg)
print("\nPROJ string: \n", crs_proj4)
print("\nWell-Known Text (WKT):\n", crs_wkt)

#Verificting if crs is especifcty value
crs_epsg == 2326 #False

crs_epsg == 4326 #True

#Pyproj CRS object

#Let´s see the current CRS of our data
print(data.crs)

# Initialize the CRS class for epsg code 3035
crs_object = CRS.from_epsg(3035)
crs_object

# Name
print("Name:", crs_object.name)

# Coordinate system
print("Coordinate system:", crs_object.coordinate_system)

# Bounds of the area where CRS is used
print("Bounds:", crs_object.area_of_use.bounds)

# Retrive CRS information in WKT format
crs_wkt = crs_object.to_wkt()
print(crs_wkt)

# Retrive EPSG code from WKT text
epsg = CRS(crs_wkt).to_epsg()
print(epsg)

#  Let's try to extract the EPSG code from the crs of our original data
CRS(data.crs).to_epsg()

# Read in a global dataset and plot three maps with different projections! 

# Read in data
fp = "/content/drive/MyDrive/Colab/L2_data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
admin = gpd.read_file(fp)

#Check input crs
admin.crs

# Set fig size
plt.rcParams['figure.figsize'] = [12, 6]

# Plot in original crs
admin.plot()
plt.title(admin.crs.name)

# Define projection as web mercator, 3785
web_mercator = CRS.from_epsg(3785)

# Re-project and plot
admin.to_crs(web_mercator).plot()

# Remove x and y axis
plt.axis('off')
plt.title("Web mercator")

# Define projection Eckert IV from https://spatialreference.org/ref/esri/54012/
eckert_IV = CRS.from_proj4("+proj=eck4 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

# Re-project and plot
admin.to_crs(eckert_IV).plot()

# Remove x and y axis
plt.axis('off')
plt.title("Eckert IV")

# Define an orthographic projection, centered in Finland! from: http://www.statsmapsnpix.com/2019/09/globe-projections-and-insets-in-qgis.html
ortho = CRS.from_proj4("+proj=ortho +lat_0=60.00 +lon_0=23.0000 +x_0=0 +y_0=0 +a=6370997 +b=6370997 +units=m +no_defs")

# Re-project and plot
admin.to_crs(ortho).plot()

# Remove x and y axis
plt.axis('off')
plt.title("Ortographic")