import sys
import string

def ft_count_word():
    out = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    list_word = out.split(' ')
    list_new = []
    list_new += [i for i in list_word if (len(i) >= int(sys.argv[2]))]

    return(list_new)   

if (len(sys.argv) == 3):
    if (sys.argv[1].isdigit() == False and sys.argv[2].isdigit() == True):
        list_new = ft_count_word()
        print(list_new)
    else:
        print('ERROR')
else:
    print("ERROR")