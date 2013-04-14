#!/usr/bin/env python
import sys
E=list()
first=dict()
V=set()
T=set()
G=list()
belong=dict()
terminal="#"
eps="0"
def FIRST_(X):

    if (first.has_key(X)):
        return first[X];
    ret=set()
    epss=set([eps])

    if X in  V:
        for e in E:
            if e[0]==X :
                if len(e)==1:
                    ret.add(eps)
                else :
                    for i in range(1,len(e)):
		        if e[i]==X:
		            break
                        ex=FIRST_(e[i])
                        if eps in ex:
                            ret=ret|(ex-epss)
                        else:
                            ret=ret|ex
                            break
                    else :
                        ret.add(eps)
    else:
        ret.add(X)
    
    first[X]=ret;
    return ret

def FIRST(x,tail):
    x.append(tail)
    ret=set()
    epss=set([eps])
    ret=ret|FIRST_(x[0])-epss
    for k in range(len(x)):
        xk=FIRST_(x[k])
        if eps in xk:
            ret=ret|xk-epss
        else:
            ret|=xk
            break
    else :
        ret.add(eps)
    return ret

#input the project ,return the id of project set.
def CLOSURE(I):
    C=list(I)

    for p in C:
        e=E[p[0]]
        pos=p[1]
        if pos+1<len(e):
            if not e[pos+1] in V:
                continue
            for j in range(len(E)):
                if E[j][0]==e[pos+1]:
                    if pos+2<len(e):
                        for tail in FIRST(e[pos+2:],p[2]):
                            if not (j,0,tail) in C:
                                C.append((j,0,tail))
                    else :
                        if not (j,0,p[2]) in C:
                            C.append((j,0,p[2]))
    return set(C)   

#input the project and the next notation,return the id of the next project set.
def GO(I,X):
    J=set()
    for p in I:
        e=E[p[0]]
        pos=p[1]
        if pos+1<len(e) and e[pos+1]==X:
            J.add((p[0],p[1]+1,p[2]))
    return CLOSURE(J)

#
def BUILD_G():
    C=G
    C.append(CLOSURE(set([(0,0,'#')])) )
    for I in C:
        for X in (T | V):
            J=GO(I,X)
            if len(J)>0 and not J in C:
                C.append(J)

    return C

#
action=dict()
goto=dict()
n=0
def BUILD_table():
    BUILD_G()
    n=len(G)

    for k in range(n):
        Ik=G[k]
        for a in T:
            Ij=GO(Ik,a)
            if len(Ij)>0 :
                j=G.index(Ij)
                if action.has_key((k,a)) and action[(k,a)]!=("S",j):
                    sys.stderr.write("Ambiguous grammar(S)!\n")
                    exit(3)
                action[(k,a)]=("S",j)

        for b in V:
            Ij=GO(Ik,b)
            if len(Ij)>0 :
                j=G.index(Ij)
                goto[(k,b)]=j

        for p in Ik:
            if p[1]+1==len(E[p[0]]):
                if action.has_key((k,p[2])) and action[(k,p[2])]!=("r",p[0]) and action[(k,p[2])][0]!="S":
                    sys.stderr.write("Ambiguous grammar(r)!\n"+"action[%s,%s]=(r%d)(r%d)\n"%(k,p[2],action[(k,p[2])][1],p[0]))
		    sys.stderr.write(" ".join(E[p[0]])+"\n")
		    sys.stderr.write(" ".join(E[action[(k,p[2])][1]])+"\n")
                    exit(3)
                action[(k,p[2])]=("r",p[0])

        if (0,1,terminal) in Ik:
            action[(k,terminal)]=("acc",0)

#__main_program__
if __name__=="__main__":
    
    if len(sys.argv)!=4:
        exit(2)

    try:
        input_file=open(sys.argv[1],"r");
    except IOError:
        exit(1)
    width=list()
    width.append(int(sys.argv[2]))
    width.append(int(sys.argv[3]))
    
    for line in input_file:
        e=line.split()
        if len(e)<1:
            continue
        E.append(e)
        print e
        V.add(e[0])
        for i in e:
            T.add(i)

    T=T-V 
    T.add(terminal)
    print "V=",V
    print "T=",T
    BUILD_table()
    #print "first=",first
    for i in range(len(G)):
        print "[%+*s]"%(width[0],str(i))
        for j in G[i]:
            print "     ",j
    print "[%+*.s]"%(width[0]," "),
    for j in T:
        print "%+*s|"%(width[1],j),
    for j in V:
        print "%+*s|"%(width[1],j),
    print 

    for i in range(len(G)):
        print "[%+*s]"%(width[0],str(i)),
        for j in T:
            a=""
            if (i,j) in action:
                a="%s%d"%action[(i,j)]
            print "%+*s|"%(width[1],a),

        for j in V:
            a=""
            if (i,j) in goto:
                a="%d"%goto[(i,j)]
            print "%+*s|"%(width[1],a),
        print 

