inp=map(int,raw_input().split())
for x in inp:
    inp.remove(x)
    if x in inp:
        print x 
        break
    else:continue
