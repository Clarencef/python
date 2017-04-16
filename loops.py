people = ['ben','albert','allen','bob']

# for loop
for person in people:
  print(person)

# iterate by seq index
for i in range(len(people)):
  print('Current Person:',people[i])

for i in range(0,10):
  print(i)

# while loop
count = 0
while count <= 5:
  print('count:',count)
  if count == 2:
    break
  count = count + 1
