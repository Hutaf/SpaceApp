'''
*Version: 2.0 Published: 2021/03/09* Source: [NASA POWER](https://power.larc.nasa.gov/)
POWER API Multi-Point Download
This is an overview of the process to request data from multiple data points from the POWER API.
'''

import os, sys, time, json, urllib3, requests, multiprocessing

urllib3.disable_warnings()

def download_function(collection):
    ''' '''

    request, filepath = collection
    response = requests.get(url=request, verify=False, timeout=30.00).json()

    with open(filepath, 'w') as file_object:
        json.dump(response, file_object)

class Process():

    def __init__(self):

        self.processes = 5 # Please do not go more than five concurrent requests.

        self.request_template =\
             r"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=WS10M,WD10M,T2MDEW,T2MWET,T2M,V10M,RH2M,PS,PRECTOT,QV2M,ALLSKY_SFC_LW_DWN,CLRSKY_SFC_LW_DWN,SZA,ALLSKY_KT,ALLSKY_SRF_ALB,ALLSKY_SFC_PAR_TOT,ALLSKY_SFC_PAR_TOT,ALLSKY_SFC_UVA,ALLSKY_SFC_UVB,ALLSKY_SFC_UV_INDEX&community=SB&longitude={longitude}&latitude={latitude}&start=20190101&end=20210331&format=JSON"
        self.filename_template = "User_Lat_{latitude}_Lon_{longitude}.json"

        self.messages = []
        self.times = {}

    def execute(self):

        Start_Time = time.time()

        locations = [(24.763990, 46.640249)]

        requests = []
        for latitude, longitude in locations:
            request = self.request_template.format(latitude=latitude, longitude=longitude)
            filename = self.filename_template.format(latitude=latitude, longitude=longitude)
            requests.append((request, filename))

        requests_total = len(requests)

        pool = multiprocessing.Pool(self.processes)
        x = pool.imap_unordered(download_function, requests)

        for i, df in enumerate(x, 1):
            sys.stderr.write('\rExporting {0:%}'.format(i/requests_total))

        self.times["Total Script"] = round((time.time() - Start_Time), 2)

        print ("\n")
        print ("Total Script Time:", self.times["Total Script"])

if __name__ == '__main__':
    Process().execute()