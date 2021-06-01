## ASSESSMENTS

Below are tasks that you are expected to complete and provide solutions to in the python scripts in the src folder. Enjoy!

## Task 1

Write a simple function named `nameValidator` that takes in `name` as an argument and validates the argument using the following constraints 
* Must be a string which is a combination of two substrings, each representing first name and last name respectively, Eg. `"Mike Gollum"`
* Must only contain alphabets and a single space character that separates the first and last name substrings 
* The length of the first and last name substrings each must be >= 5 characters and <= 20 characters 

For each of the constraints defined above, raise an exception with a meaningful error message when the constraint is violated. 

## Task 2

Write a simple function named `oddNumbers` which returns a list of odd numbers between the range of `start` and `stop`. This list should be created using python's list comprehension method.
e.g start = 2 and stop = 34, list should be = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23] 

## Task 3

Write a function named `dictComp` that takes in two integer values `stop` and `step` as arguments and returns a dictionary generated using python comprehensions, which will have string keys in the format `"items-#"` and values of type `list`, where each list is of length `step` and contains only integers. 

The integers within the list values will be sequentially generated, such that integers in a second list is a continuation of those in the first list and so on for others until we get to `stop` 

```python
# Example output dictionary given that : stop = 10 and step = 4 

{
   "items-1": [ 1, 2, 3, 4 ],
   "items-2": [ 5, 6, 7, 8 ], 
}

```

Notice in the example above, the first list starts from 1 and not 0 and that the remaining integers `9 & 10` were discarded since they are not up to 4 integers to make up another entry in the dictionary.
