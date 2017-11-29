# 'for' is often used to repeat certain code a number of times.
# when that happens, forloops are combined with 'range' objects.
# it is not necessary to call 'list' on the 'range' object when it's used in a for loop,
# bcs it is not being indexed and so list is not needed.

for p in range(69):
    print("gblin is the best pythonista ever")

for i in range(0, 20, 2):  # create a list of even numbers (including 0) ^ < 20
    print(i)