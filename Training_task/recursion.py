
def coutdown(i):
    print (i)
    if i <= 0:
        return
    else:
        coutdown(i -1)

coutdown(4)