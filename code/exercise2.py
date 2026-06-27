# WRITE YOUR CODE HERE
def move_to_bottom(d, key):
    if key in d:
        d[key] = d.pop(key)
    else:
        print("The key is not in the dictionary")
    return d

# test code below
# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 4)
  print(example_dict)