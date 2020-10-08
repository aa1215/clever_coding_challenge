import json
import sys

# # error handling for cases where no file is presented or file is the wrong file type
# if len(sys.argv) < 2:
# 	# go through and change these to standard error
# 	print("Error: No argument provided.", file=sys.stderr)
# 	quit()
#
# else:
# 	json_file = sys.argv[1]
#
# if json_file.find(".") == -1:
# 	print("Error: No argument provided.", file=sys.stderr)
# 	quit()
#
# else:
# 	file_extension = json_file.split(".")[1]
#
# if file_extension != "json":
# 	print("Error: No argument provided.", file=sys.stderr)
# 	quit()
#
with open("math.json") as f:
	classes = json.load(f)

classes_dict = {}
for i in range(0, len(classes)):
	classes_dict[classes[i].get('name')] = classes[i].get('prerequisites')

numbers_map = {}
count = 0
for i in classes_dict.keys():
	numbers_map[i] = count
	count = count + 1

current_list = []

vertices = []
for i in classes_dict:
	vertices.append(i)

def topological_sort(start, visited, sort):
    """Perform topolical sort on a directed acyclic graph."""
    current = start
    # add current to visited
    visited.append(current)
    neighbors = classes_dict[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    # return sort
    return sort

sort = topological_sort(vertices[0], [], [])
for i in sort:
	print(i)