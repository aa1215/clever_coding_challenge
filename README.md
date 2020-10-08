# Clever Coding Challenge
This is my submission for the Clever SWE Intern 2021 Coding Challenge. This program finds an order that a student can take each of the courses provided where all the prerequisites are satisfied.

## Prerequisites + Installation
This program submission does not require compilation. The program can be run through these commands:
```bash
cd clever_coding_challenge
./scheduler math.json
```

## Program Design
**Courses Input** 

According to the instructions, "the first (and only) argument to the program will be a path to a JSON file containing class names and all (if any) prerequisites they have." I used `argv` to set the input equal to the 2nd argument after the python script: i.e. `./scheduler math.json` or `python scheduler.py math.json`. 

I also decided to add in a case where if the user didn't specify a path to a JSON file in the program argument, they would have an option to input the file path as well as the program asks the user to `Please enter your file path.` 

Lastly, I set up error handling in case the file provided was not a .json file. The program checks in multiple different ways to make sure that the input file is a proper JSON file, and exits with an error if it is not.

**Data Formatting** 

The next step was to load the JSON data. I used the `json` library along with the `json.load` function to load the data from the JSON file. The data is presented as a list of dictionaries of lists, but I figured it would be simpler to just have a dictionary of lists. 

I created a helper function called `list_to_dictionary` that takes the results from `json.load` and converts it into a simpler dictionary.

Lastly, I set up error handling in the case where no classes were provided.

**Topological Sort**

Once I had my properly formatted dictionary of courses and prerequisites, it was time to figure out how to get the proper order! It helped me to visualize the list of courses and prerequisites as a graph, where each course was connected to other courses by prerequisite relationships.

More specifically, the input dictionary is a directed acyclic graph. The direction of courses can only flow in one direction and the course ordering cannot be scheduling. i.e. this example is not possible:
`calculus -> multivariable calculus -> calculus`

It wouldn't make sense for a class to be a prerequisite for it's prerequisite, so we know that we can represent our schedule of courses as a directed acyclic graph. 

I spent some time looking through the input dictionary and then understood that for each course in the dictionary, I needed to find a way to ensure that the elements in its prerequisite list were ordered before the list. I thought about a few possibilities, such as breadth-first search, depth-first search, and then remembered an algorithm I had learned in my algorithms class: topological sort.

Topological sort is a sorting algorithm that is a modified version of depth-first search. For a linear ordering of vertices, for each vertice `[a,[b,c]]` the elements b and c come before a in the ordering. Since my courses dictionary was in the proper format that I needed for topological sort, I implemented a topological sort function that takes in a starting course and outputs a list of ordered courses.

Once I obtained my list of ordered courses, I simply printed out every course in this list of ordered courses for the final output.

## Testing

There were some test cases that I considered when testing my program.

1. Wrong input file type
2. Empty JSON file (i.e. no courses provided)
2. 1 course provided with prerequisites
3. 1 course with prerequisites
4. Prerequisites are not in the course_list
5. Provided test cases

## Considerations and Future Improvements

## Time Complexity

