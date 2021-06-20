with open('sample.txt', 'w') as f:  # open the file in write mode
    for i in range(10):
        f.write(f"This is line number: {i} \n")  # Save to file, each time in a new line
