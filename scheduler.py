import json
import sys

json_file = sys.argv[1]

with open(json_file) as f:
	classes = json.load(f)

print(classes)