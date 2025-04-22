# AAL-and-AEP

The python scripts are developed for the probabilistic modeling of Turkey and Brush Creek, Johnson County, KS. These are developed to calculate Average Annualized Loss (AAL) values and Annual Exceedance Probability (AEP) raster.
This script, at this point of time, includes the calculation only for Turkey Creek.

---

## __notebooks__:
- [__AAL_calculation__](scripts/AAL_calculation.ipynb): Calculates AAL values for all the buildings

- [__AEP_calculation__](scripts/AEP_calculation.ipynb): Calculates AEP raster based on all the events probability

- [__Data_Preparation_AAL__](scripts/Data_Preparation_AAL.ipynb): Contains scripts and functions to perform miscellaneous tasks to prepare input data which will be used in AAL calculation

- [__Heatmap_Turkey__](scripts/Heatmap_Turkey.ipynb): Creates a heatmap based on calculated AAL values

---
## __Folder Structure and Contents__
The __csv_files__, __shps__, and __Turkey_wse_rasters_Slop__ contains the input data that are required for this script to run.
- __csv_files__: It should contain all the csv/excel files that are supplied as input to the scripts. The excel/csv files under this folder should contain the following files:
          ```
          1. ddf_contents.xlsx: It stores the Depth-Damage Function (DDF) curves for contents within the building.
          2. ddf_struct.xlsx: It stores the DDF curves for structure of the building.
          3. event_weights_TurkeyCreek.csv: It has the probability weights of all the events modeled (i.e., 96 different probability weights for 96 events in our case)
          ```

    There is a "reference" folder which contains other csv/excel files from FEMA HAZUS's FAST. The files within reference folder were used to determine "ddf_contents.xlsx" and "ddf_struct.xlsx".
   ---

- __shps__: It should have the shapefile of that contains the building data and all its required attributes.
  
    1. There are two folder within this folder: __point_shp__ and __polygon_shp__.
    2. The __point_shp__ folder contains the building shapefile that contains the point shapefile of all the buildings along with all the required attributes.
    Note: The building shapefile whould contain the Occupany ID that matches with the ID that is asssigned in Depth-Damage Function (DDF) curves.
    ---

- __Turkey_wse_rasters_Slop__: It stores all the water surface elevation (WSE) rasters (.tif files) from all 96 events.
  
    ---
- __outputs__: All the outputs generated are saved into this folder.
          ```
          1. AEP provides a single raster as the output file.
          2. For AAL, we save both the geodataframe/shapefile and a csv file that includes all the building attributes plus the calculated AAL values.
          ```
    
---

## __Workflow__
- Run [AAL_calculation](scripts/AAL_calculation.ipynb) to calculate the AAL values and save the outputs.
    ```
      Inputs:
        1. Building shapefile containing all building points and all the attributes
        2. All the WSE rasters (96 in our case)
        3. Excel file containing the DDF functions for both structure and contents
        4. csv file containing the probability weights of all the events
    ```
    
- Run [AEP_calculation](scrip[ts/AEP_calculation.ipynb) to calculate the AEP raster
    ```
      Inputs:
        1. All the WSE rasters (96 in our case)
        2. csv file containing the probability weights of all the events
    ```

- To calculate heatmap based on calculatedAAL data, [Heatmap_Turkey](scripts/Heatmap_Turkey.ipynb) can be used. However, this script is currently not finalized yet. 
