import json
import sys

if len(sys.argv) < 2:
    print("Please enter your file path.")
    json_file = input()
else:
    json_file = sys.argv[1]

if json_file == "" and len(sys.argv) < 2:
    print("Error: Please enter a proper .json file.", file=sys.stderr)
    quit()

if json_file.find(".") == -1:
	print("Error: Please enter a proper .json file.", file=sys.stderr)
	quit()

else:
	file_extension = json_file.split(".")[1]

if file_extension != "json":
	print("Error: Please enter a proper .json file.", file=sys.stderr)
	quit()

with open(json_file) as f:
	classes = json.load(f)

if classes == []:
    print("Error: Please enter at least one class.", file=sys.stderr)
    quit()

def list_to_dict(classes):
    classes_dict = {}
    for i in range(0, len(classes)):
        classes_dict[classes[i].get('name')] = classes[i].get('prerequisites')
    return classes_dict

classes_dict = list_to_dict(classes)
vertices = []
for i in classes_dict:
	vertices.append(i)

def topological_sort(start, visited, sort):
    current = start
    visited.append(current)
    neighbors = classes_dict[current]
    for neighbor in neighbors:
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    sort.append(current)
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    return sort

sort = topological_sort(vertices[0], [], [])
for i in sort:
	print(i)
