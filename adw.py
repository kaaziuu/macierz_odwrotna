import math
array = []
#autor Karol Kazmierczak

#obliczanie wyznacznika
def det_arr(arr):
    if len(arr) == 2:
        tmp = arr[0][0] * arr[1][1] - arr[0][1]*arr[1][0]
        return(tmp)
    if(len(arr) == 1) :
        return arr[0][0]
    sum= 0
    for  i, el in enumerate(arr[0]):
        tmp = []
        for y in range(1, len(arr)):
            tt = []
            for x in range(0, len(arr[0])):
                if(x != i):
                    tt.append(arr[y][x])
            tmp.append(tt)
        pow = 1+(i+1)
        tu = det_arr(tmp)
        sum+= math.pow(-1, pow)*el*tu

    return sum

# wylicznie elementu macierzy transponowanej
def create_el(x, y, arr):
    tmp = []
    for i ,line in enumerate(arr):
        ln = []
        for j, el in enumerate(line):
            if i!=y and j != x:
                ln.append(el)
        if(len(ln) > 0):
            tmp.append(ln)

    return det_arr(tmp)

# odwaranie macierzy
def reverse_arr(arr):
    new_arr = []
    for x in range(0,len(arr[0])):
        tmp = []
        for y in range(0, len(arr)):
            tmp.append(arr[y][x])

        new_arr.append(tmp)
    return new_arr

#  otworznie pliku i wczytanie danych
with open("tmp_1.txt", 'r') as f:
    for line in f.readlines():
        tmp = []
        line = line.split(",")
        for el in line:
            el = el.replace('\n', "")
            tmp.append(int(el))

        array.append(tmp)

det = det_arr(array)
if det == 0:
    print("brak macierzy odwrotnej")
else:
    d_arr = []
    # print(array)
    for y, line in enumerate(array):
        ln = []
        for x, el in enumerate(line):
            new = create_el(x, y, array)
            ln.append(new)
        d_arr.append(ln)

    new  = reverse_arr(d_arr)
    for i, line in enumerate(new):
        for j, el in enumerate(line):
            new[i][j] = el*(1/det)
    for line in new:
        print(line)