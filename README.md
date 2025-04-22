# AAL-and-AEP

The python scripts are developed for the probabilistic modeling of Turkey and Brush Creek, Johnson County, KS. These are developed to calculate Average Annualized Loss (AAL) values and Annual Exceedance Probability (AEP) raster.

---

## __notebooks__:
- [__AAL_calculation__](scripts/AAL_calculation.ipynb): Calculates AAL values for all the buildings

- [__AEP_calculation__](scripts/AEP_calculation.ipynb): Calculates AEP raster based on all the events probability

- [__Data_Preparation_AAL__](scripts/Data_Preparation_AAL.ipynb): Contains scripts and functions to perform miscellaneous tasks to prepare input data which will be used in AAL calculation

- [__Heatmap_Turkey__](scripts/Heatmap_Turkey.ipynb): Creates a heatmap based on calculated AAL values


  ## __Folder Structure__
  - __csv_files__: It contains all the csv files that are supplied as input to the scripts. It's contents are:
      ```
        1. [__ddf_contents__](csv_files/ddf_contents.xlsx)
