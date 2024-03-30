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


data = [
    (1, "John Smith", 101, "Freshman", "Engineering"),
    (2, "Emma Johnson", 102, "Sophomore", "Humanities"),
    (3, "Michael Brown", 103, "Junior", "Engineering"),
    (4, "Sarah Lee", 104, "Senior", "Humanities"),
    (1, "David Rodriguez", 105, "Freshman", "Engineering"),
    (2, "Emily Wilson", 106, "Sophomore", "Engineering"),
    (3, "Daniel Martinez", 107, "Junior", "Humanities"),
    (4, "Sophia Anderson", 108, "Senior", "Engineering"),
    (1, "James Thompson", 109, "Freshman", "Humanities"),
    (2, "Olivia Garcia", 110, "Sophomore", "Engineering")
]

for item in data:
    insert_heap_tree(heap_tree, item)


print("Heap after insertion:")
print_array(heap_tree)
