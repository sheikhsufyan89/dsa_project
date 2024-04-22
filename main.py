# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
import os
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


def insert_heap_tree(hT, val):
    tree_size = len(hT)
    if tree_size == 0:
        hT.append(val)
    else:
        hT.append(val)
        i = tree_size
        while i != 0 and hT[i][0] > hT[(i - 1) // 2][0]:
            hT[i], hT[(i - 1) // 2] = hT[(i - 1) // 2], hT[i]  
            i = (i - 1) // 2

def print_array(hT):
    for i in range(len(hT)):
        print(hT[i][0], hT[i][1], hT[i][2], hT[i][3], hT[i][4])






# data = [
#     (1, "John Smith", 101, "Freshman", "Engineering"),
#     (2, "Emma Johnson", 102, "Sophomore", "Humanities"),
#     (3, "Michael Brown", 103, "Junior", "Engineering"),
#     (4, "Sarah Lee", 104, "Senior", "Humanities"),
#     (1, "David Rodriguez", 105, "Freshman", "Engineering"),
#     (2, "Emily Wilson", 106, "Sophomore", "Engineering"),
#     (3, "Daniel Martinez", 107, "Junior", "Humanities"),
#     (4, "Sophia Anderson", 108, "Senior", "Engineering"),
#     (1, "James Thompson", 109, "Freshman", "Humanities"),
#     (2, "Olivia Garcia", 110, "Sophomore", "Engineering")
# ]

def makeheap():
    heap_tree = []
    fileInput = []
    fileData = []

    with open ("student_records.csv") as f :
        lines = f . readlines ()
        for line in lines :
            line = line . strip () # remove leading and trailing spaces
            tokens = line . split (",") # split the line into tokens
            fileInput . append ( tokens) # add the first token to the
        
    for i in range(1,len(fileInput)):
        fileInput[i][0] = int(fileInput[i][0])
        fileInput[i][2] = int(fileInput[i][2])
        fileData.append(tuple(fileInput[i]))


    for item in fileData:
        insert_heap_tree(heap_tree, item)
    
    return heap_tree

heap_tree = makeheap()
enrollment_cap = len(heap_tree)
enrolled_Ids = []
enrolled_Students = []

print("Heap after insertion:")

print(heap_tree)



#delete
def delete_element_heap(hT,col, val):
    basedOn = 1
    if col == "Id":
        basedOn = 2
    index = None
    for i in range(len(hT)):
        if hT[i][basedOn] == val:
            index = i
            break
    
    if index is None:
        print("Element not found in the heap")
        return None
    
    hT[index] = hT[-1]
    hT.pop()
    
    if index < len(hT):
        heapify_down(hT, index)
        heapify_up(hT, index)
    
    return val

def heapify_up(hT, i):
    parent = (i - 1) // 2
    if parent >= 0 and hT[i][0] > hT[parent][0]:
        hT[i], hT[parent] = hT[parent], hT[i]
        heapify_up(hT, parent)

def heapify_down(hT, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    largest = i

    if left_child < len(hT) and hT[left_child][0] > hT[largest][0]:
        largest = left_child

    if right_child < len(hT) and hT[right_child][0] > hT[largest][0]:
        largest = right_child

    if largest != i:
        hT[i], hT[largest] = hT[largest], hT[i]
        heapify_down(hT, largest)

# # Example usage:
# # Assuming heap_tree is already populated
# element_to_delete = 108  # Example element to delete
# deleted_element = delete_element_heap(heap_tree,"Id", element_to_delete)
# if deleted_element is not None:
#     print("Deleted element:", deleted_element)
#     print("Heap after deletion:")
#     print(heap_tree)



#get
def get_element_heap(hT,col,val):
    basedOn = 1
    if col == "Id":
        basedOn = 2
    index = None
    for i in range(len(hT)):
        if hT[i][basedOn] == val:
            index = i
            break
    
    if index is None:
        print("Element not found in the heap")
        return None
    
    return hT[index]

# # Example usage:
# # Assuming heap_tree is already populated
# el_to_get = 105  # Example index to retrieve
# retrieved_element = get_element_heap(heap_tree,"Id", el_to_get)
# if retrieved_element is not None:
#     print("Retrieved element :", retrieved_element)



#update
def update_element_heap(hT,col,val,update_col, new_value):
    basedOn = 1
    if col == "Id":
        basedOn = 2
    index = None
    for i in range(len(hT)):
        if hT[i][basedOn] == val:
            index = i
            break
    if index is None:
        print("Element not found in the heap")
        return None
    
    old_value = hT[index]
    updated_element = list(old_value)
    updated_element[update_col] = new_value
    hT[index] = tuple(updated_element)

    # If the new value is greater, perform heapify up, otherwise heapify down
    if hT[index][0] > old_value[0]:
        heapify_up(hT, index)
    else:
        heapify_down(hT, index)
    
    return True

# # Example usage:
# # Assuming heap_tree is already populated
# el_to_update = 105  # Example index to update
# new_value = "Updated Name"  # Example new value
# success = update_element_heap(heap_tree,"Id",el_to_update, 1, new_value)
# if success:
#     print("Updated element with new value:", new_value)
#     print("Heap after update:")
#     print(heap_tree)
# else:
#     print("Update failed.")

def enroll_stuTea():
    if 103 in enrolled_Ids:
        student.statusLbl.setText("Enrolled")
        student.statusLbl.setStyleSheet("color: green")
    else:
        student.statusLbl.setText("Not Enrolled")
        student.statusLbl.setStyleSheet("color: red")
        
    teacher.tablewidget.setRowCount(0)
    for i in range(len(enrolled_Students)):
        teacher.tablewidget.insertRow(i)
        for j in range(1,5):
            teacher.tablewidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(enrolled_Students[i][j])))

    teacher.IdTxt.setHidden(False)
    teacher.NameTxt.setHidden(False)
    teacher.YearTxt.setHidden(False)
    teacher.SchoolTxt.setHidden(False)

    teacher.label_3.setHidden(True)
    teacher.statusLbl.setHidden(True)

    pass

def gen_stuTea():
    student.statusLbl.setText("Pending")
    student.statusLbl.setStyleSheet("color: yellow")
    teacher.tablewidget.setRowCount(0)
    teacher.IdTxt.setHidden(True)
    teacher.NameTxt.setHidden(True)
    teacher.YearTxt.setHidden(True)
    teacher.SchoolTxt.setHidden(True)
    teacher.label_3.setHidden(False)
    teacher.statusLbl.setHidden(False)

    pass

class Ui_MainWindow(QtWidgets.QDialog):


    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        loadUi("RO.ui",self)
        self.genBtn.clicked.connect(self.generate)
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.tableWidget.setHidden(True)
        self.genBTn = self.findChild(QtWidgets.QPushButton, 'genBtn')
        self.LogoutBtn.clicked.connect(self.logout)
        self.cap = self.findChild(QtWidgets.QLineEdit, 'ECap')
        self.enrollBtn = self.findChild(QtWidgets.QPushButton, 'enrollBtn')
        self.enrollBtn.clicked.connect(lambda: self.enroll(self.cap))
        self.enrollBtn.setProperty("enabled", False)
        self.deleteBtn = self.findChild(QtWidgets.QPushButton, 'deleteBtn')
        self.addBtn = self.findChild(QtWidgets.QPushButton, 'addBtn')
        self.edit = self.findChild(QtWidgets.QPushButton, 'editBtn')
        self.deleteBtn.setHidden(True)
        self.addBtn.setHidden(True)
        self.edit.setHidden(True)
        self.deleteBtn.clicked.connect(self.delete)
        self.addBtn.clicked.connect(self.add)
        self.edit.clicked.connect(self.update)

    def logout(self):
        widget.setCurrentIndex(0)

    def add(self):
        inputDialog = QtWidgets.QInputDialog()
        name, ok = inputDialog.getText(self, 'Input Dialog', 'Enter name:' )
        if ok and name != "":
            id, ok = inputDialog.getText(self, 'Input Dialog', 'Enter id:')
            if id != "" and ok:
                item = get_element_heap(heap_tree,"Id", int(id))
            if ok and item is None:
                year, ok = inputDialog.getItem(self, 'Input Dialog', 'Select year:', ('Freshman', 'Sophomore', 'Junior', 'Senior'), 0, False)
                if ok and year is not None:
                    school, ok = inputDialog.getItem(self, 'Input Dialog', 'Select school:', ('Engineering', 'Humanities'), 0, False)
                    if ok and school is not None:
                        priority = 1
                        id = int(id)
                        if year == 'Freshman':
                            priority = 1
                        elif year == 'Sophomore':
                            priority = 2
                        elif year == 'Junior':
                            priority = 3
                        elif year == 'Senior':
                            priority = 4
                        insert_heap_tree(heap_tree, (priority, name, id, year, school))
                        print("Heap after insertion:")
                        print_array(heap_tree)
                        self.generate()


    def delete(self):
        id,ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter id:')
        if ok and id != "":
            deleted_element = delete_element_heap(heap_tree,"Id", int(id))
            if deleted_element is not None:
                print("Deleted element:", deleted_element)
                print("Heap after deletion:")
                print_array(heap_tree)
                self.generate()
            else:
                print("Element not found in the heap")


    def update(self):
        id, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter id:')
        if ok and id != "":
            item = get_element_heap(heap_tree,"Id", int(id))
            if item is None:
                print("Element not found in the heap")
                return
            updateCol, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select column to update:', ('Year', 'School'), 0, False)
            if ok and updateCol == 'School':
                new_value, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select new school:', ('Engineering', 'Humanities'), 0, False)
                if ok:
                    success = update_element_heap(heap_tree,"Id", int(id), 4, new_value)
                    if success:
                        print("Updated element with new value:", new_value)
                        print("Heap after update:")
                        print_array(heap_tree)
                        self.generate()
                    else:
                        print("Update failed.")
            elif ok and updateCol == 'Year':
                new_value, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select new year:', ('Freshman', 'Sophomore', 'Junior', 'Senior'), 0, False)
                if ok:
                    priority = 1
                    if new_value == 'Freshman':
                        priority = 1
                    elif new_value == 'Sophomore':
                        priority = 2
                    elif new_value == 'Junior':
                        priority = 3
                    elif new_value == 'Senior':
                        priority = 4
                    success = update_element_heap(heap_tree,"Id", int(id), 0, priority)
                    success = update_element_heap(heap_tree,"Id", int(id), 3, new_value)
                    if success:
                        print("Updated element with new value:", new_value)
                        print("Heap after update:")
                        print_array(heap_tree)
                        self.generate()
                    else:
                        print("Update failed.")


    def enroll_helper(self,cap):
        enrollment_cap = cap
        enrolled_Ids.clear()
        enrolled_Students.clear()
        self.tableWidget.setRowCount(0)
        for i in range(cap):
            max_element = heap_tree[0]
            self.tableWidget.insertRow(i)
            for j in range(1,5):
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(max_element[j])))
            enrolled_Ids.append(max_element[2])
            enrolled_Students.append(max_element)
            print("Max element:", max_element)
            # Remove the max element from the heap
            delete_element_heap(heap_tree, "Id", max_element[2])
        self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"])
        self.genBtn.setProperty("text", "Regenerate Table from Database")
        self.addBtn.setHidden(True)
        self.edit.setHidden(True)
        self.deleteBtn.setHidden(True)

        print("Enrolled students:")
        print(enrolled_Ids)
        print_array(enrolled_Students)
        print("Enrollment cap:", enrollment_cap)

        enroll_stuTea()

       
    def enroll(self, cap):
        print(heap_tree)
        if cap.text() == "":
            return
        cap = int(cap.text())
        if(cap > len(heap_tree)):
            cap = len(heap_tree)
            self.cap.setText(str(cap))
            self.enroll_helper(cap)
            self.enrollBtn.setProperty("enabled", False)
        elif(cap <= 0):
            print("Invalid capacity")
            return
        else:
            self.enroll_helper(cap)
            self.enrollBtn.setProperty("enabled", False)


    def generate(self):
        if self.genBtn.text() == "Regenerate Table from Database":
            for i in range(len(enrolled_Students)):
                insert_heap_tree(heap_tree, enrolled_Students[i])
        enrolled_Students.clear()
        enrolled_Ids.clear()
        gen_stuTea()

        self.tableWidget.setRowCount(0)
        for i in range(len(heap_tree)):
            self.tableWidget.insertRow(i)
            for j in range(1,5):
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(heap_tree[i][j])))

        self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"])
        self.genBtn.setProperty("text", "Generate Table from Database")
        self.tableWidget.setHidden(False)
        self.enrollBtn.setProperty("enabled", True)
        self.deleteBtn.setHidden(False)
        self.addBtn.setHidden(False)
        self.edit.setHidden(False)
        
class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login.ui",self)
        self.Student.clicked.connect(self.stu)
        self.Teacher.clicked.connect(self.teach)
        self.Admin.clicked.connect(self.admin)

    def stu(self):
        widget.setCurrentIndex(1)
    
    def teach(self):
        widget.setCurrentIndex(2)

    def admin(self):
        widget.setCurrentIndex(3)
        
    pass
        
class StudentLogin(QtWidgets.QDialog):
    def __init__(self):
        super(StudentLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)

    def back(self):
        widget.setCurrentIndex(0)
        
    def login(self):
        widget.setCurrentIndex(5)
        
    pass

class StudentWindow(QtWidgets.QDialog):
    def __init__(self):
        super(StudentWindow,self).__init__()
        loadUi("Student.ui",self)
        if len(enrolled_Ids) > 0 and 103 in enrolled_Ids:
            self.statusLbl = self.findChild(QtWidgets.QLabel, 'statusLbl')
            self.statusLbl.setText("Enrolled")
            self.statusLbl.setStyleSheet("color: green")
        elif len(enrolled_Ids) > 0 and 103 not in enrolled_Ids:
            self.statusLbl = self.findChild(QtWidgets.QLabel, 'statusLbl')
            self.statusLbl.setText("Not Enrolled")
            self.statusLbl.setStyleSheet("color: red")
        else:
            self.statusLbl = self.findChild(QtWidgets.QLabel, 'statusLbl')
            self.statusLbl.setText("Pending")
            self.statusLbl.setStyleSheet("color: yellow") 

        self.Logout = self.findChild(QtWidgets.QPushButton, 'LogoutBtn')
        self.Logout.clicked.connect(self.logout)
    
    def logout(self):
        widget.setCurrentIndex(0)
        

class TeacherLogin(QtWidgets.QDialog):
    def __init__(self):
        super(TeacherLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)
        

    def back(self):
        widget.setCurrentIndex(0)
        
        
    def login(self):
        widget.setCurrentIndex(6)
        
    pass

class TeacherWindow(QtWidgets.QDialog):
    def __init__(self):
        super(TeacherWindow,self).__init__()
        loadUi("Teacher.ui",self)
        self.Logout = self.findChild(QtWidgets.QPushButton, 'LogoutBtn')
        self.Logout.clicked.connect(self.logout)
        self.tablewidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.findBtn = self.findChild(QtWidgets.QPushButton, 'findBtn')
        self.findBtn.clicked.connect(self.get)
        self.IdTxt.setHidden(True)
        self.NameTxt.setHidden(True)
        self.YearTxt.setHidden(True)
        self.SchoolTxt.setHidden(True)


    def get(self):
        print("Get")
        if enrolled_Students != []:
            inputDialog = QtWidgets.QInputDialog()
            id, ok = inputDialog.getText(self, 'Input Dialog', 'Enter id:' )
            if ok and id != "":
                item = None
                for i in range(len(enrolled_Ids)):
                    if enrolled_Ids[i] == int(id):
                        item = enrolled_Students[i]
                if item is not None:
                    self.IdTxt.setHidden(False)
                    self.NameTxt.setHidden(False)
                    self.YearTxt.setHidden(False)
                    self.SchoolTxt.setHidden(False)
                    self.IdTxt.setText(str(item[2]))
                    self.NameTxt.setText(item[1])
                    self.YearTxt.setText(item[3])
                    self.SchoolTxt.setText(item[4])
                else:
                    print("Element not found in the heap")


    
    def logout(self):
        widget.setCurrentIndex(0)
        
    pass

class AdminLogin(QtWidgets.QDialog):
    def __init__(self):
        super(AdminLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)

    def back(self):
        widget.setCurrentIndex(0)
        
    def login(self):
        widget.setCurrentIndex(4)
        
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    ui = Ui_MainWindow()
    login = Login()
    studentLogin = StudentLogin()
    student = StudentWindow()
    teacher = TeacherWindow()
    teacherLogin = TeacherLogin()
    adminLogin = AdminLogin()
    widget.addWidget(login)
    widget.addWidget(studentLogin)
    widget.addWidget(teacherLogin)
    widget.addWidget(adminLogin)
    widget.addWidget(ui)
    widget.addWidget(student)
    widget.addWidget(teacher)
    widget.setFixedWidth(500)
    widget.setFixedHeight(700)
    widget.show()
    sys.exit(app.exec_())