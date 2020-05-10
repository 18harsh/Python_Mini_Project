import sys
import os
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QPixmap,QFont
from PIL import Image

con = sqlite3.connect("employee.db")
cur = con.cursor()
defaultImg="insert.jpg"
person_id = None

class Main(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My Employees")
		self.setGeometry(450,100,750,600)
		self.UI()
		self.show()

	def UI(self):
		self.mainDesign()
		self.layouts()
		self.getEmployees()
		self.displayfirstrecord()
	def mainDesign(self):
		self.setStyleSheet("font-size:14pt;font-family:Arial Bold;")
		self.employeeList=QListWidget()
		self.employeeList.itemClicked.connect(self.singleclick)
		self.btnNew=QPushButton("New")
		self.btnNew.clicked.connect(self.functnew)
		self.btnUpdate=QPushButton("Update")
		self.btnUpdate.clicked.connect(self.functupdate)
		self.btnDelete=QPushButton("Delete")
		self.btnDelete.clicked.connect(self.functdelete)

	def layouts(self):
		self.mainLayout = QHBoxLayout()
		self.leftLayout = QFormLayout()
		self.rightMainLayout = QVBoxLayout()
		self.rightTopLayout = QHBoxLayout()
		self.rightBottomLayout=QHBoxLayout()

		self.rightMainLayout.addLayout(self.rightTopLayout)
		self.rightMainLayout.addLayout(self.rightBottomLayout)
		self.mainLayout.addLayout(self.leftLayout,40)
		self.mainLayout.addLayout(self.rightMainLayout,60)

		self.rightTopLayout.addWidget(self.employeeList)
		self.rightBottomLayout.addWidget(self.btnNew)
		self.rightBottomLayout.addWidget(self.btnUpdate)
		self.rightBottomLayout.addWidget(self.btnDelete)

		self.setLayout(self.mainLayout)

	def functnew(self):
		self.newemployee=AddEmployee()
		self.close()
	def getEmployees(self):
		query = "SELECT id,Name,Surname From employees"
		employees=cur.execute(query).fetchall()
		for employee in employees:
			self.employeeList.addItem(str(employee[0])+"-"+employee[1]+" "+employee[2])
	def displayfirstrecord(self):		
		query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
		employee = cur.execute(query).fetchone()
		img = QLabel()
		img.setPixmap(QPixmap("Images\\"+employee[5]))
		name = QLabel(employee[1])
		surname = QLabel(employee[2])
		phone = QLabel(employee[3])
		email = QLabel(employee[4])
		address=QLabel(employee[6])
		self.leftLayout.setVerticalSpacing(20)
		self.leftLayout.addRow("",img)
		self.leftLayout.addRow("Name :",name)
		self.leftLayout.addRow("Surname :",surname)
		self.leftLayout.addRow("Phone :",phone)
		self.leftLayout.addRow("Email",email)
		self.leftLayout.addRow("Address :",address)		
	def singleclick(self):
		for i in reversed(range(self.leftLayout.count())):
			widget = self.leftLayout.takeAt(i).widget()
			if widget is not None:
				widget.deleteLater()
				
		employee=self.employeeList.currentItem().text()
		id=employee.split("-")[0]	
		query = ("SELECT * FROM employees WHERE id=?")
		person=cur.execute(query,(id)).fetchone()
		img = QLabel()
		print(person)
		img.setPixmap(QPixmap("Images\\"+person[5]))
		name = QLabel(person[1])
		surname = QLabel(person[2])
		phone = QLabel(person[3])
		email = QLabel(person[4])
		address=QLabel(person[6])
		self.leftLayout.setVerticalSpacing(20)
		self.leftLayout.addRow("",img)
		self.leftLayout.addRow("Name :",name)
		self.leftLayout.addRow("Surname :",surname)
		self.leftLayout.addRow("Phone :",phone)
		self.leftLayout.addRow("Email",email)
		self.leftLayout.addRow("Address :",address)	
	def functupdate(self):
		global person_id
		if self.employeeList.currentItem():
			employee=self.employeeList.currentItem().text()
			person_id=employee.split("-")[0]
			self.updateemployee=UpdateEmployee()
			self.close()

	def functdelete(self):
		employee=self.employeeList.currentItem().text()
		id=employee.split("-")[0]
		mbox = QMessageBox.warning(self,"Warning","Are you sure, you want to delete?",QMessageBox.Yes|QMessageBox.No)
		if mbox  == QMessageBox.Yes:
			try:
				cur.execute("DELETE FROM employees WHERE id=?",(id,))
				con.commit()
				QMessageBox.information(self,"success","Employee deleted!")
			except:	
				QMessageBox.information(self,"Warning","Select employee")
		else:
			QMessageBox.information(self,"Warning","Employee has not been deleted")		
		self.close()
		self.main=Main()	

class UpdateEmployee(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Update Employee")
		self.setGeometry(450,100,350,600)
		self.UI()
		self.show()

	def UI(self):
		self.getPerson()
		self.mainDesign()
		self.layouts()
	def getPerson(self):
		global person_id
		query = ("SELECT * FROM employees WHERE id=?")
		print(person_id)
		person=cur.execute(query,(person_id)).fetchone()
		self.name = (person[1])
		self.surname = (person[2])
		self.phone = (person[3])
		self.email = (person[4])
		self.address=(person[6])
		self.img = person[5]	

	def mainDesign(self):
		self.imgname = None
		self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
		self.title = QLabel("Update Person")
		self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
		self.imgAdd = QLabel()
		self.imgAdd.setPixmap(QPixmap("Images\\"+self.img))
		self.namelabel=QLabel("Name :")
		self.nameEntry = QLineEdit()
		self.nameEntry.setText(self.name)

		self.surnamelabel=QLabel("Surname :")
		self.surnameEntry = QLineEdit()
		self.surnameEntry.setText(self.surname)

		self.phonelabel=QLabel("Phone :")
		self.phoneEntry = QLineEdit()
		self.phoneEntry.setText(self.phone)

		self.emaillabel=QLabel("Email :")
		self.emailEntry = QLineEdit()
		self.emailEntry.setText(self.email)

		self.imglabel=QLabel("Picture :")
		self.imgbutton = QPushButton("Browse")
		self.imgbutton.setStyleSheet("background-color:orange;font-size:10pt")
		self.imgbutton.clicked.connect(self.uploadimg)
		self.addresslabel=QLabel("Address :")
		self.addressEntry = QTextEdit()
		self.addressEntry.setText(self.address)
	
		self.upbutton = QPushButton("Update")
		self.upbutton.setStyleSheet("background-color:orange;font-size:10pt")
			
		self.upbutton.clicked.connect(self.upemployee)
	def layouts(self):
		self.mainLayout= QVBoxLayout()
		self.toplayout = QVBoxLayout()
		self.bottomlayout = QFormLayout()

		self.mainLayout.addLayout(self.toplayout)
		self.mainLayout.addLayout(self.bottomlayout)

		self.toplayout.addStretch()
		self.toplayout.addWidget(self.title)
		self.toplayout.addWidget(self.imgAdd)
		self.toplayout.addStretch()
		self.toplayout.setContentsMargins(110,20,10,30)
		self.bottomlayout.addRow(self.namelabel,self.nameEntry)
		self.bottomlayout.addRow(self.surnamelabel,self.surnameEntry)
		self.bottomlayout.addRow(self.phonelabel,self.phoneEntry)
		self.bottomlayout.addRow(self.emaillabel,self.emailEntry)
		self.bottomlayout.addRow(self.imglabel,self.imgbutton)
		self.bottomlayout.addRow(self.addresslabel,self.addressEntry)
		self.bottomlayout.addRow("",self.upbutton)

		self.setLayout(self.mainLayout)			

	def uploadimg(self):
		global defaultImg
		size = (128,128)
		self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files(*.jpg *.png)")		
		name = self.nameEntry.text()
		surname = self.surnameEntry.text()
		if name and surname  !="":	
			if ok:
				newname, file_extension = os.path.splitext(self.filename)
				self.newname = name+surname+file_extension
				self.imgname = self.newname
				img = Image.open(self.filename)
				img = img.resize(size)
				img.save("Images\\{}".format(self.newname))
				self.imgAdd.setPixmap(QPixmap(self.filename))
				# print(self.filename)
			else:
				self.newname = defaultImg
				self.imgAdd.setPixmap(QPixmap("Images\\"+defaultImg))	
		else:
			QMessageBox.information(self,"Warning","Field cannot be empty")				
	def upemployee(self):
		global defaultImg,person_id
		name = self.nameEntry.text()
		surname = self.surnameEntry.text()
		phone = self.phoneEntry.text()
		email = self.emailEntry.text()
		if self.imgname == None:
			img = defaultImg
		else:
			img = self.imgname	
		address = self.addressEntry.toPlainText()
		if (name and surname and phone!=""):
			try:
				query = "UPDATE employees SET Name=?,Surname=?,Phone=?,Email=?,Img=?,Address=? WHERE id=?"
				cur.execute(query,(name,surname,phone,email,img,address,person_id))
				con.commit()
				QMessageBox.information(self,"Success","Person has been Updated")
				self.imgname = None
				person_id = None
				self.close()
				self.main=Main()
			except:
				QMessageBox.information(self,"Warning","Person has not been updated")	
		else:
			QMessageBox.information(self,"Warning","Field cannot be empty")		
	
	def closeEvent(self,event):
			global person_id
			self.imgname = None
			person_id = None
			self.main=Main()


class AddEmployee(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Add Employees")
		self.setGeometry(450,100,350,600)
		self.UI()
		self.show()

	def UI(self):
		self.mainDesign()
		self.layouts()

	def mainDesign(self):
		self.imgname = None
		self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
		self.title = QLabel("Add Person")
		self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
		self.imgAdd = QLabel()
		self.imgAdd.setPixmap(QPixmap("Images\\insert.jpg"))
		self.namelabel=QLabel("Name :")
		self.nameEntry = QLineEdit()
		self.nameEntry.setPlaceholderText("Enter Employees Name")

		self.surnamelabel=QLabel("Surname :")
		self.surnameEntry = QLineEdit()
		self.surnameEntry.setPlaceholderText("Enter Employees Surname")

		self.phonelabel=QLabel("Phone :")
		self.phoneEntry = QLineEdit()
		self.phoneEntry.setPlaceholderText("Enter Employees phone")

		self.emaillabel=QLabel("Email :")
		self.emailEntry = QLineEdit()
		self.emailEntry.setPlaceholderText("Enter Employees email")

		self.imglabel=QLabel("Picture :")
		self.imgbutton = QPushButton("Browse")
		self.imgbutton.setStyleSheet("background-color:orange;font-size:10pt")
		self.imgbutton.clicked.connect(self.uploadimg)
		self.addresslabel=QLabel("Address :")
		self.addressEntry = QTextEdit()
		
		self.addbutton = QPushButton("Add")
		self.addbutton.setStyleSheet("background-color:orange;font-size:10pt")
		self.addbutton.clicked.connect(self.addemployee)
	def layouts(self):
		self.mainLayout= QVBoxLayout()
		self.toplayout = QVBoxLayout()
		self.bottomlayout = QFormLayout()

		self.mainLayout.addLayout(self.toplayout)
		self.mainLayout.addLayout(self.bottomlayout)

		self.toplayout.addStretch()
		self.toplayout.addWidget(self.title)
		self.toplayout.addWidget(self.imgAdd)
		self.toplayout.addStretch()
		self.toplayout.setContentsMargins(110,20,10,30)
		self.bottomlayout.addRow(self.namelabel,self.nameEntry)
		self.bottomlayout.addRow(self.surnamelabel,self.surnameEntry)
		self.bottomlayout.addRow(self.phonelabel,self.phoneEntry)
		self.bottomlayout.addRow(self.emaillabel,self.emailEntry)
		self.bottomlayout.addRow(self.imglabel,self.imgbutton)
		self.bottomlayout.addRow(self.addresslabel,self.addressEntry)
		self.bottomlayout.addRow("",self.addbutton)

		self.setLayout(self.mainLayout)			

	def uploadimg(self):
		global defaultImg
		size = (128,128)
		self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files(*.jpg *.png)")		
		name = self.nameEntry.text()
		surname = self.surnameEntry.text()
		if name and surname  !="":	
			if ok:
				newname, file_extension = os.path.splitext(self.filename)
				self.newname = name+surname+file_extension
				self.imgname = self.newname
				img = Image.open(self.filename)
				img = img.resize(size)
				img.save("Images\\{}".format(self.newname))
				self.imgAdd.setPixmap(QPixmap(self.filename))
				# print(self.filename)
			else:
				self.newname = defaultImg
				self.imgAdd.setPixmap(QPixmap("Images\\"+defaultImg))	
		else:
			QMessageBox.information(self,"Warning","Field cannot be empty")				
	def addemployee(self):
		global defaultImg
		name = self.nameEntry.text()
		surname = self.surnameEntry.text()
		phone = self.phoneEntry.text()
		email = self.emailEntry.text()
		if self.imgname == None:
			img = defaultImg
		else:
			img = self.imgname	
		address = self.addressEntry.toPlainText()
		if (name and surname and phone!=""):
			try:
				query = "INSERT INTO employees(Name,Surname,Phone,Email,Img,Address) VALUES(?,?,?,?,?,?)"
				cur.execute(query,(name,surname,phone,email,img,address))
				con.commit()
				QMessageBox.information(self,"Success","Person has been added")
				self.imgname = None
				self.close()
				self.main=Main()
			except:
				QMessageBox.information(self,"Warning","Person has not been added")	
		else:
			QMessageBox.information(self,"Warning","Field cannot be empty")		
	def closeEvent(self,event):
			self.imgname = None
			self.main=Main()		


def main():
	APP =QApplication(sys.argv)
	window=Main()
	sys.exit(APP.exec_())
if __name__ == "__main__":
	main()		