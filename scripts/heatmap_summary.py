import pandas as pd
import geopandas as gpd
import folium 
from folium.plugins import HeatMap
from folium.plugins import MeasureControl
from folium import plugins
from shapely.geometry import Point
pd.set_option("display.max_columns",100)
import numpy as np
from matplotlib import pyplot as plt

pdDataframe = 'Pandas DataFrame'
gpdGeoDataFrame = 'GeoPandas GeoDataFrame'
FolMap = 'Folium Map'
DATAFIELDS = ['dmg_val_st', 'dmg_val_co', 'dmg_total']


def add_tiles(m: FolMap, tile_type:str='World_Imagery', services:str=''):
    """
    add different tiles to the interactive map
    inputs
        folmap = intitialized interactive map
        Defaults:
            - tile type = esri tile layer name (World_Imagery, USA_Topo_Maps, World_Shaded_Relief,
                                                World_Street_Map)
            - services  = access service sub dir or choose other ones (/Canvas,/Elevation,/Ocean,
                                                                        /Polar, etc)
            *note*  : if you change services then the tile needs to be changed according to the service
                        you want.
    """
    EsriImagery = "https://server.arcgisonline.com/ArcGIS/rest/services"\
                f"{services}/{tile_type}/MapServer/"\
                "tile/{z}/{y}/{x}"
    EsriAttribution = "Tiles &copy; Esri &mdash; Source: Esri, i-cubed,"\
                " USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP"\
                ", UPR-EGP, and the GIS User Community"
    folium.TileLayer(tiles=EsriImagery, attr=EsriAttribution, name=tile_type).add_to(m)
    return m


def df_to_gdf(data: pdDataframe, book: str, project_name: str):
    """
    Converts an aal dataframe into a gdf with geometry.
    Prints summary statistics.
    """
    use_cols = [col for col in data.columns if 'dmg' in col]
    geodf = gpd.GeoDataFrame(
        data[use_cols].copy(),
        crs='EPSG:4326',
        geometry=[Point(xy) for xy in zip(data.lon, data.lat)])

    print('{:,} {} Points for {}\n'.format(geodf.shape[0],book ,project_name))
    fresults = geodf[DATAFIELDS[0]].sum()
    presults = geodf[DATAFIELDS[1]].sum()
    tresults = geodf[DATAFIELDS[2]].sum()

    print('Sum of Average Annual Losses')
    print('-'*20)
    print('Structure: ${:,}'.format(int(fresults)))
    print('Contents: ${:,}'.format(int(presults)))
    print('Total  : ${:,}'.format(int(tresults)))
    return geodf


def get_outlier_info(data: gpdGeoDataFrame, threshold: int = 3000):
    """
    Subsets the data gdf based on an outlier threshold (default 3000).
    Prints outlier information/stats.
    """
    results = data[data[DATAFIELDS[1]] >threshold ]
    print('\nContents')
    print('-'*20)
    print(results[DATAFIELDS[1]].describe().round(2).to_string())

    results = data[data[DATAFIELDS[0]] >threshold ]
    print('\nStructure')
    print('-'*20)
    print(results[DATAFIELDS[0]].describe().round(2).replace(np.nan,0.0).to_string())


def map_aals(data: gpdGeoDataFrame, col: str, colname: str,
             location: list = [38.9, -77.0], zoom_start: int = 12):
    """
    Create a Folium HeatMap of AAL data.
    Inputs: 
        col = column name to visualize (e.g. 'FLUV_AAL')
        colname = more formal, readible alias of col. (e.g. 'Fluvial')
        location = center coordinates for the Folium map to render.
        zoom_start = initial level of zoom 
    """
    m = folium.Map(location=location, 
                  tiles = 'Stamen Terrain', 
                  zoom_start=12, )

    pointdata = HeatMap( list(zip(data.geometry.y, data.geometry.x, data[col].values)),
                       min_opacity=0.5,
                       radius=17, blur=15, 
                       max_zoom=1, 
                       name='{} Hotspots'.format(colname),
                       show=True, 
                       overlay=True, 
                       control=True
                     )

    add_tiles(m)
    m.add_child(MeasureControl())
    m.add_child(pointdata)

    plugins.Fullscreen(
        position='topleft',
        title='Full Screen Mode',
        title_cancel='Full Screen Mode',
        force_separate_button=True).add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)

    return m
