# gcs_to_gee
This script is designed to read a local csv file containing uri links from a GCS bucket, then generate and upload a single multi-tile asset into Google Earth Engine

You need to have local csvs in the format of the example included in this repository. The uri links should all end in .tif
These links should be in a personal or publicly accessible bucket
In the script, manually enter the date that the tiles refer to. You can also add other properties like the region or whatever else may be relevant

Update the filename to the name of your local file & directory
filename = "tz_bd_10_19.csv" 

Update the eeCollectionName to your own pre-made earth engine image collection.
eeCollectionName = "projects/earthengine-legacy/assets/users/planetufuoma/tza_monthly_bd" 
