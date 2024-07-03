from flask import Flask, json, render_template,jsonify 

app = Flask(__name__)  

JOBS =[{
    'id':1,
    'title':'Data Analyst', 
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
},
{
    'id': 2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    
},
{    
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'$120,000'

},
{
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$150,000'
    
}
      ]

@app.route('/')
def index():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app. run (host='0.0.0.0', debug=True)