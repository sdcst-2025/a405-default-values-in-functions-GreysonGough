#!python3

"""
Create a function called sentence() that takes 3 input paremters:
greeting: string that will contain a salutation, examples: Hello, Hiya, Ola
name: a string that will contain a person's name.  This should have a default value of "Benjamin"
question: a string that will contain a full question to ask the person.  It should have a default value of "How are you"

Have the greeting, name and question combine together into a string. 
Note: You are not using a print statement, so you may
use the concatenate (+) operator. Make sure your spacing is appropriate.
However, you can still use formatted strings using:
f"{variable} contents"

return value:
string. The output sentence

example assertion:
assert sentence("Hello") == "Hello Benjamin. How are you"
assert sentence("Hiya","Casey","Have you enjoyed your meal") == "Hiya Casey. Have you enjoyed your meal"

(2 points) 
"""

def sentence(greeting, name="Benjamin", question="How are you"):
    return f"{greeting} {name}. {question}"


if __name__ == "__main__":
  assert sentence("Hello") == "Hello Benjamin. How are you"
  assert sentence("Hiya","Casey","Have you enjoyed your meal") == "Hiya Casey. Have you enjoyed your meal"
