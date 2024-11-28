# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:23:55 2024

@author: nestor.gualsaqui
"""

import geopandas as gpd
import ezdxf
import os
# --------------------------------------------------------------
# Infos
# 0-Black, 9-Brown,1-Red,10-Khaki,2-Yellow,11-Dark Green,3-Green,12-Steel Blue,4-Cyan
# 13-Dark Blue,5-Blue,14-Purple,6-Magenta,15-Dark Grey,16-White,8-Grey,17-Light Grey
#--------------------------------------------------------------
# setting data paths
cwd = os.getcwd()
dataPathFolder = os.path.join(cwd, 'data')
dataOutputFolder = os.path.join(cwd, 'output')
gpkgFilePath = os.path.join(dataPathFolder, 'Holzbuettgen_20231006.gpkg')
fullDXFoutputPath = os.path.join(dataOutputFolder, 'Holzbuettgen_converted_v3.dxf')


# Step 1: Read GeoPackage data
# layers in gdf
gdf_accesspoint = gpd.read_file(gpkgFilePath, layer = 'ACCESSPOINT')
gdf_drilling = gpd.read_file(gpkgFilePath, layer = 'DRILLING')
gdf_duct = gpd.read_file(gpkgFilePath, layer='DUCT')

# gdf_ductjoin = gpd.read_file(gpkgFilePath, layer='DUCTJOIN')
gdf_pop = gpd.read_file(gpkgFilePath, layer='POP')
doc = ezdxf.new()

# Define layers and their properties
accesspoint_layer = doc.layers.new(name='ACCESSPOINT')  # Red color
drilling_layer = doc.layers.new(name='DRILLING')        # Cyan color

# Set color for entities on each layer
accesspoint_layer.color = 1  # Red color
drilling_layer.color = 4     # Cyan color


# Convert gdf_accesspoint to DXF points and add to the 'ACCESSPOINT' layer
for idx, row in gdf_accesspoint.iterrows():
    point = row['geometry']
    doc.modelspace().add_point(point.coords[0], dxfattribs={'layer': 'ACCESSPOINT', 'linetype': 'Continuous'})

# Convert gdf_drilling to DXF polylines and add to the 'DRILLING' layer
for idx, row in gdf_drilling.iterrows():
    line = row['geometry']
    doc.modelspace().add_lwpolyline(line.coords, dxfattribs={'layer': 'DRILLING', 'linetype': 'Continuous'})

# Save the DXF file
doc.saveas(fullDXFoutputPath)
print("DXF file created successfully.")




