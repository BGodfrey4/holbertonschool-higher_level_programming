#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    a = len(sys.argv)
    if a == 1:
    	print("0 arguments.")
		break
    elif a == 2:
    	print("1 argument:")
    print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(a-1))
    for i in range(1, a):
        print("{:d}: {:s}".format(i, sys.argv[i]))
