"""
Functional test.
To run:
python soccer_functional_test.py
"""
import string
import random
import os

def print_file(name):
  """
  print the out file.
  """
  with open(name, "r") as f:
    for line in f.readlines():
      print line.strip()

def create_random_input():
  """
  Generate valid random input data.
  """
  with open("sample-input.txt", "w") as f:
    teams = []
    for i in range(random.randint(1, 4)):
       teams.append("".join(random.sample(string.ascii_letters+string.digits, 5)))

    for i in range(random.randint(1,10)):
      scores = []
      for j in range(2):
        line = ""
        line += teams[(i+j)%len(teams)]
        line += " "
        line += str(random.randint(0, 3))
        scores.append(line)

      f.write(",".join(scores) + "\n")

def run_cmd(cmd):
  r = os.system(cmd)
  if r != 0:
    print "Command", cmd, "FAILED"
  else:
    print "Command", cmd, "PASSED"


# Run the tests:

# create data
create_random_input()
# print input file
print "Randomly creaed input soccer data"
print_file("sample-input.txt")

print "Redirect case"
r = run_cmd("python soccer.py < sample-input.txt")

# print put file
print_file("expected-output.txt")

print "pipe case"
run_cmd("cat sample-input.txt | python soccer.py")
# print put file
print_file("expected-output.txt")

print "file argument"
run_cmd("python soccer.py --file sample-input.txt")
# print put file
print_file("expected-output.txt")


