[FireHose for mongoDB](#FireHose for mongoDB)

[FFT Jupyter Kernel Gateway](#FFT Jupyter Kernel Gateway)

# FireHose for mongoDB

## Purpose: 
Fetch mongodb data and post to the api server.
#
## Usage:
```
python NTUST_Motor_Vibration_Firehose_Para.py [-h] [-m MACHINE] [-d DATABASE]
                                              [-u USER] [-p PASSWORD]
                                              [-H HOST] [-c COLLECTION]
                                              [-e POSTFE] [-y POSTCLASSIFY]
                                              [-b BEGIN] [-n END]
                                              [-i INTERVAL]
```
### optional arguments:
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



# FFT Jupyter Kernel Gateway


## Purpose: 
jupyter kernel gateway compute FFT and post next the api server.

## Usage:
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