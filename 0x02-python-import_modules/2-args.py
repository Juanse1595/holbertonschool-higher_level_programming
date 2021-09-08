#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    if argv_len <= 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv_len))
        for index in range(1, argv_len + 1):
            print("{}: {}".format(index, sys.argv[index]))
