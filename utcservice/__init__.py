#!/usr/bin/env python3

from flask import Flask, request
import dateparser

app = Flask('utcservice')

@app.route("/")
def parse_date():
    return dateparser.parse(request.args.get('date', '')).isoformat(u'T', 'seconds')

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
