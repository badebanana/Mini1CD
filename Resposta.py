from Functions import *

for v in functions.values():
    v["x"] = 2
    v["y"] = 2
val = add(v["x"], v["y"])
print('Resposta:', val)