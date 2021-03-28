def myfunc(*args):
    return(args)

if __name__ == '__main__':
    a = myfunc([1,2], [1,2], [1,3])
    print(a)
