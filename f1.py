def binnarysearch(list,value):
    l=0
    h=len(list)-1
    print(h)
    print(l)

    while l <= h :

        m=(l+h) //2

        print(m)

        if list[m] == value:
            return True
        elif list[m] > value:

            h= m -1
        else:

            l= m +1

    return False



list=list(range(1,11))

value=9


toshow=binnarysearch(list,value)
print(toshow)










