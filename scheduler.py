import json
import sys

## error handling for cases where no file is presented or file is the wrong file type
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

print(classes)
