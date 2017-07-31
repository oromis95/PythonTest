import sys
import os
import random
import time

start = time.time()
counter = 0
for i in range(0, 10000000):
    a = random.normalvariate(5, 2.5)
    if (a < 0 or a > 10):
        counter += 1
timeElapsed = time.time() - start
print("Out of range %d " % counter)
print("Eseguito in %f" % timeElapsed)
