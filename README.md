# Clever Coding Challenge
This is my submission for the Clever SWE Intern 2021 Coding Challenge. Imagine you are a student and you have a list of courses you want to take. Many of these courses have prerequisites which you must take before you can take that course. This program finds an order that you can take each of the courses where all the prerequisites are satisfied.

## Prerequisites + Installation
This program contains an executable inside of `clever_coding_challenge/distr`. The program can be run easily through:
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

## Testing

## Considerations and Future Improvements

## Time Complexity

