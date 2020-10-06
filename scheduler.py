import json
import sys

## error handling for cases where no file is presented or file is the wrong file type
if len(sys.argv) < 2:
	print("Please specify a JSON file argument.")
	quit()

else:
	json_file = sys.argv[1]

if json_file.find(".") == -1:
	print("Please specify a JSON file argument.")
	quit()

else:
	file_extension = json_file.split(".")[1]

if file_extension != "json":
	print("Please specify a JSON file argument.")
	quit()

with open(json_file) as f:
	classes = json.load(f)

print(classes)
