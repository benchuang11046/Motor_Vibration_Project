

There are three application in this project.

*   FireHose for mongoDB
*   FFT Flask
*   FFT Jupyter Kernel Gateway


# FireHose for mongoDB

## Purpose: 
Fetch mongodb data and post to the api server.
#
## Usage:

### Execute directely

```
python NTUST_Motor_Vibration_Firehose_Para.py [-h] [-m MACHINE] [-d DATABASE]
                                              [-u USER] [-p PASSWORD]
                                              [-H HOST] [-c COLLECTION]
                                              [-e POSTFE] [-y POSTCLASSIFY]
                                              [-b BEGIN] [-n END]
                                              [-i INTERVAL]
```


#### optional arguments:
```
  -h, --help            show this help message and exit
  -m MACHINE, --machine MACHINE
                        Machine ID list split by comma
  -d DATABASE, --database DATABASE
                        MongoDB database name
  -u USER, --user USER  MongoDB user name
  -p PASSWORD, --password PASSWORD
                        MongoDB password
  -H HOST, --host HOST  MongoDB host
  -c COLLECTION, --collection COLLECTION
                        MongoDB collection name
  -e POSTFE, --postfe POSTFE
                        Post feature extraction post url
  -y POSTCLASSIFY, --postclassify POSTCLASSIFY
                        Post classifier post url
  -b BEGIN, --begin BEGIN
                        Begin timestamp
  -n END, --end END     End timestamp
  -i INTERVAL, --interval INTERVAL
                        Send time interval (second)
```

### Zip and Push to cf
```
zip NTUST_Motor_Vibration_Firehose NTUST_Motor_Vibration_Firehose_Para.py Procfile requirements.txt logging.ini manifest.yml
```

# FFT Flask 

## Purpose: 
Flask compute FFT and post next the api server.

## Program Path
In directory [fft/](https://github.com/benchuang11046/Motor_Vibration_Project/tree/master/fft)

## Usage:

### Execute directely
```
python  NTUST_fft.py
```

### Zip and Push to cf
```
zip fft .fft/*
```

### API content 
```
URI: https://532735e7-98aa-4aea-a93b-8ad3d84f4eec-NTUST-Motor-FFT-dev.iii-cflab.com
Method: POST
POST body:
{
	"Machine_ID": "A",
	"Time": "0",
	"V1": [10, 10, 10, 10],
	"V2": [10, 10, 10, 10],
	"V3": [10, 10, 10, 10],
	"I1": [10, 10, 10, 10],
	"I2": [10, 10, 10, 10],
	"I3": [10, 10, 10, 10],
	"A1": [10, 10, 10, 10],
	"A2": [10, 10, 10, 10],
	"A3": [10, 10, 10, 10]
}
```



# FFT Jupyter Kernel Gateway 

## Purpose: 
Jupyter kernel gateway compute FFT and post next the api server.
(ISSUE: hanged in 30 minutes on CF)

## Usage:

### Execute directely
```
 jupyter-kernelgateway --KernelGatewayApp.port=9090 --KernelGatewayApp.ip='0.0.0.0' --KernelGatewayApp.api=notebook-http --KernelGatewayApp.seed_uri='NTUST_Motor_Vibration_FFT.ipynb' --NotebookHTTPPersonality.static_path='./results'
 ```
 
### API content 
```
URI: https://532735e7-98aa-4aea-a93b-8ad3d84f4eec-NTUST-Motor-FFT-dev.iii-cflab.com
Method: POST
POST body:
{
	"Machine_ID": "A",
	"Time": "0",
	"V1": [10, 10, 10, 10],
	"V2": [10, 10, 10, 10],
	"V3": [10, 10, 10, 10],
	"I1": [10, 10, 10, 10],
	"I2": [10, 10, 10, 10],
	"I3": [10, 10, 10, 10],
	"A1": [10, 10, 10, 10],
	"A2": [10, 10, 10, 10],
	"A3": [10, 10, 10, 10]
}
```
