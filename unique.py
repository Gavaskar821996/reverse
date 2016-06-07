inp=map(int,raw_input().split())
for x in inp:
    inp.remove(x)
    if x not in inp:print x
    else:continue
