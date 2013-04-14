#!/usr/bin/env python
import sys

if __name__ == "__main__":
    if len(sys.argv)!=3:
        exit(2)

    try:
        fpi_1=open(sys.argv[1],"r")
    except IOError:
        exit(1)

    try:
        fpi_2=open(sys.argv[2],"r")
        exit(1)

    #f[(state,tail,next)]
    f=dict()
    E=list()
    V=set()
    T=set()
    stack=list()

    for line in fpi_1:
        if line=="table:":
            break
        e=line.split():
