from flask import Flask, request
import requests
import json
app = Flask(__name__)

def getForwardHeaders(request):
    headers = {}

    incoming_headers = [ 'me', 
                         'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers


@app.route('/info')
def hello_world():
    v1 = requests.get("http://counter/counter", headers=getForwardHeaders(request))
    rv1 = v1.json()
    v2 = requests.get("http://date/date", headers=getForwardHeaders(request))
    rv2 = v2.json()
    return json.dumps({"counter":rv1["counter"], "date": rv2["date"]}), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0")
