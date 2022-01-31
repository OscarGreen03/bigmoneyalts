from flask import Flask
from flask import render_template
from flask import request
from flask import flash

from random import randint
import hashlib


app = Flask(__name__)

@app.route('/', methods=(['GET','POST']))
def initial():
    cashalt = ['money', 'currency', 'legaltender', 'coinage', 'silver', 'hardcash', 'capital', 'finances']
    bigalt = ['sizable', 'large', 'substantial', 'considerable', 'great', 'huge', 'immense', 'enormous', 'colossal',
              'mammoth']

    if request.method == 'POST':
        inputfield = request.form['title']
        inputfield = hashlib.md5(inputfield.encode('utf-8')).hexdigest()

        print(inputfield)
        if inputfield == "311354ef5c1a158fbf779f48bed47eed":
            name = bigalt[randint(0,len(bigalt))-1] + cashalt[randint(0,len(cashalt))-1]
        if inputfield == "d41d8cd98f00b204e9800998ecf8427e":
            name = ""
        else:
            name = "INTRUDER DETECTED RUNNING RAM DUMP"

    return render_template('namegen.html', name = name)