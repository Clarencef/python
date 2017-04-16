# Open a file and write mode - will overwrite the file
file = open('movie_quotes.txt','w')

# Get info
print('Name: ', file.name)
# File is open?
print('Is Closed: ', file.closed)
# File mode
print('Opening Mode: ', file.mode)
# Write File
file.write('I love javascript\n')
# Close File
file.close()
print('Is Closed: ', file.closed)

# Open a file and append mode
file = open('movie_quotes.txt', 'a')
print('Opening Mode: ', file.mode)
file.write('I also love python')
file.close()

# Read from file
file = open('movie_quotes.txt', 'r+')
content = file.read()
print(content)
file.close()

# Create file
file = open('test.txt', 'w+')
file.write('I love node.js')
file.close()