from html.parser import HTMLParser
from bs4 import BeautifulSoup

class HTMLCalendarParser():

	def __init__(self, html):
		self.soup = BeautifulSoup(html)
		self.setTableAttribute(0,0)
		#self.addEmployeeButton(None)
		self.init_searchbox()
		#self.add_rows()
	def setTableAttribute(self,att, val):
		t = self.soup.table
		t['style'] = 'position: absolute; height: 100%; width: 100%; top:0; bottom: 0; left: 0; right: 0;'

	def getHTMLString(self):
		return self.soup

	#Add proper MVC architecture later
	#def addEmployee(self, employee, datecell):
#
#Demonstrates how to change str content of cells 
#	def addEmployeeButton(self, name):
#
#		for child in self.soup.table.descendants:
#			if (str(child.string) == 'Mon'):
#				child.string.replace_with("MONDAY")
	def init_searchbox(self):
		#self.soup.table.tr.th['colspan'] = 7
		
		cell = self.soup.new_tag('td')
		textbox = self.soup.new_tag('input', type='text', id='empsearch', list="emps")
		datalist = self.soup.new_tag('datalist', id='emps')
		btn = self.soup.new_tag('button',type='button', id='empsubmit')
		btn['class'] = 'btn btn-info'
		textbox['placeholder'] = 'Search for...'
		btn.string = 'Add Employee'
		new_row = self.soup.new_tag("tr")
		new_cell = self.soup.new_tag('td')
		self.soup.table.tr.insert_after(new_row)
		#self.soup.table.new_row.append(btn)
		#self.soup.table.new_row.append(textbox)
		#self.soup.table.tr.insert_after('th',(cell.append(textbox.append(btn))))
		rows = self.soup.find_all('tr')
		rows[1].append(new_cell)
		rows[1].td.append(btn)
		rows[1].td.append(textbox)	
		rows[1].td['colspan'] = 7
