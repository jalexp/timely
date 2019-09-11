"""
This application prints Hello World to the browser
@
"""
from flask import Flask, render_template
from sitecalendar import SiteCalendar
from htmlcalendarparser import HTMLCalendarParser
from flask_sqlalchemy import SQLAlchemy

#create an object instance of the Flask class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flaskapp.db'

db = SQLAlchemy(app)

model = "Habibti"

sc_model = HTMLCalendarParser(SiteCalendar().getThisMonthHTMLCalendar()).getHTMLString()


#this decorator creates our first View
#Python MVC terminology View, Controller differ slightly
@app.route('/')
#similar to Spring, the decorator allows our index function
#to route to the base url 'https://app1/
def base():
	return render_template('base.html')


@app.route('/result')
def result():
	return render_template('result.html', model = model)

@app.route('/schedule')
def schedule():
	return render_template('schedule.html', model = sc_model)

@app.route('/schedule/add-emp', methods=["POST"])
def add_employee():
	return "Employee Added"




if __name__ == '__main__':
	app.run(host='0.0.0.0')
