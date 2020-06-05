import math
alpha = -1
def linreg():
    (pairs, length) = inputs()
    (xav, yav) = avg(pairs, length)
    (sx, sy) = stdev(pairs, length, xav, yav)

    r = zscore(pairs, xav, yav, sx, sy)/(length-1)
    slope = r *(sy/sx)
    b = yav - (slope*xav)
    display(slope, b, r)

def logreg():
    (pairs, length) = inputs()
    (xav, yav) = lnavg(pairs, length)
    (sxx, syy, sxy) = lnslope(pairs, xav, yav)
    r = lnr(sxx, syy, sxy)
    slope = sxy/sxx
    A = yav - slope*xav
    print(slope, A, r)
    display(slope, A, r)

def inputs():
    coordinates = []
    while True:
        tmp = input("Enter a coordinate pair:")
        if tmp == "done":
            break
        ltmp = tmp.split(',')
        tuptemp = (ltmp[0], ltmp[1])
        coordinates.append(tuptemp)
    return coordinates, len(coordinates)

def avg(l, length):
    xsum = 0
    ysum = 0
    for (x, y) in l:
        xsum = xsum + float(x)
        ysum = ysum + float(y)
    xavg = xsum/length
    yavg = ysum/length
    return xavg, yavg

def stdev(l, length, xavg, yavg):
    stx = 0
    sty = 0
    for (x, y) in l: #calculates stdev
        xtmp = (float(x)-xavg)**2
        stx = stx + xtmp

        ytmp = (float(y)-yavg)**2
        sty = sty + ytmp

    sx = (stx/(length-1))**(1/2)
    sy = (sty/(length-1))**(1/2)
    return sx, sy;

def zscore(l, xavg, yavg, sx, sy):
    xz = 0
    yz = 0
    zsum = 0
    for (x, y) in l:
        xz = (float(x) - xavg)/sx
        yz = (float(y) - yavg)/sy
        zsum = zsum + xz*yz
    return zsum

def display(a, b, r):
    if alpha == 0:
        print("The line of best fit is: " + str(a) + "x" + "+ " + str(b))
    elif alpha == 1:
        print("The curve of best fit is: " + str(b) + " + " + str(a) + "lnx")
    print("The correlation coefficient is: " + str(r))

def lnavg(l, length):
    xs = 0
    ys = 0
    for (x, y) in l:
        xs = xs + math.log(float(x))
        ys = ys + float(y)
    return xs/length, ys/length

def lnslope(l, xavg, yavg):
    xdifsum = 0
    ydifsum = 0
    sxy = 0
    for (x, y) in l:
        xtmp = math.log(float(x)) - xavg
        ytmp =  float(y) - yavg
        xdifsum = xdifsum + ((xtmp)**2)
        ydifsum = ydifsum + ((ytmp)**2)
        sxy = sxy + xtmp*ytmp
    return xdifsum, ydifsum, sxy

def lnr(a, b, c):
    d = a**(1/2)
    e = b**(1/2)
    return c/(d*e)

while True:
    type = input("Enter the type of regression: ")
    if type == "linear":
        alpha = 0
        linreg()
        break
    elif type == "logarithmic":
        alpha = 1
        logreg()
        break
    else:
        print("Enter a valid type")
        continue
