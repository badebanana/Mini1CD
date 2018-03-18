from Server import *

functions = {
    "Add": {"x": 0, "y": 0},
    "Sub": {"x": 0, "y": 0},
    "Mul": {"x": 0, "y": 0},
}

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

for k,v in functions.items():
    if msg.upper() == k.upper():
        for i in functions.values():
            i["x"] = 2
            i["y"] = 2
    msg = add(v["x"], v["y"])

