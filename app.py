from flask import Flask, render_template,jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(100), nullable=True)
    requirements = db.Column(db.String(200), nullable=False)
    recommendations = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Job('{self.title}', '{self.location}', '{self.salary}', '{self.requirements}', '{self.recommendations}')"

JOBS = [
    {'title': 'Data Analyst', 'location': 'Bengaluru, India', 'salary': 'Rs. 10,00,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'Python, SQL'},
    {'title': 'Data Scientist', 'location': 'Delhi, India', 'salary': None, 'requirements': 'Master\'s degree in Computer Science', 'recommendations': 'Python, Machine Learning'},
    {'title': 'Frontend Engineer', 'location': 'Remote', 'salary': '$120,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'JavaScript, React'},
    {'title': 'Backend Engineer', 'location': 'San Francisco, USA', 'salary': '$150,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'Python, Django'},
    {'title': 'Full Stack Engineer', 'location': 'New York, USA', 'salary': '$140,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'JavaScript, Python'},
    {'title': 'DevOps Engineer', 'location': 'London, UK', 'salary': '£80,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'AWS, Docker'},
    {'title': 'Product Manager', 'location': 'Bengaluru, India', 'salary': 'Rs. 15,00,000', 'requirements': 'MBA', 'recommendations': 'Product development, Marketing'},
    {'title': 'UX Designer', 'location': 'San Francisco, USA', 'salary': '$100,000', 'requirements': 'Bachelor\'s degree in Design', 'recommendations': 'Design thinking, Figma'},
    {'title': 'Software Engineer', 'location': 'Toronto, Canada', 'salary': '$90,000', 'requirements': 'Bachelor\'s degree in Computer Science', 'recommendations': 'Python, Java'},
    {'title': 'Technical Writer', 'location': 'Remote', 'salary': '$60,000', 'requirements': 'Bachelor\'s degree in English', 'recommendations': 'Technical writing, Documentation'}
]



@app.route('/')
def index():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Insert the job listings into the table
        for job in JOBS:
            new_job = Job(**job)
            db.session.add(new_job)
        db.session.commit()
    app.run(host='0.0.0.0', port=5000, debug=True)