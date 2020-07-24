import os
import json
import csv
from datetime import datetime
import time
import ee

ee.Initialize()
##this script assumes i have a csv file of the gs names in the same directory as the python file

date_str = '2019-10-01' #UPDATE
dt = datetime.strptime(date_str, '%Y-%m-%d')
date_in_epoch = time.mktime(dt.timetuple()) + dt.microsecond/1e6 #epoch format for manifest upload
# print(date_in_epoch)

country = "tza" #UPDATE for different countries
filename = "tz_bd_10_19.csv" #UPDATE filename for each month
eeCollectionName = "projects/earthengine-legacy/assets/users/planetufuoma/tza_monthly_bd" #no need to edit
tza_uris = [] #empty list to hold gs:ending in tif names

# #this creates an empty manifest and edits it for each uri
def update_manifest(uri_list, eeCollectionName, assetName, date, country):
    ''' Function that creates a new manifest file.
    Parameters:
    uri_list: list of gs:// uris ending in .tif
    date: epoch(seconds) representation of date
    eeCollectionName: string used to reference pre-made Image Collection in EE
    assetName: asset to upload the quads to. All quads for a month will be uploaded as a single mosaic
    country: 3-letter country code. Could be a good property to include
    '''

    source_json = {
      "name": "",
      "tilesets": [
        {
          "sources": [
          ]
        }
      ],
      "start_time": {
        "seconds": [""]
      },
      "end_time":{
        "seconds": [""]
      },
      "properties": {
        "country_name": [""]
      }
    }

    source_json['name'] = eeCollectionName + "/" + assetName
    for i in range(len(uri_list)):
        uri = uri_list[i]
        source_json['tilesets'][0]['sources'].append({"uris": uri})
    source_json['start_time']['seconds'] = date
    source_json['end_time']['seconds'] = date
    source_json['properties']['country_name'] = country
    
    # print(source_json)
    # print(os.getcwd())
    manifest_filename = "manifest_" + date_str
    with open(manifest_filename, "w") as write_file:
        json.dump(source_json, write_file)
    
    return write_file

def ee_ingest(manifest_file):
    ''' Function that calls the earthengine Python API command to ingest files stored on GCP into Earth Engine
    based on manifest upload.
    
    Parameters:
    mainfest_file: manifest to upload
    '''
    #print(os.getcwd())
    try:
        f = open(manifest_file.name)
        f.close()
    except FileNotFoundError:
        print('File does not exist')
    # print(os.path.exists('/home/ufuoma/' + manifest_file.name))
    cmd = 'earthengine upload image --manifest ' + '/home/ufuoma/' + manifest_file.name
    print(cmd)
    os.system(cmd)

with open(filename, "r") as csv_file:  
#open the csv file located in same directory as the python
#convert column into lists > tz_uris
#close the file
    for a in csv.reader(csv_file, delimiter=','):
    # Append each variable to a list
        tza_uris.append(a)

# assetName = "test_num3_7_14"
assetName = "bd_" + date_str #CHANGE BACK 
manifest = update_manifest(tza_uris, eeCollectionName, assetName, date_in_epoch, country)
ee_ingest(manifest)
