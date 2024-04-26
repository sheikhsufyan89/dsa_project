from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
import os
os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'




LoginIds = {"Admin": "admin", "Teacher": "teacher"} # Login Ids for students, admin and teacher

FileName = "student_records.csv" # File name for student records




def heapify_up(hT, i): # Function to heapify up
    parent = (i - 1) // 2 # Calculate the parent index
    if parent >= 0 and hT[i][0] > hT[parent][0]: # If the value is greater than its parent
        hT[i], hT[parent] = hT[parent], hT[i] # Swap the value with its parent
        heapify_up(hT, parent) # Recursively call heapify up

def heapify_down(hT, i): # Function to heapify down
    left_child = 2 * i + 1 # Calculate the left child index
    right_child = 2 * i + 2 # Calculate the right child index
    largest = i # Initialize largest to i

    if left_child < len(hT) and hT[left_child][0] > hT[largest][0]: # If the left child is greater than the largest
        largest = left_child # Set largest to left child

    if right_child < len(hT) and hT[right_child][0] > hT[largest][0]: # If the right child is greater than the largest
        largest = right_child # Set largest to right child

    if largest != i: # If largest is not i
        hT[i], hT[largest] = hT[largest], hT[i] # Swap the value with the largest
        heapify_down(hT, largest) # Recursively call heapify down

def search(heap,value):
        print("Inorder Traversal:")
        output = []
        return (search_recursive(heap,0,value,output),output)

def search_recursive(heap, index,value,output):
    if index >= len(heap):
        return False

    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2

    if int(heap[index][2]) == value:
        output.append((heap[index],index))
        return True

    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2

    return search_recursive(heap, left_child_index,value,output) or search_recursive(heap, right_child_index,value,output)







def insert_heap_tree(hT, val):  # hT is the heap tree, val is the value to be inserted
    tree_size = len(hT)
    if tree_size == 0: # If the heap tree is empty, insert the value at the root
        hT.append(val)
    else:
        hT.append(val)
        heapify_up(hT, len(hT)-1) # Perform heapify up
        # i = tree_size
        # while i != 0 and hT[i][0] > hT[(i - 1) // 2][0]: # If the value is greater than its parent, swap the value with its parent
        #     hT[i], hT[(i - 1) // 2] = hT[(i - 1) // 2], hT[i]   # Swap the value with its parent
        #     i = (i - 1) // 2 # Move to the parent index

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

def makeheap(FileName = "student_records.csv"): # Function to create a heap tree from the data
    heapTree = []
    fileInput = []
    fileData = []

    with open (FileName) as f :
        lines = f . readlines ()
        for line in lines :
            line = line . strip () # remove leading and trailing spaces
            tokens = line . split (",") # split the line into tokens
            fileInput . append ( tokens) # add the first token to the
         
    for i in range(1,len(fileInput)): # Skip the first line as it contains the column names
        LoginIds[fileInput[i][2]] = fileInput[i][1] # Add the student name and id to the LoginIds dictionary
        fileInput[i][0] = int(fileInput[i][0]) # Convert the priority to an integer
        fileInput[i][2] = int(fileInput[i][2]) # Convert the id to an integer
        fileData.append(tuple(fileInput[i])) # Append the tuple to the fileData list


    for item in fileData:
        insert_heap_tree(heapTree, item) # Insert the item into the heap tree
    
    return heapTree

permaHeap = makeheap()
heap_tree = makeheap()
enrollment_cap = len(heap_tree)
enrolled_Ids = []
enrolled_Students = []

print("Heap after insertion:")

print(heap_tree)



#delete
def delete_element_heap(hT,col, val): # hT is the heap tree, col is the column to be based on, val is the value to be deleted
    basedOn = 1
    if col == "Id": # If the column is Id, set basedOn to 2
        basedOn = 2
    index = None # Initialize index to None
    found,result = search( heap_tree, val)
    print(found,result)
    if found == False:
        print("Element not found in the heap")
        return None
    index = result[0][1]
    
    delItem = hT[index] # Get the value to be deleted

    hT[index] = hT[-1] # Replace the value to be deleted with the last value in the heap tree
    hT.pop() # Remove the last value from the heap tree
    
    if index < len(hT): # If the index is less than the length of the heap tree
        heapify_down(hT, index) # Perform heapify down
        # heapify_up(hT, index) # Perform heapify up
    
    return delItem


# Example usage:
# Assuming heap_tree is already populated
element_to_delete = 108  # Example element to delete
deleted_element = delete_element_heap(heap_tree,"Id", element_to_delete)
if deleted_element is not None:
    print("Deleted element:", deleted_element)
    print("Heap after deletion:")
    print(heap_tree)



# #get
# def get_element_heap(hT,col,val): # hT is the heap tree, col is the column to be based on, val is the value to be retrieved
#     basedOn = 1
#     if col == "Id": # If the column is Id, set basedOn to 2
#         basedOn = 2
#     index = None
#     for i in range(len(hT)): # Iterate through the heap tree
#         if hT[i][basedOn] == val: # If the value is found
#             index = i
#             break
    
#     if index is None:
#         print("Element not found in the heap")
#         return None
    
#     return hT[index]

# # Example usage:
# # Assuming heap_tree is already populated
# el_to_get = 105  # Example index to retrieve
# retrieved_element = get_element_heap(heap_tree,"Id", el_to_get)
# if retrieved_element is not None:
#     print("Retrieved element :", retrieved_element)







el_to_Get = 111  # Example index to retrieve
priority = 1
retrieved_element = search(heap_tree,el_to_Get)
if retrieved_element is not None:
    print("Retrieved element :", retrieved_element)








#update
def update_element_heap(hT,col,val,update_col, new_value): # hT is the heap tree, col is the column to be based on, val is the value to be updated, update_col is the column to be updated, new_value is the new value
    basedOn = 1
    if col == "Id": # If the column is Id, set basedOn to 2
        basedOn = 2
    index = None
    found,result = search( heap_tree, val)
    print(found,result)
    if found == False:
        print("Element not found in the heap")
        return None
    index = result[0][1] 
    
    old_value = hT[index] # Get the old value
    updated_element = list(old_value) # Convert the old value to a list
    updated_element[update_col] = new_value # Update the value
    hT[index] = tuple(updated_element) # Convert the updated value back to a tuple and update the heap tree
    # If the new value is greater, perform heapify up, otherwise heapify down
    if hT[index][0] > old_value[0]: 
        heapify_up(hT, index)
    else:
        heapify_down(hT, index)
    
    return True

# Example usage:
# Assuming heap_tree is already populated
el_to_update = 105  # Example index to update
new_value = "Updated Name"  # Example new value
print("Updating")
success = update_element_heap(heap_tree,"Id",el_to_update, 1, new_value)
if success:
    print("Updated element with new value:", new_value)
    print("Heap after update:")
    print(heap_tree)
else:
    print("Update failed.")










def enroll_stuTea():  # Enroll students helper
   
        
    teacher.tablewidget.setRowCount(0) # Clear the table widget
    for i in range(len(enrolled_Students)): # Iterate through the enrolled students
        teacher.tablewidget.insertRow(i) # Insert a row in the table widget
        for j in range(1,5): # Iterate through the columns
            teacher.tablewidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(enrolled_Students[i][j]))) # Set the item in the table widget

    teacher.IdTxt.setHidden(False) # Set the Id text box to visible
    teacher.NameTxt.setHidden(False)  # Set the Name text box to visible
    teacher.YearTxt.setHidden(False) # Set the Year text box to visible
    teacher.SchoolTxt.setHidden(False) # Set the School text box to visible

    teacher.label_3.setHidden(True) # Set the label to hidden
    teacher.statusLbl.setHidden(True) # Set the status label to hidden

    pass

def gen_stuTea(): # Generate students helper
    student.statusLbl.setText("Pending") # Set the status label to pending
    student.statusLbl.setStyleSheet("color: yellow") # Set the status label color to yellow
    teacher.tablewidget.setRowCount(0) # Clear the table widget
    teacher.IdTxt.setHidden(True) # Set the Id text box to hidden
    teacher.NameTxt.setHidden(True) # Set the Name text box to hidden
    teacher.YearTxt.setHidden(True) # Set the Year text box to hidden
    teacher.SchoolTxt.setHidden(True) # Set the School text box to hidden
    teacher.label_3.setHidden(False) # Set the label to visible
    teacher.statusLbl.setHidden(False) # Set the status label to visible

    pass

class Ui_MainWindow(QtWidgets.QDialog): # RO window class


    def __init__(self): 
        super(Ui_MainWindow,self).__init__()
        loadUi("RO.ui",self) # Load the RO.ui file
        
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
        self.csvBtn = self.findChild(QtWidgets.QPushButton, 'csvBtn')
        self.addBtn = self.findChild(QtWidgets.QPushButton, 'addBtn')
        self.edit = self.findChild(QtWidgets.QPushButton, 'editBtn')
        self.viewDB = self.findChild(QtWidgets.QPushButton, 'viewDB')
        self.unviewDB = self.findChild(QtWidgets.QPushButton, 'unviewDB')
        self.unviewDB.setHidden(True)
        self.viewDB.setHidden(True)
        self.deleteBtn.setHidden(True)
        self.addBtn.setHidden(True)
        self.edit.setHidden(True)
        self.deleteBtn.clicked.connect(self.delete)
        self.addBtn.clicked.connect(self.add)
        self.edit.clicked.connect(self.update)
        self.csvBtn.clicked.connect(self.csvChange)
        self.viewDB.clicked.connect(self.addHeapToEnrolled)
        self.unviewDB.clicked.connect(self.deleteHeapToEnrolled)
        global heap_tree
        global permaHeap

    def csvChange(self): # Function to change the CSV file
        try :
            inputDialog = QtWidgets.QFileDialog() # Open a file dialog
            file = inputDialog.getOpenFileName(self, 'Open file', '.\\', "CSV files (*.csv)") # Get the file name
            
            if file != "": # If the file is not empty
                fileInput=[]
                with open (file[0]) as f :
                    lines = f . readlines ()
                    print(lines)
                    print(lines[0])
                    if lines[0] != 'Priority,Name,ID,Year,School\n': # If the first line is not the column names 
                        return
                global heap_tree
                global permaHeap
                print("Heap before change: ")
                print(heap_tree)
                heap_tree = makeheap(file[0]) # Create a new heap tree from the file
                permaHeap = makeheap(file[0]) # Create a new heap tree from the file
                print("Heap after change:")
                print(heap_tree)
        except( Exception):
            print(Exception)
            

    def logout(self):
        widget.setCurrentIndex(0) # Go to the login page

    def add(self): # Function to add an element
        inputDialog = QtWidgets.QInputDialog() # Open an input dialog
        name, ok = inputDialog.getText(self, 'Input Dialog', 'Enter name:' ) # Get the name
        if ok: # If Success
            if name == "": # If the name is empty or already exists
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Invalid name")
                msg.setWindowTitle("Credentials error")
                msg.exec_()
                return
            id, ok = inputDialog.getText(self, 'Input Dialog', 'Enter id:') # Get the id
            if id == "" and ok:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Enter ID to continue")
                msg.setWindowTitle("Credentials error")
                msg.exec_()
            elif id != "" and ok: # If the id is not empty
                found,result = search( heap_tree, int(id))
                if found == True: # If the item is found
                # Show error message
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("ID already exists")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    return
                elif ok and found == False: # If the item is not found
                    year, ok = inputDialog.getItem(self, 'Input Dialog', 'Select year:', ('Freshman', 'Sophomore', 'Junior', 'Senior'), 0, False) # Get the year
                    if ok and year is not None: # If the year is not empty
                        school, ok = inputDialog.getItem(self, 'Input Dialog', 'Select school:', ('Engineering', 'Humanities'), 0, False) # Get the school
                        if ok and school is not None: # If the school is not empty
                            priority = 1
                            id = int(id)
                            if year == 'Freshman': # Set the priority based on the year
                                priority = 1
                            elif year == 'Sophomore': 
                                priority = 2
                            elif year == 'Junior':
                                priority = 3
                            elif year == 'Senior':
                                priority = 4
                            insert_heap_tree(heap_tree, (priority, name, id, year, school)) # Insert the item into the heap tree
                            insert_heap_tree(permaHeap, (priority, name, id, year, school)) # Insert the item into the heap tree
                            LoginIds[str(id)] = name # Add the name and id to the LoginIds dictionary
                            print("Heap after insertion:")
                            print_array(heap_tree)
                            self.generate() # Generate the table


    def delete(self): # Function to delete an element
        id,ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter id:') # Get the id
    
        if ok and id != "": # If the id is not empty
            deleted_element = delete_element_heap(heap_tree,"Id", int(id)) # Delete the element with the id

            if deleted_element is not None: # If the element is found
                print("Deleted element:", deleted_element)
                print("Heap after deletion:")
                print_array(heap_tree)
                self.generate() # Generate the table
                print("LoginIds before deletion:")
                print(LoginIds)
                del LoginIds[str(deleted_element[2])] # Delete the name from the LoginIds dictionary
                print("LoginIds after deletion:")
                print(LoginIds)
            else: # If the element is not found
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Student not found")
                msg.setWindowTitle("Element not found")
                msg.exec_()


    def update(self): # Function to update an element
        try:
            id, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter id:') 
            if ok and id != "":
                found,result = search( heap_tree, int(id))
                # item = get_element_heap(heap_tree,"Id", int(id)) # Get the item with the id
                if found == False:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Student not found")
                    msg.setWindowTitle("Element not found")
                    msg.exec_()
                    return
                updateCol, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select column to update:', ('Name','Year', 'School'), 0, False) # Get the column to update
                if ok and updateCol == 'School': # If the column to update is School
                    new_value, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select new school:', ('Engineering', 'Humanities'), 0, False) # Get the new value
                    if ok:
                        success = update_element_heap(heap_tree,"Id", int(id), 4, new_value) # Update the element
                        success = update_element_heap(permaHeap,"Id", int(id), 4, new_value) # Update the element
                        if success: # If the update is successful
                            print("Updated element with new value:", new_value)
                            print("Heap after update:")
                            print_array(heap_tree)
                            self.generate() # Generate the table
                        else:
                            msg = QtWidgets.QMessageBox() # for generating error if update fails.
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setText("Update failed")
                            msg.setWindowTitle("Failure")
                            msg.exec_()
                elif ok and updateCol == 'Year': # If the column to update is Year
                    new_value, ok = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Select new year:', ('Freshman', 'Sophomore', 'Junior', 'Senior'), 0, False) # Get the new value
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
                        success = update_element_heap(permaHeap,"Id", int(id), 0, priority)
                        success = update_element_heap(permaHeap,"Id", int(id), 3, new_value)
                        if success:
                            print("Updated element with new value:", new_value)
                            print("Heap after update:")
                            print_array(heap_tree)
                            self.generate()
                        else:
                            msg = QtWidgets.QMessageBox() # for generating error if update fails.
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setText("Update failed")
                            msg.setWindowTitle("Failure")
                            msg.exec_()
                elif ok and updateCol == 'Name':
                    new_value, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter new name:')
                    if ok:
                        success = update_element_heap(heap_tree,"Id", int(id), 1, new_value)
                        success = update_element_heap(permaHeap,"Id", int(id), 1, new_value)
                        if success:
                            LoginIds[str(id)] = new_value
                            print("Updated element with new value:", new_value)
                            print("Heap after update:")
                            print_array(heap_tree)
                            self.generate()
                        else:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setText("Update failed")
                            msg.setWindowTitle("Failure")
                            msg.exec_()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enter a valid Id")
            msg.setWindowTitle("Error")
            msg.exec_()


    def enroll_helper(self,cap):
        enrollment_cap = cap # Set the enrollment cap
        enrolled_Ids.clear() # Clear the enrolled ids
        enrolled_Students.clear() # Clear the enrolled students
        self.tableWidget.setRowCount(0) # Clear the table widget
        for i in range(cap): # Iterate through the enrollment cap
            max_element = heap_tree[0] # Get the max element
            self.tableWidget.insertRow(i) # Insert a row in the table widget
            for j in range(1,5): # Iterate through the columns
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(max_element[j]))) # Set the item in the table widget
            enrolled_Ids.append(max_element[2]) # Append the id to the enrolled ids
            enrolled_Students.append(max_element) # Append the student to the enrolled students
            print("Max element:", max_element)
            # Remove the max element from the heap
            delete_element_heap(heap_tree, "Id", max_element[2]) # Delete the element from the heap tree
        print(heap_tree)
        self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"]) # Set the horizontal header labels
        self.genBtn.setProperty("text", "Regenerate Table from Database") # Set the text of the generate button
        self.addBtn.setHidden(True) # Set the add button to hidden
        self.edit.setHidden(True) # Set the edit button to hidden
        self.deleteBtn.setHidden(True) # Set the delete button to hidden

        print("Enrolled students:")
        print(enrolled_Ids)
        print_array(enrolled_Students)
        print("Enrollment cap:", enrollment_cap)

        enroll_stuTea() # Enroll the students

       
    def enroll(self, cap): # Function to enroll the students
        print(heap_tree)
        if cap.text() == "": # If the capacity is empty
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enrollment capacity cannot be empty")
            msg.setWindowTitle("Enrollment Error")
            msg.exec_()
            return
        cap = int(cap.text()) # Convert the capacity to an integer
        if(cap > len(heap_tree)): # If the capacity is greater than the heap tree length
            cap = len(heap_tree) # Set the capacity to the heap tree length
            self.cap.setText(str(cap)) # Set the capacity text
            self.enroll_helper(cap) # Enroll the students
            self.enrollBtn.setProperty("enabled", False) # Set the enroll button to disabled
            self.viewDB.setHidden(False) # Set the view database button to visible
        elif(cap <= 0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid capacity")
            msg.setWindowTitle("Enrollment Error")
            msg.exec_()
            return
        else:
            self.enroll_helper(cap) # Enroll the students
            self.enrollBtn.setProperty("enabled", False) # Set the enroll button to disabled
            self.viewDB.setHidden(False) # Set the view database button to visible

    def generate(self): # Function to generate the table
        if self.genBtn.text() == "Regenerate Table from Database": 
            for i in range(len(enrolled_Students)):
                found,result = search( heap_tree, enrolled_Students[i][2])
                if found == False:
                    insert_heap_tree(heap_tree, enrolled_Students[i]) # Insert the enrolled students back into the heap tree
        enrolled_Students.clear() # Clear the enrolled students
        enrolled_Ids.clear() # Clear the enrolled ids
        gen_stuTea() # Generate students helper

        self.tableWidget.setRowCount(0) # Clear the table widget
        for i in range(len(heap_tree)):
            self.tableWidget.insertRow(i) # Insert a row in the table widget
            for j in range(1,5):
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(heap_tree[i][j]))) # Set the item in the table widget

        self.tableWidget.setHorizontalHeaderLabels([ "Name", "Id", "Year", "School"]) # Set the horizontal header labels
        self.genBtn.setProperty("text", "Generate Table from Database") # Set the text of the generate button
        self.tableWidget.setHidden(False) # Set the table widget to visible
        self.enrollBtn.setProperty("enabled", True) # Set the enroll button to enabled
        self.viewDB.setHidden(True) # Set the view database button to visible
        self.unviewDB.setHidden(True) # Set the unview database button to visible
        self.deleteBtn.setHidden(False) # Set the delete button to visible
        self.addBtn.setHidden(False) # Set the add button to visible
        self.edit.setHidden(False) # Set the edit button to visible
        
    def addHeapToEnrolled(self):
        cap = len(enrolled_Ids)
        for i in range(cap,len(heap_tree)+cap):
            self.tableWidget.insertRow(i) # Insert a row in the table widget
            for j in range(1,5):
                self.tableWidget.setItem(i,j-1,QtWidgets.QTableWidgetItem(str(heap_tree[i-cap][j])))
                self.tableWidget.item(i,j-1).setBackground(QtGui.QColor(200, 0, 0)) # Set the background color of the item
        self.viewDB.setHidden(True) # Set the view database button to visible
        self.unviewDB.setHidden(False) # Set the unview database button to visible

    def deleteHeapToEnrolled(self):
        cap = len(enrolled_Ids)
        for i in range(cap,len(heap_tree)+cap):
            self.tableWidget.removeRow(cap) # Remove the row from the table widget
        self.viewDB.setHidden(False) # Set the view database button to visible
        self.unviewDB.setHidden(True) # Set the unview database button to visible


class Login(QtWidgets.QDialog):
    def __init__(self):
        
        super(Login,self).__init__()
        loadUi("Login.ui",self) # load the login file and initialize the UI.
        self.Student.clicked.connect(self.stu)
        self.Teacher.clicked.connect(self.teach)
        self.Admin.clicked.connect(self.admin)

    def stu(self): # method to handle student button click.
        widget.setCurrentIndex(1)
    
    def teach(self): # method to handle teacher button click.
        widget.setCurrentIndex(2)

    def admin(self): # method to handle admin button click.
        widget.setCurrentIndex(3)
        
    pass
        
class StudentLogin(QtWidgets.QDialog):
    def __init__(self):
        super(StudentLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.setWindowTitle("Student Login")
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label.setText("Student Login")
        


    def back(self):
        widget.setCurrentIndex(0)
        
    def login(self): # for student login 
        username = self.Username.text()
        password = self.Password.text()
        print(username, password)
        print(LoginIds)
        try:
            # Iterate over the LoginIds dictionary to check if the entered credentials are valid
            for v, k in LoginIds.items():
                # Check if the username and password match the ones in LoginIds
                if k == password and v == username:
                    # Get the item from heap_tree with the given password (password is the ID)
                    found, result = search(heap_tree, int(username)) 
                    if found == True:
                        item = result[0][0]
                        # Clear the rows in the student tableWidget and insert a new row
                        student.tableWidget.setRowCount(0)
                        student.tableWidget.insertRow(0)
                        for j in range(1, 5):
                            student.tableWidget.setItem(0, j - 1, QtWidgets.QTableWidgetItem(str(item[j])))
                        widget.setCurrentIndex(5)
                        # Update the enrollment status label based on enrolled_Ids
                        if enrolled_Ids:
                            if int(password) in enrolled_Ids:
                                student.statusLbl.setText("Enrolled")
                                student.statusLbl.setStyleSheet("color: green")
                            else:
                                student.statusLbl.setText("Not Enrolled")
                                student.statusLbl.setStyleSheet("color: red")
                        return
            # If no matching credentials found, show alert
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid credentials")
            msg.setWindowTitle("Login Error")
            msg.exec_()
        except Exception as e:
            print("An error occurred:", str(e))    
            
        
        
    pass

class StudentWindow(QtWidgets.QDialog):
    def __init__(self): # for loading the UI 
        super(StudentWindow,self).__init__()
        loadUi("Student.ui",self)
        self.statusLbl = self.findChild(QtWidgets.QLabel, 'statusLbl')
        self.statusLbl.setText("Pending")
        self.statusLbl.setStyleSheet("color: yellow") 

        self.Logout = self.findChild(QtWidgets.QPushButton, 'LogoutBtn')
        self.Logout.clicked.connect(self.logout)
    
    def logout(self): # intializing logout
        widget.setCurrentIndex(0)
        

class TeacherLogin(QtWidgets.QDialog): # for loading the UI
    def __init__(self):
        super(TeacherLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.setWindowTitle("Teacher Login")
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label.setText("Teacher Login")
        

    def back(self): # switching when back button is clicked.
        widget.setCurrentIndex(0)
        
    def login(self): # login logic for teacher login page
        try:
            if self.Username.text() == "Teacher" and self.Password.text() == "teacher": # if credentials match
                widget.setCurrentIndex(6)
            else:
                # if credentails do not match show error message
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Invalid credentials")
                msg.setWindowTitle("Login Error")
                msg.exec_()
        except Exception as e:
            # FOr any exception show error message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid credentials")
            msg.setWindowTitle("Login Error")
            msg.exec_()

class TeacherWindow(QtWidgets.QDialog):
    def __init__(self): # for initializing UI.
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


    def get(self):  # Method to retrieve student details
        try :
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
                        # If there are no enrolled students
                        # Show a warning message indicating that students not found.
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Students not found")
                        msg.setWindowTitle("Failure")
                        msg.exec_()
            else:
                # If enrolled has not occured.
                # Show a warning message indicating that enrollment is yet to begin
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Enrollment is yet to begin.")
                msg.setWindowTitle("Failure")
                msg.exec_()
        except:
            # If an exception occurs
            # Show a warning message indicating that the operation failed
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Get failed")
            msg.setWindowTitle("Failure")
            msg.exec_()


    
    def logout(self):
        widget.setCurrentIndex(0) # initializing logout
        
    pass

class AdminLogin(QtWidgets.QDialog):
    def __init__(self):
        super(AdminLogin,self).__init__()
        loadUi("LoginAll.ui",self)
        self.setWindowTitle("Admin Login")
        self.Login.clicked.connect(self.login)
        self.Back.clicked.connect(self.back)
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.label.setText("Admin Login")

    def back(self):
        widget.setCurrentIndex(0)
        
    def login(self): # login logic for admin
        try:
            if self.Username.text() == "Admin" and self.Password.text() == "admin": # credentials match 
                widget.setCurrentIndex(4)
            else:
                # Show error message if invalid credentials are entered. 
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Invalid credentials")
                msg.setWindowTitle("Login Error")
                msg.exec_()
        except Exception as e:
            # Show error message if any exception occurs.
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Invalid credentials")
            msg.setWindowTitle("Login Error")
            msg.exec_()


if __name__ == "__main__":
    # Create an instance of QApplication to manage the GUI application
    app = QtWidgets.QApplication(sys.argv)
    # Set the display name for the application
    app.setApplicationDisplayName("Registration Office")
    widget = QtWidgets.QStackedWidget()
    # Set the window icon for the application
    widget.setWindowIcon(QtGui.QIcon("Logo.png"))
    ui = Ui_MainWindow()  # Main window UI
    login = Login()  # Login dialog
    studentLogin = StudentLogin()  # Student login dialog
    student = StudentWindow()  # Student window
    teacher = TeacherWindow()  # Teacher window
    teacherLogin = TeacherLogin()  # Teacher login dialog
    adminLogin = AdminLogin()  # Admin login dialog
    # Add the dialogs to the stacked widget
    widget.addWidget(login)
    widget.addWidget(studentLogin)
    widget.addWidget(teacherLogin)
    widget.addWidget(adminLogin)
    widget.addWidget(ui)
    widget.addWidget(student)
    widget.addWidget(teacher)
    # fixed height and width.
    widget.setFixedWidth(500)
    widget.setFixedHeight(700)
    widget.show()
    sys.exit(app.exec_())