import calendar
import datetime

class SiteCalendar:
	
	def __init__(self, htmlc = calendar.HTMLCalendar(), today = datetime.date.today()):
		self.htmlcalendar = htmlc
		self.today = today
	

	def getThisMonthHTMLCalendar(self):
		
		return self.htmlcalendar.formatmonth(self.today.year, self.today.month) 
