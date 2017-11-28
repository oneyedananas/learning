# performs code on each item in a list i.e. iteration
# uses a while loop and a counter variable

words = ["milda", "nigga", "karel", "pavel"]
counter = 0
max_index = len(words) - 1  # python starts counting from 0 so -1 is needed

# print(max_index) now returns 3: range of the list - 1

while counter <= max_index:
    word = words[counter]
    print(word + "!")  # concatenation
    counter = counter + 1
