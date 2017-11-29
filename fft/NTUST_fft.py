"""
A first simple Cloud Foundry Flask app
"""
from flask import Flask, request, jsonify
import os
import requests
import pandas as pd
import numpy as np
import json

def do_fft(V1,V2,V3,I1,I2,I3):
    V1_fft = np.fft.fft(V1)
    list_V1 = []
    for a in V1_fft :
        b = (abs(a)*2)/len(V1_fft)
        list_V1.append(b)
    list_V1=list_V1[0:5000]

    V2_fft = np.fft.fft(V2)
    list_V2 = []
    for a in V2_fft :
        b = (abs(a)*2)/len(V2_fft)
        list_V2.append(b)
    list_V2=list_V2[0:5000]

    V3_fft = np.fft.fft(V3)
    list_V3 = []
    for a in V3_fft :
        b = (abs(a)*2)/len(V3_fft)
        list_V3.append(b)
    list_V3 = list_V3[0:5000]

    I1_fft = np.fft.fft(I1)
    list_I1 = []
    for a in I1_fft :
        list_I1.append(abs(a))
    list_I1=list_I1[0:5000]
    
    I2_fft = np.fft.fft(I2)
    list_I2 = []
    for a in I2_fft :
        list_I2.append(abs(a))
    list_I2=list_I2[0:5000]
    
    I3_fft = np.fft.fft(I3)
    list_I3 = []
    for a in I3_fft :
        list_I3.append(abs(a))
    list_I3=list_I3[0:5000]
    
    return list_V1,list_V2,list_V3,list_I1,list_I2,list_I3


app = Flask(__name__)

# Get port from environment variable or choose 9090 as local default
port = int(os.getenv("PORT", 6666))

@app.route('/', methods=['POST'])
def hello_world():
    #arr = request.json['QSEND_NO']

    classifier_post_url = "http://cf-json-matching.iii-cflab.com/feature_post"

    #request = json.loads(REQUEST)
    #request_data = request['body']

    request_data = request.json

    key_list = ['V1', 'V2', 'V3', 'I1', 'I2', 'I3']
    return_key_list = ['list_V1', 'list_V2', 'list_V3' ,'list_I1', 'list_I2' ,'list_I3']
    data_dict = {}
    result_dict = {}

    for key in key_list:
        data_dict[key] = request_data[key]

    r = do_fft(data_dict[key_list[0]], data_dict[key_list[1]], data_dict[key_list[2]], data_dict[key_list[3]], data_dict[key_list[4]], data_dict[key_list[5]])
    for num in range(len(return_key_list)):
        result_dict[return_key_list[num]] = r[num]

    result_dict['Time'] = int(request_data['Time'])
    result_dict['Machine_ID'] = request_data['Machine_ID']

    try:
        r = requests.post(classifier_post_url, json=result_dict)
    except Exception as e:
        error = True
        exc = {'exc': str(e)}
        print(json.dumps(exc))
        return jsonify({'statuscode':400}), 400
    else:
        error = False
        #print(json.dumps({'text': r.text, 'request': str(r.request.headers), 'resp': result_dict, 'status': r.status_code}))
    # print(r.status_code)

    #return jsonify({'statuscode':500}), 500
    return jsonify({'statuscode':200}), 200


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)



