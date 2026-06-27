# WRITE YOUR CODE HERE
def swap(d):
    swapped_dict = {}
    try:
        for key, value in d.items():
            # Attempting to use 'value' as a key will raise a TypeError if it's a list
            swapped_dict[value] = key
        return swapped_dict
    except TypeError:
        return "Cannot swap the keys and values for this dictionary"


# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)