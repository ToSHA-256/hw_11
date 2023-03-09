def geom_progress(p, q):
    try:
        err = 0
        while err == 0:
            p *= q
            yield p
    except BaseException as xcp:
        print(xcp)
        err = 1


while True:
    try:
        print("Enter p for geometric progression")
        geom_p = float(input())
        print("Enter q for geometric progression")
        geom_q = float(input())
        geom = geom_progress(geom_p, geom_q)
        for itr in range(1, 10):
            print(next(geom))
    except ValueError:
        print("It must be int or float!")
