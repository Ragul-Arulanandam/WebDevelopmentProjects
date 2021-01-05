from flask import Flask,request,render_template,url_for,redirect
import json
from forms import Dataform
from calculator import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '318e2013cc0b3183eff7e57e112c888e'


@app.route('/',methods=['POST','GET'])
def homepage():
    form = Dataform()
    ans = request.form.get('comp-select')
    print(ans)
    a=form.input1.data
    b=form.input2.data
    print(a,b)
    t = calculator(a,b)
    data=1
    try:
        if (ans =="Addition"):
            data = t.sum()
        elif (ans == "Subraction"):
            data =t.sub()

        elif (ans == "Multiplication"):
            data = t.mul()
        elif (ans == "Division"):
            data =t.div()
    except:
        data = "Enter valid Inputs"
    return render_template('home.html',form=form,title='Home',final1=data)

app.run(debug=True)