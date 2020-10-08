import json
import sys

# error handling for cases where no file is presented or file is the wrong file type
if len(sys.argv) < 2:
	# go through and change these to standard error
	print("Error: No argument provided.", file=sys.stderr)
	quit()

else:
	json_file = sys.argv[1]

if json_file.find(".") == -1:
	print("Error: No argument provided.", file=sys.stderr)
	quit()

else:
	file_extension = json_file.split(".")[1]

if file_extension != "json":
	print("Error: No argument provided.", file=sys.stderr)
	quit()

with open(json_file) as f:
	classes = json.load(f)

classes_dict = {}
for i in range(0, len(classes)):
	classes_dict[classes[i].get('name')] = classes[i].get('prerequisites')

current_list = []

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