from sys import stdin

top = [[0]]

for _ in range(4):
    a = stdin.readline()[:-1]
    top.append([int(x) for x in str(a)])

def rotate(arr):
    a = arr.pop()
    arr.insert(0,a)

def R_rotate(arr):
    a = arr[0]
    del arr[0]
    arr.append(a)

def wrap_rotate(arr, dir):
    if dir == 1:
        rotate(arr)
    elif dir == -1:
        R_rotate(arr)
    else:
        pass

def cal_point(top):
    res = 0
    for i in range(4):
        if(top[i + 1][0] == 1):
            res += pow(2, i)
    return res

k = int(stdin.readline())

while (k):
    num, dir = map(int, stdin.readline().split(' '))
    check = [0, 0, 0, 0, 0]
    check[num] = dir
    for i in range(num, 4):
        if (top[i][2] != top[i+1][6]):
            check[i+1] = check[i] * -1
    for i in range(num, 1, -1):
        if(top[i][6] != top[i-1][2]):
            check[i-1] = check[i] * -1

    for i in range(1, 5):
        wrap_rotate(top[i], check[i])

    k -=1

print(cal_point(top))