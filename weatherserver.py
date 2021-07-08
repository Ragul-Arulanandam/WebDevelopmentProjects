from flask import Flask,request,render_template,url_for,redirect
import urllib.request
import json
from forms import SearchForm


app=Flask(__name__)
app.config['SECRET_KEY'] = '318e2013cc0b3183eff7e57e112c888e'



@app.route('/',methods=['POST','GET'])
def homepage():
    form= SearchForm()
    if form.validate_on_submit():
        return weatherdata(form.countryname.data)
    return render_template('home.html', form =form,title='Home')

def weatherdata(city):
    api = "7fccc77ed9c1f1f56366a13535f46ddd"
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city + '&appid=' + api + '&units=metric'
    
    source = urllib.request.urlopen(url).read()
    dataslist = json.loads(source)
    data = {
        "CITY": city,
        "SUN RISE": str(dataslist['sys']['sunrise']),
        "COUNTRY CODE": str(dataslist['sys']['country']),
        "COORDINATES": str(dataslist['coord']['lon']) + ' '
        + str(dataslist['coord']['lat']),
        "TEMPERATURE": str(dataslist['main']['temp']) + ' °C',
        "MAX TEMPERATURE": str(dataslist['main']['temp_max']) + ' °C',
        "MIN TEMPERATURE": str(dataslist['main']['temp_min']) + ' °C',
        "PRESSURE": str(dataslist['main']['pressure']),
        "HUMITIDY": str(dataslist['main']['humidity']),
        "VISIBILITY": str(dataslist['visibility']),
        "TIMEZONE": str(dataslist['timezone']),
        
    }
   
    return render_template('submit.html',data=data,title=city)

app.run(debug=True)

