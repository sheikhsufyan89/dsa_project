# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys



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

class Ui_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        loadUi("RO.ui",self)
        self.genBtn.clicked.connect(self.generate)
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.tableWidget.setHidden(True)
        self.LogoutBtn.clicked.connect(self.logout)
        self.cap = self.findChild(QtWidgets.QLineEdit, 'ECap')
        self.enrollBtn = self.findChild(QtWidgets.QPushButton, 'enrollBtn')
        self.enrollBtn.clicked.connect(lambda: self.enroll(self.cap))
        self.enrollBtn.setProperty("enabled", False)
        # self.deleteBtn = self.findChild(QtWidgets.QPushButton, 'deleteBtn')
        # self.getBtn = self.findChild(QtWidgets.QPushButton, 'getBtn')
        # self.updateBtn = self.findChild(QtWidgets.QPushButton, 'updateBtn')
        # self.deleteBtn.clicked.connect(self.delete)
        # self.getBtn.clicked.connect(self.get)
        # self.updateBtn.clicked.connect(self.update)

    def logout(self):
        widget.setCurrentIndex(0)

    def delete(self):
        id = self.id.text()
        deleted_element = delete_element_heap(heap_tree,"Id", int(id))
        if deleted_element is not None:
            print("Deleted element:", deleted_element)
            print("Heap after deletion:")
            print_array(heap_tree)
            self.generate()
        else:
            print("Element not found in the heap")

    def get(self):
        id = self.id.text()
        retrieved_element = get_element_heap(heap_tree,"Id", int(id))
        if retrieved_element is not None:
            print("Retrieved element :", retrieved_element)
        else:
            print("Element not found in the heap")

    def update(self):
        id = self.id.text()
        name = self.name.text()
        year = self.year.text()
        school = self.school.text()
        success = update_element_heap(heap_tree,"Id",int(id), 1, name)
        success = update_element_heap(heap_tree,"Id",int(id), 2, int(year))
        success = update_element_heap(heap_tree,"Id",int(id), 3, school)
        if success:
            print("Updated element with new value:", name)
            print("Heap after update:")
            print_array(heap_tree)
            self.generate()
        else:
            print("Update failed.")

    def enroll(self, cap):
        if cap.text() == "":
            return
        cap = int(cap.text())
        if(cap > len(heap_tree)):
            print("Not enough students to enroll")
            return
        elif(cap <= 0):
            print("Invalid capacity")
            return
        else:
            self.tableWidget.setRowCount(0)
            for i in range(cap):
                self.tableWidget.insertRow(i)
                for j in range(1,5):
                    self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(heap_tree[i][j])))
            self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"])


    def generate(self):
        self.tableWidget.setRowCount(0)
        for i in range(len(heap_tree)):
            self.tableWidget.insertRow(i)
            for j in range(1,5):
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(heap_tree[i][j])))

        self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"])
        self.tableWidget.setHidden(False)
        self.enrollBtn.setProperty("enabled", True)
        
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
        widget.setCurrentIndex(4)
        
    pass

class TeacherLogin(QtWidgets.QDialog):
    def __init__(self):
        super(TeacherLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)

    def back(self):
        widget.setCurrentIndex(0)
        
        
    def login(self):
        widget.setCurrentIndex(4)
        
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
    student = StudentLogin()
    teacher = TeacherLogin()
    admin = AdminLogin()
    widget.addWidget(login)
    widget.addWidget(student)
    widget.addWidget(teacher)
    widget.addWidget(admin)
    widget.addWidget(ui)
    widget.setFixedWidth(500)
    widget.setFixedHeight(700)
    widget.show()
    sys.exit(app.exec_())