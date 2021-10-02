import json
from datetime import datetime
import pandas as pd
file = open('User_Lat_24.76399_Lon_46.640249.json',)
 

data = json.load(file)
 

for i in data['properties']['parameter']['T2M']:
    print(i, " : ", data['properties']['parameter']['CLRSKY_SFC_LW_DWN'][i], ' Irradiance')

# for i in data['parameters']:
    
#     # datetime_object = datetime.strptime(i, '%yyyy%m%d%H')
#     print(i, ': ', data['parameters'][i]['longname'])

print(data['messages']) # error messages, cuz of api requesting.
 
 
file.close()

