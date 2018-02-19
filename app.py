#!/bin/env/python
# coding: utf-8

app = Flask(__name__)

@app.route('/')
def index(user):
  return render_template('index.html', 'Hello')

if __name__ == "__main__":
  port = 8000
  app.debug = True
  app.run(host='0.0.0.0', port=port)
