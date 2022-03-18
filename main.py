import Dominant_number
import Bridge
import time
import multiprocessing

g6 = open("test11.txt").read()
output = open("answer.txt", 'w')
g6 = g6.split('\n')
ans = [[0 for j in range(12)] for i in range(12)]


def run(line):
    d_number = Dominant_number.dominant(line)
    b_number = Bridge.bridges(line)
    ans[d_number][b_number] += 1
start = time.time()
for line in g6:
    if not line:
        break
    run(line)
end = time.time()
for line in ans:
    print("\t", line)
    output.write("".join(str(line)))
    output.write('\n')
print("Total time - " + str(end - start) + "c")

