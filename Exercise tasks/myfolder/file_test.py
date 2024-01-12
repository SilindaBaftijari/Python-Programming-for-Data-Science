
filename = "Exercise tasks/hello.txt"
reader = open(filename, 'r')
lines = reader.readlines()
print(lines[-2].strip())
print(lines[-1].strip())

