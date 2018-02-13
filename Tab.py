
import sys

original = sys.argv[1]
trans = sys.argv[2]

f = open(original)
cab = f.read()
f.close()

change = cab.replace("\t", " "*8)
print(change)
