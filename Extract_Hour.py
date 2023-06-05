name = "mbox-short.txt"
handle = open(name)

time = dict()

# For loop to split the lines up into individual words
# in the file into a list
for x in handle:
    y = x.split()
    # If From is in the list
    if 'From' in y:
        # If : is in the list of the time
        if ':' in y[5]:
            # Then get ONLY the hour in the time and append it to the time dictionary
            # as well as adding a count. Then if the same hour shows up then keep counting.
            time[y[5][0:2]] = time.get(y[5][0:2], 0) + 1

# For loop that will get the key and value pair in the sorted items in the time dictionary
for key, value in sorted(time.items()):
    print(key, value)
