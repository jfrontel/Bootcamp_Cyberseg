import sys
import time



def ft_progress(it, size=21, j=0):
    count = len(it)

    def show(j):
        x = int(size*j/count) 
        sys.stdout.write("ETA: %.2fs [%.2i%s][%s>%s] %i/%i | elapsed time %.2f\r" % (time_load, x/size*100, "%", "="*x, " "*(size-x-1), j, count, time_total))
        sys.stdout.flush()
    for i, item in enumerate(it):
        yield item
        show(i+1)

time_load = 0  
listy = range(1000)
ret = 0
for i in ft_progress(listy):
    inicio = time.time()
    ret += (i + 3) % 5
    time.sleep(0.01)
    fin = time.time()
    time_total = (fin - inicio) * len(listy)
    time_load += (fin - inicio)

print(f"\n{ret}")

