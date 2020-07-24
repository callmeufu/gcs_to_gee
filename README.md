# gcs_to_gee
This script is designed to read a local csv file containing uri links from a GCS bucket, then generate multi-tile manifest and upload it into Google Earth Engine as a single asset in an image collection. Learn more about manifest uploads here. https://developers.google.com/earth-engine/image_manifest#using-manifests

You need to have local csvs in the format of the example included in this repository. The uri links should all end in .tif
These links should be in a personal or publicly accessible bucket

In the script:

Update the date that the tiles refer to. You can also add other data for other properties like the region or whatever else may be relevant

Update the filename to the name of your local file & directory
filename = "tz_bd_10_19.csv" 

Update the eeCollectionName to your own pre-made earth engine image collection.
eeCollectionName = "projects/earthengine-legacy/assets/users/planetufuoma/tza_monthly_bd" 
