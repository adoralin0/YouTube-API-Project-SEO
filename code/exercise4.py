# WRITE YOUR CODE HERE
def is_nested(d):
    for value in d.values():
        # Check if the value is a list, tuple, or dictionary
        if isinstance(value, (list, tuple, dict)):
            return True
    return False

# test code below
# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : [4, 5]
  }

  print(is_nested(example_dict))