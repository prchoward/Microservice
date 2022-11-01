import time
import os
import random
while True:
    random.seed()
    time.sleep(5)
    f = open("studentservice.txt", "r+")
    with open("studentservice.txt", "r+"):
        text = f.read()
        if 'run' in text:
            f.close()
            name = input()
            f = open(name, "r")
            with open(name, "r") as f:
                content = f.read()
                print(content + "\n")
