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




heap_tree = []

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

# Example usage:
# Assuming heap_tree is already populated
element_to_delete = 108  # Example element to delete
deleted_element = delete_element_heap(heap_tree,"Id", element_to_delete)
if deleted_element is not None:
    print("Deleted element:", deleted_element)
    print("Heap after deletion:")
    print(heap_tree)



#get
def get_element_heap(hT, index):
    if index < 0 or index >= len(hT):
        print("Index out of bounds")
        return None
    return hT[index]

# Example usage:
# Assuming heap_tree is already populated
index_to_get = 5  # Example index to retrieve
retrieved_element = get_element_heap(heap_tree, index_to_get)
if retrieved_element is not None:
    print("Retrieved element at index", index_to_get, ":", retrieved_element)



#update
def update_element_heap(hT, index, new_value):
    if index < 0 or index >= len(hT):
        print("Index out of bounds")
        return False
    
    old_value = hT[index]
    hT[index] = new_value

    # If the new value is greater, perform heapify up, otherwise heapify down
    if new_value[0] > old_value[0]:
        heapify_up(hT, index)
    else:
        heapify_down(hT, index)
    
    return True

# Example usage:
# Assuming heap_tree is already populated
index_to_update = 0  # Example index to update
new_value = (5, "Updated Name", 105, "Updated Grade", "Updated Department")  # Example new value
success = update_element_heap(heap_tree, index_to_update, new_value)
if success:
    print("Updated element at index", index_to_update, "with new value:", new_value)
    print("Heap after update:")
    print(heap_tree)
else:
    print("Update failed.")

