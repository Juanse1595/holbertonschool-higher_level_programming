#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for index in range(1, len(sys.argv)):
            add = add + int(sys.argv[index])
        print("{}".format(add))
