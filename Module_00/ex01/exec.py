import sys
i = 1
size = len(sys.argv)
if (len(sys.argv) == 1):
    print("Dame al menos un argumento, por favor")
else:
    string = sys.argv[1]
    i = i + 1
    while (i < size):
        if sys.argv[i] == '':
            string = string + '' + sys.argv[i]
        else:
            string = string + ' ' + sys.argv[i]
        i = i + 1
    string_swap = string.swapcase()
    print(string_swap[::-1])
