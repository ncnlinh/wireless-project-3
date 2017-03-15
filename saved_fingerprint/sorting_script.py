import os

for filename in os.listdir('.'):
  with open(filename) as f:
    lines = f.readlines()

  lines = sorted(lines)

  f = open('sorted_'+filename, 'w')
  for line in lines:
    f.write(line)
  f.close()

