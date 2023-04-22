'''import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
        file.write("\n")
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\n")
    file.flush()
    
import time

for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(0.1)
    


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
    print()
    print(ret)'''
    
import time
inicio = time.time()
# Código a medir
time.sleep(1)
# -------------

fin = time.time()
time_ejec = fin - inicio
print(time_ejec) # 1.0005340576171875



def inf_sequence():
    num = '#'
    x =0
    while x < 3:
        yield num
        x += 1

         
for i in inf_sequence():
    print(i, end="")