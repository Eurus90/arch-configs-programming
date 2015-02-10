__author__ = 'lorcan'

abc = open("hnr1.abc", "r")

tune_count = 0

for line in abc:
    if line[:2] == "X:":
        tune_count += 1
        hasTitle = False
        print(tune_count)
    elif line[:2] == "T:":
        if not hasTitle:
            print("Title:  ", line[2:-1])
            hasTitle = True
    elif line[:2] == "M:":
        print("Time Sig:  ", line[2:-1])
    elif line[:2] == "K:":
        print("Key Sig:  ", line[2:-1], "\n\n")




