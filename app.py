#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

import gdata.spreadsheet.service
import gdata.docs.service

import json
with open("GoogleAppPw.json") as fh:
    config = json.load(fh)

# Create connection object
client = gdata.spreadsheet.service.SpreadsheetsService()

# Login using credentials
client.ClientLogin(config['rossinyolks@gmail.com'], config['9585520Valencia'])

# List all spreadsheets
documents_feed = client.GetSpreadsheetsFeed()
for document_entry in documents_feed.entry:
    print document_entry.title.text

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):

    speech = "aaa"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "test-sales-322-Open-app-More-"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
