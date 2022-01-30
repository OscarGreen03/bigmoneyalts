from flask import Flask
from flask import render_template
from flask import request
from random import randint
app = Flask(__name__)

@app.route('/', methods=(['GET','POST']))
def initial():
    cashalt = ['money', 'currency', 'legaltender', 'coinage', 'silver', 'hardcash', 'capital', 'finances']
    bigalt = ['sizable', 'large', 'substantial', 'considerable', 'great', 'huge', 'immense', 'enormous', 'colossal',
              'mammoth']

    if request.method == 'POST':
        name = bigalt[randint(0,len(bigalt))-1] + cashalt[randint(0,len(cashalt))-1]
        print(name)



    return render_template('namegen.html', name = name)