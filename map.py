import parse
from parse import parse, MY_FILE
import json
from json import dumps

def create_map (data_file):
    #define type of geojson we are creating (featurecollection)
    geo_map = {"type": "FeatureCollection"}
    #define empty list to collect each point to graph
    item_list = []
    #iterate over our data to create GeoJSON document.
    #we are using enumerate () so we'll get the line as well as the index/line #
    for index, line in enumerate (data_file):
        #skip any zero coordinates as this will throw off our map
        if line ['X'] == "0" or line ['Y'] == "0":
            continue
        #set up a new dict for each iteration
        data = {}
        #assign line items to appropriate GeoJSON fields
        #assign values of our parsed data file (feature, index, category, descript)
        #to keys in our empty data dict (type, id, properties)
        data ['type'] = 'Feature'
        data ['id'] = index
        #values of 'category' 'descript' and 'date' are assigned as
        # 'title', 'description' and 'date' values in the key 'properties'
        #this is basically making another dictionary in our dictionary for
        #the key, properties
        data ['properties'] = {'title': line ['Category'],
                                'description': line ['Descript'],
                                'date': line ['Date']}
        data ['geometry'] = {'type': 'Point',
                            'coordinates': (line ['X'], line ['Y'])}
        #add data dictionary to our item_list
        item_list.append (data)
    #for each pt in our item_list, we add the pt to our dict.
    #setdefault = creates key called 'features' that has a value type of []
    #with each iteration we are appending our pt to that empty list.
    for point in item_list:
        geo_map.setdefault ('features', []).append (point)
    #TLDR: our setup looks like this:
    #geo_map = {[item_list{data dicitionary keys and values{data second dictionary keys and values}}]}
    #now that all our data is parsed into a GeoJSON write to a file, we can
    #upload it to gist.github.com
    with open ('file_sf.geojson', 'w') as f:
        f.write (json.dumps(geo_map))

def main ():
    data = parse (MY_FILE, ',')
    return create_map(data)

if __name__ == '__main__':
    main ()
