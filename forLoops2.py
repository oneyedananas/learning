# iterating using 'while' is not very efficient as it requires a lot of code
# instead 'for' is used ('foreach' in other languages)

words = ["prvni", "druhy", "treti", "ctvrty"]
counter = 1
for word in words:
    print(str(counter) + ". " + word)
    counter = counter + 1
